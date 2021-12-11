from setuptools import setup

setup (
    name = 'WalkWoman',
    description = "A simple sprite",
    author = "Alberto Rivera",
    author_email= "alberto.rivera.garcia@gmail.com",
    version ="0.0.1",
    packages= ["WalkWoman"],
    entry_points = {"console_scripts": ["WalkWoman = WalkWoman.__main__:main"]},
    install_requires = ["pygame"]
)