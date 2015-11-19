import sys

from .downloader import cartretrieve


def main():
    if len(sys.argv) < 2:
        print('need a cart-id as argument! (for example, 10022 gets you Hug Arena)')
        exit(1)

    cart_id = sys.argv[1]
    path, httpmsg = cartretrieve(cart_id)
    print('ok, saved to {}'.format(path))


if __name__ == '__main__':
    main()
