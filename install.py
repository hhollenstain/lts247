#!/usr/bin/python
#Simple local config/install script. Requires docker/docker-compose already installed
import argparse
import docker
import os.path
import subprocess
from shutil import copyfile

currentWorkingDir = os.path.dirname(os.path.realpath(__file__))
#starting up containers
def composeUp():
    cmd = ['docker-compose up -d']
    process = subprocess.Popen(cmd, shell=True, cwd=currentWorkingDir)
    print('INFO: Running docker-compose up -d')
    out, err = process.communicate()
    errcode = process.returncode

#Installing extensions from the extensions listed in extension.list
def installExtensions():
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    extensions = open('%s/extension.list' % currentWorkingDir, 'r')
    for ext in extensions:
        print('INFO: Loading extension: %s' % ext)
        exec_id = client.exec_create( container='flarum', cmd='extension require %s' % (ext), tty=True)
        generator = client.exec_start(exec_id, stream=True)
        for x in generator:
            print x


class __main__():
    actions = [
            'build',
            'update'
          ]
    #building Arg praser for options
    parser = argparse.ArgumentParser()
    parser.add_argument('action', help='build, update')
    args = parser.parse_args()

    if args.action:
        if args.action not in actions:
            print 'ERROR:  Unrecongizned action: %s, please use one of the allowed actions %s' % (args.action, `actions`)
            sys.exit(1)

    if args.action == "build":
        composeUp()
        installExtensions()

    if args.action == "update":
        installExtensions()
