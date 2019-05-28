# coding=utf-8

# third part modules
'''
browse and install them on https://pypi.org/
'''

'''
how to install? module name is case insensitive
>>> pip install <module_name>

try this:
pip install pillow
'''

# PIL
print('\n# PIL')
from os import path
from PIL import Image

img = Image.open(path.join(path.dirname(__file__), '../../assets/images/coolconan.png'))
print('format: %s' % img.format)
print('width: %spx, height: %spx' % (img.size[0], img.size[1]))
print('color mode: %s' % img.mode)


# sys.path
print('\n# sys.path')
import sys
print(sys.path)