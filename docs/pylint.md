##

First, you need to have Pylint and Pylint-django installed.

```
pip install pylint
pip install pylint-django
```

You can check if you have pylint installed with:

```
pylint --version
```

## Running pylint

Run the following command in the top project directory:

```
pylint --load-plugins=pylint_django <path to folder or file>
```

For example to run pylint over the whole project:

```
pylint --load-plugins=pylint_django app
```

## Configuring pylint

Pylint is configured by .pylintrc in the top level directory. If you want to completely disable a message, add the message number to the
```
disable=
    C0114, C0116, C0115
```
at the top of the file.

If you want to disable a particular instance of a warning, add the comment 
```
# pylint:disable=<message number>
```
to the end of the offending line.