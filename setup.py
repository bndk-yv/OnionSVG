#!/usr/bin/env python

from distutils.core import setup
import setuptools

setup(
    name = 'OnionSVG',
    version = '0.1',
    description = 'Peel your SVG files with Python',
    author = 'ybnd',
    author_email = 'ybnd@tuta.io',
    url = 'https://github.com/ybnd/OnionSVG',
    install_requires = ['lxml', 'cairosvg'],
)