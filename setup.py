from setuptools import setup, find_packages

setup(
    name='demommath',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'your-command-name=your_package.module1:main_function',
        ],
    },
    author='Gangesh',
    author_email='gvelip@nio.org',
    description='This package is for testing And How to create a package',

)

