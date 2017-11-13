"""Setup script for extension."""

from setuptools import setup


setup(
    name='grow-ext-html-min',
    version='1.0.0',
    license='MIT',
    author='Grow Authors',
    author_email='hello@grow.io',
    include_package_data=False,
    packages=[
        'html_min',
    ],
    install_requires=[
        'htmlmin==0.1.11',
    ],
)
