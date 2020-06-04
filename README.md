# pytest-err

Error reporting plugin for pytest

## What and Why

When swapping out external dependencies (going from python2 to 3, swapping out lxml to xml) or similair actions where many points are affected tools for identifying common errors are nice to have. This plugin for pytest aims to provide you with relevant information telling you for example that your 100 errors are actually four errors where one of them stands for 70 of the 100 cases.

It was developed as a script during a 2to3 conversion on a tool working with binary data. It has since been ported to be a plugin to pytest.

## Developing

### General development

Per usual set up your python virtual environment first.

Install pre-commit
```bash
pip install pre-commit
pre-commit install
```
Now every time you commit it will run the pre-commit checks

To test the suite run:
```bash
pip install nox
nox
```
This will run the sessions defined in [noxfile.py](noxfile.py)

### Tests

passta

## License
See [LICENSE](LICENSE)
