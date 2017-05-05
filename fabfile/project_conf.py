'''
--------------------------------------------------------------------------------------
project_conf.py
--------------------------------------------------------------------------------------
Configuration settings that detail your EC2 instances and other info about your Django
servers

author : Ashok Fernandez (github.com/ashokfernandez/)
credit : Derived from files in https://github.com/gcollazo/Fabulous
date   : 11 / 3 / 2014

Make sure you fill everything out that looks like it needs to be filled out, there are links
in the comments to help.
'''

import os.path

fabconf = {}

#  Do not edit
fabconf['FAB_CONFIG_PATH'] = os.path.dirname(__file__)

# Project name
fabconf['PROJECT_NAME'] = ""

# Username for connecting to EC2 instaces - Do not edit unless you have a
# reason to
fabconf['SERVER_USERNAME'] = "ubuntu"

# Full local path for .ssh
fabconf['SSH_PATH'] = "~/.ssh"

# Name of the private key .pem file you use to connect to EC2 instances
fabconf['EC2_KEY_NAME'] = ""

# Don't edit. Full path of the ssh key you use to connect to EC2 instances
fabconf[
    'SSH_PRIVATE_KEY_PATH'] = '%s/%s' % (fabconf['SSH_PATH'], fabconf['EC2_KEY_NAME'])
print(fabconf['SSH_PRIVATE_KEY_PATH'])
# Where to install apps
fabconf['APPS_DIR'] = "/home/%s/webapps" % fabconf['SERVER_USERNAME']

# Where you want your project installed: /APPS_DIR/PROJECT_NAME
fabconf[
    'PROJECT_PATH'] = "%s/%s" % (fabconf['APPS_DIR'], fabconf['PROJECT_NAME'])

# Sub project
fabconf['SUB_PROJECT_PATH'] = "%s/%s/%s" % (fabconf['APPS_DIR'], fabconf['PROJECT_NAME'], fabconf['PROJECT_NAME'])

# Your Django's version "run migrations" command
fabconf['RUN_MIGRATIONS_CMD'] = "python %s/manage.py migrate" % fabconf['PROJECT_PATH']

# App domains
fabconf['DOMAINS'] = "example.com www.example.com"

# Path for virtualenvs
fabconf['VIRTUALENV_DIR'] = "/home/%s/.virtualenvs" % fabconf['SERVER_USERNAME']

# Email for the server admin
fabconf['ADMIN_EMAIL'] = ""

# Git username for the server
fabconf['GIT_USERNAME'] = ""

# Name of the private key file used for git deployments
fabconf['GIT_DEPLOY_KEY_NAME'] = ""

# Don't edit. Local path for deployment key you use for git
fabconf['GIT_DEPLOY_KEY_PATH'] = "%s/%s" % (
    fabconf['SSH_PATH'], fabconf['GIT_DEPLOY_KEY_NAME'])

# The top-level domain name for your remote git service
fabconf['GIT_HOST_DOMAIN'] = "github.com"

# Path to the repo of the application you want to install. The
# REPO_USERNAME could be same as the GIT_USERNAME if the repo is under the
# same account else, it is the org username (for orgs) or the username of
# the projects owner. The REPO_NAME can contain slashes (eg
# <project_name>/<repo_name> if you are using Bitbucket and the project is
# within a project)
fabconf['REPO_USERNAME'] = ''
fabconf['REPO_NAME'] = ''

# Creates the ssh location of your remote repo from the above details
fabconf['REPO_URL'] = "ssh://git@%s/%s/%s.git" % (
    fabconf['GIT_HOST_DOMAIN'], fabconf['REPO_USERNAME'], fabconf['REPO_NAME'])

# Virtualenv activate command
fabconf['ACTIVATE'] = "source /home/%s/.virtualenvs/%s/bin/activate" % (
    fabconf['SERVER_USERNAME'], fabconf['PROJECT_NAME'])

# Name tag for your server instance on EC2
fabconf['INSTANCE_NAME_TAG'] = ""

# EC2 key. http://bit.ly/j5ImEZ
fabconf['AWS_ACCESS_KEY'] = ''

# EC2 secret. http://bit.ly/j5ImEZ
fabconf['AWS_SECRET_KEY'] = ''

# EC2 region. http://amzn.to/12jBkm7
ec2_region = 'us-west-2'

# AMI name. http://bit.ly/liLKxj #for Ubuntu AMI in Oregon; different for other Availability Zones
ec2_amis = ['ami-efd0428f']

# Name of the keypair you use in EC2. http://bit.ly/ldw0HZ
ec2_keypair = ''

# Name of the security group. http://bit.ly/kl0Jyn
ec2_secgroups = []

# API Name of instance type. http://bit.ly/mkWvpn
# t2.micro for free tier
ec2_instancetype = 't2.micro'

# Existing instances - add the public dns of your instances here when you have spawned them
fabconf['EC2_INSTANCES'] = []
