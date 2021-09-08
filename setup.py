from setuptools import setup

setup(
    name='virtual_coach_db',
    version='0.1',
    author='Robin Richardson, Sven van den Burg, Bouke Scheltinga, Nele Albers',
    install_requires=open("requirements.txt", "r").readlines(),
    long_description=open("README.md", "r").read(),
    long_description_content_type='text/markdown',
    packages=['helper', 'dbschema'],
    include_package_data=True,
    description="Hello World testing setuptools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
)
