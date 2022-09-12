# Python Project Template

- I recommend you use `pyenv` to manage your Python versions
- Run `pyenv install 3.10.6` to install your favorite Python version
- Set and activate it `pyenv global 3.10.6 && pyenv shell 3.10.6`
- `pip install --upgrade pip`
- `pip install cookiecutter` or use your package manager (i.e. `brew install cookiecutter`)
- `cookiecutter https://github.com/fschlz/python-project-template.git --checkout master`
- Follow the instructions in the prompt
- `cd {project_name}`

If you do not have `poetry` installed, I recommend you use it to manage your project dependencies over conda, pipenv, or pip -> [link](https://python-poetry.org/)
- Run `poetry config virtualenvs.in-project true` to get a `.venv` in your project folder after running `poetry install` (easier to deal with than having it hidden somewhere on your system)
- `poetry shell` activates it, later your IDE should detect this on its own
- `poetry add {pkg}` installs any given package
