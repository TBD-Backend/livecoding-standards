# Tools

## pycodestyle

Pycodestyle is a static code analysis tool used to check the code against some of the PEP8 style conventions.

```shell
pip install pycodestyle
pycodestyle --first bad_code.py
```

## McCabe

McCabe is a static code analysis tool used to check the code for methods and functions exceedingly complex.

The higher the number the more complex the code
5 is a good baseline
Anything above 5 is bad

```shell
pip install mccabe
mccabe --min 5 example.py
```

## flake8

flake8 combines pycodestyle, pyflakes and mccabe

```shell
pip install flake8
flake8 example.py
```
