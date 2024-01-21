# Django-Learning
# devsearch is the root folder
# Adding virtualenv 
    >>virtualenv <name of virtual env>
# Activating Virtual Env
    >>django_app\Scripts.\activate

# Deactivating Virtual Env
    >>deactivate
# Installing requirements.txt
    >> pip install -r requirements.txt
# django-admin useful commands:
    makemigrations : preps db for migrations
    migrate : Executes the migrations of makemigrations and makes the db tables
    runserver : runs the server
    startproject : creates a django project
    startapp :  creates a django app
# Django migration commands
    python manage.py makemigrations
    python manage.py migrate

# Creating a django project
    django-admin startproject devsearch 

# Run server command at DEVSEARCH
    python manage.py runserver

# settings.py 
    main project configuration file for django project

# urls.py
    url navigation file 
# wsgi
    Web server gateway interface
# asgi
    Asynchronous server gateway interface

# App Files:
    # models.py
        contains the database tables
    # views.py 
        contains all the business logic , all the functions that will be triggered when the urls are
        activated
    # apps.py
        app config
    # admin.py
        main admin panel config

# Telling Django about new app
    We need to add app to "Installed App" list so that django knows about the app we created
    # Go to devsearch/devsearch/settings.py and add:
        <app name>.apps.<main class name>
        example:
            projects.apps.ProjectsConfig

# Python manage.py createsuperuser
    Command to create superuser

# python manage.py shell
    Command to enter shell
    
