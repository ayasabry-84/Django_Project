# My Django Project

This project is a **Django-based Task Management API** built with **Django REST Framework**. It provides a robust backend solution for managing tasks efficiently, offering a comprehensive set of features for users to create, read, update, and delete tasks.

### **Key Features**
- **Task Management**: Create, read, update, and delete tasks with attributes such as title, description, due date, priority, and status.
- **User Authentication**: Secure access to tasks with user authentication, ensuring each user can only manage their own tasks.
- **Task Filtering and Sorting**: Filter and sort tasks based on criteria like priority, status, or due date.
- **Error Handling**: Proper error handling with appropriate HTTP status codes for a seamless user experience.

### **Purpose**
This project aims to deliver a **reliable and user-friendly solution** for task management, empowering users to stay organized and productive. Whether you're managing personal tasks or collaborating with a team, this API provides the tools you need to stay on top of your work.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ayasabry-84/Task_Management_API.git
2. Navigate to the project directory:
   ```bash
   cd Task_Management_API
3. Create a virtual environment:
   ```bash
   python -m venv venv
   
4. Activate the virtual environment:
  On Windows:
     ```bash
     .\venv\Scripts\activate
         
5. Install dependencies:
   ```bash
   pip install -r requirements.txt

6. Run migrations:
   ```bash
   python manage.py migrate
   
7. Start the development server:
   ```bash
   python manage.py runserver

## Usage 🚀

 ### API Endpoints
 
 #### **Get All Tasks📋**
     GET /api/tasks/
 #### **Create a Task ➕**
     POST /api/tasks/
 #### **Example Request Body:**
     {
     "title": "Complete documentation",
     "description": "Write the README.md file",
     "status": "In Progress"
     }
 
 #### **Get Task Details 🔍**
     GET /api/tasks/1/
 
 #### **Update a Task ✏️**
     PUT /api/tasks/1/
 
 #### **Example Request Body:**
     {
       "title": "Updated Task Title",
       "description": "Updated task description",
       "status": "Completed"
     }
 
 #### **Delete a Task 🗑️**
     DELETE /api/tasks/1/
 
 
 #### **API Endpoints Summary 📊**
 - User Authentication
   | Method | URL             | Description                     |
   |--------|-----------------|---------------------------------|
   | POST   | `/register/`    | Register a new user.            |
   | PUT    | `/update/`      | Update user details.            |
   | POST   | `/login/`       | Log in a user.                  |
   | DELETE | `/delete/`      | Delete a user account.          |
   | POST   | `/logout/`      | Log out a user.                 |
   
 - Task Management
   | Method | URL             | Description                     |
   |--------|-----------------|---------------------------------|
   | GET    | `/api/tasks/`   | Get a list of all tasks.        |
   | POST   | `/api/tasks/`   | Create a new task.              |
   | GET    | `/api/tasks/1/` | Get details of a specific task. |
   | PUT    | `/api/tasks/1/` | Update a specific task.         |
   | DELETE | `/api/tasks/1/` | Delete a specific task.         |

## Contributing
 Contributions are welcome! Please follow these steps:
 
 1. Fork the repository.
 2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
 3. Commit your changes:
    ```bash
    git commit -m "Add your feature"
 4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
 5. Open a pull request.


## Acknowledgments
- [Django](https://www.djangoproject.com/) - The web framework used.
- [Django REST Framework](https://www.django-rest-framework.org/) - For building the API.


## Contact
 For questions or feedback, please contact [Aya Sabry](mailto:ayasabryy017@gmail.com) or open an issue on [GitHub](https://github.com/ayasabry-84/Task_Management_API/issues).
