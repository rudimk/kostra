from fabric.api import *
from fabric.tasks import execute

def execute_update_packages(env, hosts):
    print hosts
    print env
    execute(update_packages, hosts=hosts, env=env)

def update_packages(env):
    local("echo Updating package repositories...")
    sudo('apt-get update')