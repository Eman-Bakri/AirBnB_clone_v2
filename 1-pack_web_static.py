#!/usr/bin/python3
# Fabfile Script generating .tgz archive using do_pack function.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create .tgz archive of web_static."""
    dt = datetime.utcnow()
    arch = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(arch)).failed is True:
        return None
    return arch
