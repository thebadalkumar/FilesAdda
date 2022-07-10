# FilesAdda

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/thebadalkumar/FilesAdda.git
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
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Hurray!!!