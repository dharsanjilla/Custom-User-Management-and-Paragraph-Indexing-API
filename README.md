My Django REST framework 
This is a Django REST API project that allows users to interact with various endpoints for managing paragraphs and performing searches.

Table of Contents
Features
Tech Stack
Installation
Usage
API Endpoints
Testing
Deployment
Features
User authentication and authorization
CRUD operations for managing paragraphs
Search functionality to find paragraphs containing specific words
Dockerized environment for easy setup
Tech Stack
Django REST Framework
PostgreSQL
Docker
Postman (for API testing)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/your-repo.git
Navigate to the project directory:

bash
Copy code
cd your-repo
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory.
Add the required environment variables (e.g., database credentials, secret keys).
Apply migrations:

bash
Copy code
python manage.py migrate
Usage
Start the development server:

bash
Copy code
python manage.py runserver
Access the API at http://127.0.0.1:8000/.

I have used sqlite as database to use postgressql change 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_django_project',  # Replace with your database name
        'USER': 'your_username',  # Replace with your PostgreSQL user
        'PASSWORD': 'your_password',  # Replace with your PostgreSQL password
        'HOST': 'localhost',  # Change if your PostgreSQL server is on a different machine
        'PORT': '5432',  # Default PostgreSQL port
    }
}


Create User account by navigating to api/register
To log in into account navigate through api/login
After logging in  navigate to api/paragraphs to upload paragraph
To search the words appeared in paragraph navigate to api/search 

Use Postman or any API client to interact with the endpoints.

Json Format for register and login  {"email":"example email","username":"example user","password":"example password"}
for paragraph {"content":"example paragraph"}
for search {"word":""}



API Endpoints
/api/users/: CRUD operations for users (requires authentication)
/api/paragraphs/: CRUD operations for paragraphs (requires authentication)
/api/search/?word=<search_word>: Search for paragraphs containing the specified word


Testing
Run unit tests:

bash
Copy code
python manage.py test
Test API endpoints using Postman or automated testing tools.

Deployment
Deploy the API to your preferred hosting platform (e.g., Heroku, AWS).
Configure environment variables and database settings for production.
Contributing
Contributions are welcome! Fork the repository, make changes, and submit a pull request.


