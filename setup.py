#!/usr/bin/env python

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pagelebels-py',
    version='0.1.0',
    description='PDF file reader/writer library',
    long_description=read("README.rst"),
    author='Ophir Lojkine',
    author_email='pere.jobs@gmail.com',
    platforms='Independent',
    url='https://github.com/lovasoa/pagelabels-py',
    packages=['pagelabels'],
    install_requires=[
        'pdfrw',
    ],
    license='GNU General Public License v3.0',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Software Development :: Libraries',
        'Topic :: Text Processing',
        'Topic :: Printing',
        'Topic :: Utilities',
    ],
    keywords='PDF, page labels",
)