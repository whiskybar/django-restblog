import os
from setuptools import setup, find_packages


try:
    f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(
    name='django-restblog',
    version='1.0',
    url="http://github.com/whiskybar/django-restblog",
    description='A simple blog engine for Django powered by reST.',
    long_description=long_description,
    author='Jiri Barton',
    author_email='jbar@hosting4u.cz',
    license='BSD',
    keywords='django libraries blog rest'.split(),
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
)

