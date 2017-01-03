from fabric.api import *
from fabric.tasks import execute

#----------------------------------------------------------
## Update Ubuntu packages.

def execute_update_packages(env, hosts):
    execute(update_packages, hosts=hosts, env=env)

def update_packages(env):
    local("echo Updating package repositories...")
    sudo('apt-get update')

#----------------------------------------------------------