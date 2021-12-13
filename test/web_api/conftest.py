import pytest
import os
import requests


@pytest.fixture(scope="session")
def base_url():
    return 'https://master.apis.dev.openstreetmap.org'


@pytest.fixture()
def username():
    return os.environ['USERNAME']


@pytest.fixture()
def password():
    return os.environ['PASSWORD']


@pytest.fixture()
def create_changeset(base_url, username, password):
    xml_file = './test_data/web_api/create_changeset_200_ok.xml'
    with open(xml_file, mode='rb') as xml:
        response = requests.put(f'{base_url}/api/0.6/changeset/create', data=xml, auth=(username, password))
    return response
