from setuptools import setup, find_packages

setup(
    name = 'django-generic-foreign-key',
    version = '0.0.1',
    author = 'Tierzov Andrii',
    author_email = 'avtierzov@gmail.com',
    description = 'Django application for GenericForeignKey',
    url = 'https://bitbucket.org/avtierzov/django-generic-fk',
    packages = find_packages(exclude=['example_project', 'example_project.*']),
    include_package_data = True,
    zip_safe = False,
    install_requires = ['Django'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)