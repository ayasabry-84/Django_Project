from urllib import request
from django.contrib.auth import get_user_model, authenticate
from rest_framework import status, permissions, generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, LoginSerializer, TaskSerializer , TaskUpdateSerializer
from .models import CustomUser, Task
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from django.utils import timezone
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

class RegisterUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            # Generate a token for the newly registered user
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": serializer.data,
                "token": token.key,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        return self.request.user


class LoginUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            # Generate or retrieve the user's token
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class DeleteUserView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        return self.request.user  # We get the currently authenticated user

    def destroy(self, request, *args, **kwargs):
        # Call the original destroy method to delete the user
        response = super().destroy(request, *args, **kwargs)
        
        # Custom message after user is deleted
        return Response({
            "message": "User deleted successfully."
        }, status=status.HTTP_200_OK)


class LogoutUserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        try:
            # Delete the user's token to log them out
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "User not logged in"}, status=status.HTTP_400_BAD_REQUEST)

class TaskFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status', lookup_expr='iexact')
    priority = filters.CharFilter(field_name='priority', lookup_expr='iexact')
    due_date = filters.DateFromToRangeFilter(field_name='due_date')

    class Meta:
        model = Task
        fields = ['status', 'priority', 'due_date']

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = TaskFilter
    ordering_fields = ['due_date', 'priority']
    search_fields = ['title', 'description']  # إضافة بحث في العنوان والوصف لو احتاجتي
    
    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)

        # فلترة حسب status
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)

        # فلترة حسب priority
        priority = self.request.query_params.get('priority', None)
        if priority:
            queryset = queryset.filter(priority=priority)

        # فلترة حسب due_date
        due_date = self.request.query_params.get('due_date', None)
        if due_date:
            queryset = queryset.filter(due_date=due_date)

        return queryset


    def perform_create(self, serializer):
        # Save the task with the logged-in user
        task = serializer.save(user=self.request.user)  # ربط الـ task بالـ user و حفظه
        # Returning the task data including the id
        return Response({
            "id": task.id,  # Return the id of the newly created task
            "message": "Task created successfully"
    }, status=status.HTTP_201_CREATED)


    def get_serializer_class(self):
        # Use the regular TaskSerializer for list and create operations
        if self.action in ['update', 'partial_update']:
            return TaskUpdateSerializer
        return TaskSerializer

    def get_object(self):
        task = super().get_object()
        # Ensure the task belongs to the logged-in user
        if task.user != self.request.user:
            raise PermissionDenied("You do not have permission to access this task.")
        return task

    @action(detail=True, methods=['patch'])
    def partial_update_task(self, request, pk=None):
        task = self.get_object()

        if task.status == 'Completed':
            raise PermissionDenied("You cannot update a completed task.")

        serializer = self.get_serializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def update_task(self, request, pk=None):
        task = self.get_object()

        if task.status == 'Completed':
            raise PermissionDenied("You cannot update a completed task.")

        # Update the task with full data (not partial)
        serializer = self.get_serializer(task, data=request.data, partial=False)  # Full update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete_task(self, request, pk=None):
        task = self.get_object()
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['patch'])
    def mark_complete(self, request, pk=None):
        task = self.get_object()

        # Prevent updating a completed task
        if task.status == 'Completed':
            raise PermissionDenied("You cannot update a completed task.")

        task.status = 'Completed'
        task.completed_at = timezone.now()  # Set the completion timestamp
        task.save()

        return Response({
            "id": task.id,
            "message": "Task marked as complete",
            "completed_at": task.completed_at
        }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'])
    def mark_incomplete(self, request, pk=None):
        task = self.get_object()

        if task.status == 'Pending':
            raise PermissionDenied("Task is already incomplete.")

        task.status = 'Pending'
        task.completed_at = None  # Clear the completion timestamp
        task.save()

        return Response({
            "id": task.id,
            "message": "Task reverted to incomplete"
        }, status=status.HTTP_200_OK)
    