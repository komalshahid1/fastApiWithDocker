from setuptools import setup, find_packages

setup(
    name='python_helpers',
    version='0.1',
    packages=find_packages(),  # This line ensures it includes the `python_helpers/` folder
    install_requires=[
         'wtforms'
    ],
)
