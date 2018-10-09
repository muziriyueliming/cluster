import os
import requests
import sys

def check_version(remote_ver, local_ver):
    '用于判断服务器上是否有新版本的软件，有返回True，否则返回False'
    if not os.path.exists(local_ver):
        return True  # 如果本地版本文件不存在则返回True

    r = requests.get(remote_ver)
    with open(local_ver) as fobj:
        version = fobj.read()

    if version != r.text:
        return True

    return False

def check_md5(fname):


def download(url, dst_name):


def deploy():


if __name__ == '__main__':
    remote_ver = 'http://192.168.4.3/deploy/live_version'
    local_ver = '/var/www/packages/live_verion'
    new_ver = check_version(remote_ver, local_ver)
    if not new_ver:
        sys.exit(0)
