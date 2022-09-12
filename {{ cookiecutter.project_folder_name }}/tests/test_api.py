import requests

from {{ cookiecutter.package_name }} import database, utils


def test_api_results(test_param_dict):
    current_response = requests.request(
        method="POST",
        url=test_param_dict.get("url") + test_param_dict.get("endpoint"),
        headers=test_param_dict.get("header"),
        data=test_param_dict.get("request"),
        verify=False,
    )
    current_response = current_response.text.replace(" ", "")
    expected_response = test_param_dict.get("response").replace(" ", "")
    assert (current_response == expected_response) && (current_response.status_code == 200)
