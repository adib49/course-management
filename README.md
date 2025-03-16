Course Management System , role based access control (RBAC) , backend to add roles and content (courses) based on roles.
## Features

- **Admin Dashboard**: Manage users and view all courses.
- **Instructor Dashboard**: Create, edit, and delete courses.
- **Student Dashboard**: View enrolled courses.
- **User Authentication**: Login and logout functionality.

  ## Installation
  
1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd CourseManagementSystem
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```
3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```sh
    python manage.py runserver
    ```
## Usage

- **Admin Dashboard**: Accessible at `/admin-dashboard/`. Allows managing users and viewing all courses.
- **Instructor Dashboard**: Accessible at `/instructor-dashboard/`. Allows creating, editing, and deleting courses.
- **Student Dashboard**: Accessible at `/student-dashboard/`. Allows viewing enrolled courses.
- **Login**: Accessible at `/`.


## File Descriptions

- **`src/cms/settings.py`**: Django settings for the project.
- **`src/cms/urls.py`**: URL configuration for the project.
- **`src/cms_app/views.py`**: Contains view functions for handling requests.
- **`src/cms_app/models.py`**: Defines the data models for the application.
- **`src/cms_app/forms.py`**: Contains form definitions for user input.
- **[cms_app](http://_vscodecontentref_/11)**: Contains HTML templates for rendering views.
