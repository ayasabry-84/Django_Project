 # My Django Project

This project is a Django application for Task Management.
It is a backend project built with Django and Django REST Framework, designed to allow users to manage their tasks efficiently. It provides a set of endpoints for creating, reading, updating, and deleting tasks, with attributes such as title, description, due date, priority, and status. 
Users can also mark tasks as complete or incomplete and filter or sort tasks based on various criteria. The API includes user authentication, ensuring secure access to each user’s tasks, and employs proper error handling with HTTP status codes. 
This project aims to deliver a robust, scalable, and secure solution for task management in both development and production environments.


## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ayasabry-84/Django_Project.git

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Task_Management_API.git
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

## Usage
API Endpoints
 - Get All Tasks:
    ```bash
    GET /api/tasks/
 - Create a Task:
    ```bash
    POST /api/tasks/
 - Example Request Body:
   ```json
   {
   "title": "Complete documentation",
   "description": "Write the README.md file",
   "status": "In Progress"
   }
API Endpoints
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
