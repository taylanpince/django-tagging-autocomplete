# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

packages = find_packages()
long_description = open('README.txt').read()
template_patterns = [
    'templates/*.html',
    'templates/*/*.html',
]

setup(
    name='django-tagging-autocomplete',
    version='0.3.1',
    description='Autocompletion for django-tagging',
    long_description=long_description,
    author='Ludwik Trammer',
    author_email='ludwik@gmail.com',
    url='http://code.google.com/p/django-tagging-autocomplete/',
    packages=packages,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    package_data=dict((package, template_patterns) for package in packages),
) 
