from django.urls import path , include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token


from rest_framework.routers import DefaultRouter
from .views import RegisterUserView, UpdateUserView, DeleteUserView, TaskViewSet, LogoutUserView , LoginUserView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/token-auth/', obtain_auth_token, name='token_auth'),

   
    path('register/', RegisterUserView.as_view(), name='register'),
    path('update/', UpdateUserView.as_view(), name='update_user'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('delete/', DeleteUserView.as_view(), name='delete_user'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('', include(router.urls)),  # تسجيل جميع الـ API Endpoints الخاصة بالـ tasks
]


