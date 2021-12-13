import requests
import xml.etree.ElementTree as ET


class TestCreateChangeset:

    def test_should_create_changeset(self, create_changeset, base_url):
        response = create_changeset
        assert response.status_code == 200
        changeset_id = response.text
        response = requests.get(f'{base_url}/api/0.6/changeset/{changeset_id}')
        tag = ET.fromstring(response.text).find('changeset').find('tag')
        assert tag.get('v') == 'Making a changeset test'

    def test_should_not_create_changeset_without_auth(self, base_url):
        xml_file = './test_data/web_api/create_changeset_200_ok.xml'
        with open(xml_file, mode='rb') as xml:
            response = requests.put(f'{base_url}/api/0.6/changeset/create', data=xml)
        assert response.status_code == 401

    def test_should_not_create_changeset_with_bad_xml(self, base_url, username, password):
        xml_file = './test_data/web_api/create_changeset_400_bad.xml'
        with open(xml_file, mode='rb') as xml:
            response = requests.put(f'{base_url}/api/0.6/changeset/create', data=xml, auth=(username, password))
        assert response.status_code == 400


class TestModifyChangeset:

    def test_should_modify_changeset(self, create_changeset, base_url, username, password):
        response = create_changeset
        assert response.status_code == 200
        changeset_id = response.text
        xml_file = './test_data/web_api/modify_changeset_200_ok.xml'
        with open(xml_file, mode='rb') as xml:
            response = requests.put(f'{base_url}/api/0.6/changeset/{changeset_id}', data=xml, auth=(username, password))
        assert response.status_code == 200
        tag = ET.fromstring(response.text).find('changeset').find('tag')
        assert tag.get('v') == 'This is a changed comment.'

    def test_should_not_modify_changeset_without_auth(self, create_changeset, base_url):
        response = create_changeset
        changeset_id = response.text
        xml_file = './test_data/web_api/modify_changeset_200_ok.xml'
        with open(xml_file, mode='rb') as xml:
            response = requests.put(f'{base_url}/api/0.6/changeset/{changeset_id}', data=xml)
        assert response.status_code == 401

    def test_should_not_modify_changeset_already_closed(self, create_changeset, base_url, username, password):
        response = create_changeset
        changeset_id = response.text
        requests.put(f'{base_url}/api/0.6/changeset/{changeset_id}/close', auth=(username, password))
        xml_file = './test_data/web_api/modify_changeset_200_ok.xml'
        with open(xml_file, mode='rb') as xml:
            response = requests.put(f'{base_url}/api/0.6/changeset/{changeset_id}', data=xml, auth=(username, password))
        assert response.status_code == 409
