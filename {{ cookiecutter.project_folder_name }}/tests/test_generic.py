from {{ cookiecutter.package_name }} import __version__


def test_version(current_version):
    assert __version__ == current_version
