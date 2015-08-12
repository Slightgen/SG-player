#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup

setup(
    name='SG-player',
    version='1.0.0',
    url='https://github.com/Slightgen/SG-player',
    author='girish joshi',
    author_email='girish946@gmail.com',
    description=('GUI for omxplayer using PyQt4'),
    license='GPLV3',
    packages=[],
    test_suite='',
    install_requires=['pyautogui'],
    keywords="Omxplayer GUI raspberry-pi PyQt4 ",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    scripts=['sg-player']
)
