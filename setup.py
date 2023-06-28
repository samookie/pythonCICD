from setuptools import setup, find_packages

setup(
    name='mon-application',
    version='1.0.0',
    author='Votre nom',
    author_email='votre@email.com',
    description='Description de votre application',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'requests==2.26.0'
    ],
)
