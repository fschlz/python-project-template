import os
import pathlib
import sys

MODULE_DIR = os.path.abspath(pathlib.Path("./src"))
sys.path.append(MODULE_DIR)
os.chdir(MODULE_DIR)

import logging

import pytest
import yaml
import dotenv

logger = logging.getLogger(__name__)

logger.info(os.getcwd())


@pytest.fixture
def test_param_dict():
    test_param_dict = yaml.load(open(pathlib.Path("../tests/test_params.yml"), "r"), yaml.FullLoader)
    return test_param_dict


@pytest.fixture
def secrets():
    return dotenv.dotenv_values(dotenv_path="/configs/.env")


@pytest.fixture
def current_version():
    with open(pathlib.Path("./VERSION")) as f:
        v = f.read()
    return v
