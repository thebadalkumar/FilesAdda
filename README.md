# FilesAdda

## Setup

**PYTHON MUST BE INSTALLED ON MACHINE TO RUN THIS PROJECT**

Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/) and add it's path to Environment Variables ([Windows](https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows)).

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/thebadalkumar/FilesAdda.git
$ cd FilesAdda
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
```
Activate it on Windows

```sh
$ env/Scripts/activate
```
Activate it on Linux/ Mac OS

```sh
$ source env/bin/activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:

Migrate the database

```sh
(env)$ python manage.py migrate
```
and lastly run the server
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Hurray!!!