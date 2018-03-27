from setuptools import setup, find_packages

setup(
    name="django-fe-jwt",
    version="0.0.1",
    url='https://github.com/fernandoe/django-fe-jwt',
    author="Fernando Espíndola",
    author_email="fer.esp@gmail.com",
    packages=find_packages(),
    install_requires=[
        'django-fe-core==0.3.0',
        'djangorestframework-jwt>=1.11.0'
    ]
)
