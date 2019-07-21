from setuptools import setup

setup(
    zip_safe=True,
    name='mock_server',
    version='1.0',
    author='Salim',
    author_email='salimkabeer@gmail.com',
    packages=[
    ],
    license='free ware',
    description='Mock To Do List Server',
    install_requires=[
        'Flask==1.0.2'
    ]
)