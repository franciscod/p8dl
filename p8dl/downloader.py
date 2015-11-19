import urllib.request

import appdirs
import platform
import os.path


def cart_url(cart_id):
    return 'http://www.lexaloffle.com/bbs/cposts/{}/{}.p8.png'.format(
        cart_id[0],
        cart_id
    )


def pico8_path():
    if platform.system() == 'Linux':
        return os.path.expanduser("~/.lexaloffle/pico-8")

    return appdirs.user_data_dir('pico-8', False, roaming=True)


def pico8_config_var(key):
    with open(os.path.join(pico8_path(), 'config.txt')) as f:
        for line in f.readlines():
            if line.startswith(key):
                return line.strip()[len(key)+1:]


def cart_path(cart_id):
    return os.path.join(
        pico8_config_var('root_path'),
        '{}.p8.png'.format(cart_id),
    )


def cartretrieve(cart_id):
    url, path = cart_url(cart_id), cart_path(cart_id)
    return urllib.request.urlretrieve(url, path)
