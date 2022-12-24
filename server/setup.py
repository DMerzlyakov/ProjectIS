from setuptools import setup

setup(
    name='Project IS',
    version='0.0.1',
    author='Team 2',
    author_email='d.merzlyakov',
    description='FastApi app',
    install_requires=[
        'fastapi==0.70.0',
        'uvicorn==0.15.0',
        'SQLAlchemy==1.4.26',
        'pytest==6.2.5',
        'requests==2.26.0',
    ],
    scripts=[
        'server.py'
    ]
)
