from setuptools import setup

setup(
    zip_safe=True,
    name='todolist_mock_server',
    version='1.0',
    author='Aqua Security',
    author_email='automation.qa@aquasec.com',
    packages=[
    ],
    license='Aqua Security',
    description='Mock To Do List Server',
    install_requires=[
        'Flask==1.0.2'
    ]
)