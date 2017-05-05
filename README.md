# Django Fabric AWS Python3
### A Fabric script to manage a Django deployment on Amazon AWS in Python3

This project is a Python3 extension for [Django Fabric AWS](https://github.com/ashokfernandez/Django-Fabric-AWS)

This fabfile along with the provided templates can spawn EC2 instances, install and configure a stateless Django stack on them (nginx + gunicorn with Amazon S3 for staticfiles). 

Furthermore it can update your instances from a git repo stored on bitbucket [private repos are free on bitbucket so you can run private stuff on your server]

## Author
[Ankit Agrawal](https://github.com/ankitmaverick/)

## Acknowledgements
[Django Fabric AWS](https://github.com/ashokfernandez/Django-Fabric-AWS)
[Fabulous](https://github.com/gcollazo/Fabulous) by [Giovanni Collazo](https://github.com/gcollazo).


## Installation
 * Download this repo and drag the **fabfile** folder into the root directory of your Django project. 
 * cd into the folder and run `pip install -r requirements.txt`

## Setting up Your Django Project
See an [example here](https://github.com/ashokfernandez/Django-Fabric-AWS---amazon_app) of how to setup your Django project using the following instructions.

 * Create a folder in the root directory of your Django project called **requirements** that has three pip requirements files in it:
    * **common.txt** for all your common python dependancies between the server and local (add Django to this)
    * **dev.txt** for your local python dependancies
    * **prod.txt** for your server python dependancies (add boto, django-storages and psycopg2 to this)

* Create a folder where the settings.py of your Django project is located called **settings** that has four Python files in it
    * **\__init__.py**
    * **common.py** for all your common Django settings
    * **dev.py** for your local Django settings
    * **prod.py** for your server Django settings
* At the top of both **dev.py** and **prod.py** add the line `from <django_project_name>.settings.common import *`
* Change the `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<django_project_name>.settings")` in both wsgi.py and manage.py to `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<django_project_name>.settings.prod")`. This means that the project with default to the production settings, however you can run it locally using `python manage.py runserver --settings=<django_project_name>.settings.dev`
* [Setup a set of SSH keys](https://confluence.atlassian.com/display/BITBUCKET/Set+up+SSH+for+Git) for the bitbucket account where your repo is hosted
* Provision an S3 bucket for the staticfiles and add the following to **settings/prod.py**
    
        INSTALLED_APPS += ('storages',)
        AWS_STORAGE_BUCKET_NAME = "<s3_staticfiles_bucket_name>"
        STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
        S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
        STATIC_URL = S3_URL

* Fill out the details in **fabfile/project_conf.py**

## Commands
After all that work you can now run these commands which will execute across all your EC2 instances

- `fab spawn instance` 
    - Spawns a new EC2 instance (as definied in project_conf.py) and return's it's public dns. This takes around 8 minutes to complete.

- `fab update_packages`
    - Updates the python packages on the server to match those found in requirements/common.txt and 
      requirements/prod.txt

- `fab deploy`
    - Pulls the latest commit from the master branch on the server, collects the static files, syncs the db and                   
      restarts the server

- `fab reload_gunicorn`
    - Pushes the gunicorn startup script to the servers and restarts the gunicorn process, use this if you 
      have made changes to templates/start_gunicorn.bash

- `fab reload_nginx`
    - Pushes the nginx config files to the servers and restarts the nginx, use this if you 
      have made changes to templates/nginx-app-proxy or templates/nginx.conf

- `fab reload_supervisor`
    - Pushes the supervisor config files to the servers and restarts the supervisor, use this if you 
      have made changes to templates/supervisord-init or templates/supervisord.conf

- `fab manage:command="management command"`
    - Runs a python manage.py command on the server. To run this command we need to specify an argument, eg for syncdb
      type the command -> fab manage:command="syncdb --no-input"

