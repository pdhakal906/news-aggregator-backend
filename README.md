# For Backend

Fist clone the repository.  
Then,
Create and activate **virtual environment**.

Create a **Postgres** database and a user.

Create a **.env** file and add database configuration:

**DATABASE_ENGINE = yourdatabaseengine** <br>
**DATABASE_NAME = yourdatabasename** <br>
**DATABASE_USERNAME = yourdatabaseusername** <br>
**DATABASE_PASSWORD = yourdatabasepassword** <br>
**DATABASE_HOST = yourdatbasehost** <br>
**DATABASE_PORT = yourdatabaseport** <br>

Then install requirements:
**pip install -r requirements.txt**

After that, run migrations:
**python manage.py migrate**

Next, make migrations:
**python manage.py makemigrations api**

Run migrations again:
**python manage.py migrate**

Create a superuser:
**python manage.py createsuperuser**

Then start server to get the API up and running:
**python manage.py runserver**
