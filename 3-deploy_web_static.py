#!/usr/bin/python3
""" Fabric script for deploying web_static """

from fabric.api import run, put, env, local
from os.path import exists
from datetime import datetime
import os

env.hosts = ['100.26.250.129', '54.210.53.36']
env.user = 'ubuntu'


"""def do_pack():
    #generates a .tgz archive from the contents of the web_static folder 
    try:
        local("mkdir -p versions")
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(date_time)
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None


def do_deploy(archive_path):
   # deploy an archive to your web servers 
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        put(archive_path, '/tmp/{}'.format(archive_name))

        archive_base = archive_name.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_base))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive_name, archive_base))

        run('rm /tmp/{}'.format(archive_name))

        run('rm /data/web_static/current')

        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_base))

        return True
    except Exception:
        return False


def deploy():
    # deploys an archive to your web servers
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)"""

def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)