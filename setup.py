from setuptools import setup

setup(
    name = "todo-flask",
    version = "0.0.1",
    author = "Wayne Werner",
    author_email = "waynejwerner@gmail.com",
    description = "A sample todo app written with Flask, unittest, and sqlite",
    license = "BSD",
    keywords = "example flask unittest",
    url = "https://github.com/waynew/todo-flask",
    packages=['todo'],
    scripts=['scripts/start_todo'],
    install_requires=['flask'],
    tests_require=['coverage'],
    test_suite="tests",
    long_description="A sample todo app written with Flask, unittest, and sqlite",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
