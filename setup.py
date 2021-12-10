from setuptools import setup

setup(
    name='m3-project',
    version='1.0.0',
    packages=['m3_project', 'm3_project.m3_project', 'm3_project.app', 'm3_project.app.migrations'],
    url='',
    license='',
    author='vladislav',
    author_email='',
    description='',
    install_requires=[
            'django==2.2',
            'm3-django-compat==1.9.2',
            'm3-objectpack==2.2.47']
)
