#!/usr/bin/python3

""" Fabric script for deploying web_static """

from fabric.api import run, put, env, local, sudo
from fabric.contrib.files import exists
from os.path import exists
from datetime import datetime
import os

env.hosts = ['100.26.250.129', '54.210.53.36']
env.user = 'ubuntu'


def do_pack():
    """ generates a .tgz archive from the contents of the web_static folder """
    try:
        local("mkdir -p versions")
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(date_time)
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None


""" def do_deploy(archive_path):
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
"""


"""def do_deploy(archive_path):
    #distributes an archive to the web servers
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False"""

  
def do_deploy(archive_path):
    """ deploy an archive to your web servers """
    if not os.path.exists(archive_path):
        return False
    try:
        releases_path = "/data/web_static/releases/"
        file_name = os.path.basename(archive_path)
        file_name_no_ext = file_name.split(".")[0]
        current = "/data/web_static/current"

        put(archive_path, '/tmp/')
        # check if the path dosen't exist, it must be created
        if not exists(releases_path):
            sudo(f"mkdir -p {releases_path}")
            sudo(f"mkdir -p /data/web_static/shared/")
        sudo(f"tar -xzf /tmp/{file_name} -C {releases_path} && sudo mv \
            {releases_path}web_static {releases_path}{file_name_no_ext}")
        run(f"rm '/tmp/{file_name}'")

        # checks if "current" exists on the server before attempting to delete
        if exists(current):
            sudo(f"rm {current}")
        else:
            pass
        sudo(f"ln -s {releases_path}{file_name_no_ext} {current}")
        print("New version deployed!")
        return True
    except Exception:
        return False
