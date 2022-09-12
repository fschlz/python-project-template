# Python Project Template

- I recommend you use `pyenv` to manage your Python versions
- Run `pyenv install 3.10.6` to install your favorite Python version
- Set and activate it `pyenv global 3.10.6 && pyenv shell 3.10.6`
- `pip install --upgrade pip`
- `pip install cookiecutter`
- `cookiecutter https://github.com/fschlz/python-project-template --checkout master`
- Follow the instructions in the prompt
- If you do not have `poetry` installed, I recommend you use it to manage your project dependencies over conda, pipenv, or pip
- Run `poetry install` to setup a virtualenv
- `poetry shell` activates it, later your IDE should detect this on its own
- `poetry add {pkg}` installs the given package
