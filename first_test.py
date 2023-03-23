import json
import jsonpath
import requests
import pytest


def test_get_assertion():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/'
    response = requests.get(base_url + endpoint)
    assert response.status_code == 200, 'Status code not match'


def test_create_authors():
    request_json = dict(id=100, idBook=100, firstName='string100', lastName='string100')
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors'
    response = requests.post(base_url + endpoint, json=request_json)
    assert response.status_code == 200, 'Status code not match'


def test_get_single_author():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors' + '1'
    response = requests.get(base_url, endpoint)
    assert response.status_code == 200, 'Status code not match'


def test_update_author_info():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/' + '1'
    request_json = dict(id=0, idBook=0, firstName='string', lastName='string')
    response = requests.put(base_url + endpoint, json=request_json)

    assert response.status_code == 200


def test_delete_single_author():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/' + '1'
    response = requests.delete(base_url + endpoint)
    assert response.status_code == 200, 'Status code not match'
