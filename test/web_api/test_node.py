import os

import requests
import pytest
import xml.etree.ElementTree as ET


@pytest.fixture()
def create_node(create_changeset, base_url, username, password):
    response = create_changeset
    assert response.status_code == 200
    changeset_id = response.text
    xml_file = './test_data/web_api/create_node_200_ok.xml'
    tree = ET.parse(xml_file)
    tree.getroot().find('node').set('changeset', changeset_id)
    tree.write(xml_file)
    with open(xml_file, mode='rb') as xml:
        yield requests.put(f'{base_url}/api/0.6/node/create', data=xml, auth=(username, password))
    tree.getroot().find('node').set('changeset', '')
    tree.write(xml_file)


class TestCreateNode:

    def test_should_create_node(self, create_node, base_url, username, password):
        response = create_node
        node_id = response.text
        assert response.status_code == 200
        response = requests.get(f'{base_url}/api/0.6/node/{node_id}', auth=(username, password))
        tag = ET.fromstring(response.text).find('node').find('tag')
        assert tag.get('v') == 'Just a node'

    def test_should_not_create_node_without_auth(self, create_changeset, base_url):
        response = create_changeset
        assert response.status_code == 200
        changeset_id = response.text
        xml_file = './test_data/web_api/create_node_200_ok.xml'
        tree = ET.parse(xml_file)
        tree.getroot().find('node').set('changeset', changeset_id)
        tree.write(xml_file)
        with open(xml_file, mode='rb') as xml:
            response = requests.put(f'{base_url}/api/0.6/node/create', data=xml)
        tree.getroot().find('node').set('changeset', '')
        tree.write(xml_file)
        assert response.status_code == 401

    def test_should_not_create_node_with_closed_changeset(self, base_url, username, password):
        xml_file = './test_data/web_api/create_node_200_ok.xml'
        tree = ET.parse(xml_file)
        tree.getroot().find('node').set('changeset', '1')
        tree.write(xml_file)
        with open(xml_file, mode='rb') as xml:
            response = requests.put(f'{base_url}/api/0.6/node/create', data=xml, auth=(username, password))
        assert response.status_code == 409
        tree.getroot().find('node').set('changeset', '')
        tree.write(xml_file)


class TestModifyNode:

    def test_should_modify_node(self, create_node, base_url, username, password):
        response = create_node
        node_id = response.text
        assert response.status_code == 200
        response = requests.get(f'{base_url}/api/0.6/node/{node_id}', auth=(username, password))
        root = ET.fromstring(response.text)
        root.find('node').find('tag').set('v', 'Just a modified node')
        tree = ET.ElementTree(root)
        tree.write('temp.xml')
        with open('temp.xml', mode='rb') as xml:
            response = requests.put(f'{base_url}/api/0.6/node/{node_id}', data=xml, auth=(username, password))
        assert response.status_code == 200
        os.remove('temp.xml')

    def test_should_not_modify_node_without_auth(self, create_node, base_url, username, password):
        response = create_node
        node_id = response.text
        assert response.status_code == 200
        response = requests.get(f'{base_url}/api/0.6/node/{node_id}', auth=(username, password))
        root = ET.fromstring(response.text)
        root.find('node').find('tag').set('v', 'Just a modified node')
        tree = ET.ElementTree(root)
        tree.write('temp.xml')
        with open('temp.xml', mode='rb') as xml:
            response = requests.put(f'{base_url}/api/0.6/node/{node_id}', data=xml)
        assert response.status_code == 401
        os.remove('temp.xml')

    def test_should_not_modify_node_with_wrong_version(self, create_node, base_url, username, password):
        response = create_node
        node_id = response.text
        assert response.status_code == 200
        response = requests.get(f'{base_url}/api/0.6/node/{node_id}', auth=(username, password))
        root = ET.fromstring(response.text)
        root.find('node').find('tag').set('v', 'Just a modified node')
        root.find('node').set('version', '5')
        tree = ET.ElementTree(root)
        tree.write('temp.xml')
        with open('temp.xml', mode='rb') as xml:
            response = requests.put(f'{base_url}/api/0.6/node/{node_id}', data=xml, auth=(username, password))
        assert response.status_code == 409
        os.remove('temp.xml')


class TestDeleteNode:

    def test_should_delete_node(self, create_node, base_url, username, password):
        response = create_node
        node_id = response.text
        assert response.status_code == 200
        response = requests.get(f'{base_url}/api/0.6/node/{node_id}', auth=(username, password))
        root = ET.fromstring(response.text)
        tree = ET.ElementTree(root)
        tree.write('temp.xml')
        with open('temp.xml', mode='rb') as xml:
            response = requests.delete(f'{base_url}/api/0.6/node/{node_id}', data=xml, auth=(username, password))
        assert response.status_code == 200
        os.remove('temp.xml')

    def test_should_not_delete_node_when_not_owner(self, base_url, username, password):
        xml_file = './test_data/web_api/delete_node.xml'
        with open(xml_file, mode='rb') as xml:
            response = requests.delete(f'{base_url}/api/0.6/node/1', data=xml, auth=(username, password))
        assert response.status_code == 409

    def test_should_not_delete_node_when_already_deleted(self, create_node, base_url, username, password):
        response = create_node
        node_id = response.text
        assert response.status_code == 200
        response = requests.get(f'{base_url}/api/0.6/node/{node_id}', auth=(username, password))
        root = ET.fromstring(response.text)
        tree = ET.ElementTree(root)
        tree.write('temp.xml')
        with open('temp.xml', mode='rb') as xml:
            requests.delete(f'{base_url}/api/0.6/node/{node_id}', data=xml, auth=(username, password))
            response = requests.delete(f'{base_url}/api/0.6/node/{node_id}', data=xml, auth=(username, password))
        assert response.status_code == 410
        os.remove('temp.xml')
