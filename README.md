# User Events

User Events is a web application where users can log in, create and publish events with
titles and description.

Functions
---------------

1. Registration with email and password.
2. Login with email and password.
3. Any logged in user can create events.
4. Logged in user can edit and delete own events.
5. Logged in user can participate in events.


Getting Started
---------------

To work on the sample code, you'll need to clone project's repository to your
local computer. If you haven't, do that first. 

github repo :

bitbucket repo :

git clone 

1. Create a Python virtual environment for your Django project. This virtual
environment allows you to isolate this project and install any packages you
need without affecting the system Python installation. At the terminal, type
the following command:

    $ virtualenv -p python3.6 venv

2. Activate the virtual environment:

    $ source venv/bin/activate

3. Install Python dependencies for this project:

    $ pip install -r requirements.txt

4. For Database schema:

    $ python manage.py migrate

5. Create Super User

    $ python manage.py createsupersuer

6. Start the Django development server:

    $ python manage.py runserver

7. Open http://127.0.0.1:8000/ in a web browser to view your application.



What's Here
-----------

This sample includes:

* README.md - this file
* userevents/ - this directory contains your Django project files
* events/ - this directory contains your Django application files
* manage.py - this Python script is used to start your Django web application
* static/ - this directory contains static web assets used by your application
* templates/ - this directory contains templates used by your application


Data Base Schema
----------------

User Related with Event Model
