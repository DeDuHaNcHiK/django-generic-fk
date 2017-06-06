import codecs
import os

from setuptools import setup, find_packages


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = __import__("generic_fk").__version__

setup(
    name='generic-fk',
    version=VERSION,

    author='Tierzov Andrii',
    author_email='avtierzov@gmail.com',

    url='https://bitbucket.org/avtierzov/django-generic-fk',
    description='Django application for GenericForeignKey',
    long_description=read("README.rst"),

    packages=find_packages(exclude=['example_project', 'example_project.*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django ~= 1.11'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Django',
    ]
)
