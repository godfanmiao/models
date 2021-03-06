"""
Utils
"""

import six
import os


def print_arguments(args):
    """
    Print arguments
    """
    print('-----------  Configuration Arguments -----------')
    for arg, value in sorted(six.iteritems(vars(args))):
        print('%s: %s' % (arg, value))
    print('------------------------------------------------')


def mkdir(path):
    """
    Mkdir
    """
    if not os.path.isdir(path): 
        if os.path.split(path)[0]:
            mkdir(os.path.split(path)[0])
    else:
        return
    os.mkdir(path)


def pos_encoding_init():
    """
    Pos encoding init
    """
    pass


def scaled_dot_product_attention():
    """
    Scaleed dot product attention
    """
    pass
