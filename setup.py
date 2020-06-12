from setuptools import setup, find_packages

setup(
    name='ftlr',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        "xmltodict",
    ],
    url='',
    license='MIT',
    author='Harry Djachenko',
    author_email='i.s.djachenko@gmail.com',
    description='',
    entry_points={
        "console_scripts": [
            "ftlr = ftlr.runner:run",
        ]
    }
)
