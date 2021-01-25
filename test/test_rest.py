import unittest
from src.main import app
from src.utils import read_file
import json


class BasicTestCase(unittest.TestCase):

	def assert_dataset(self, dataset_resp):
		self.assertEqual(dataset_resp['name'], 'clients')
		self.assertEqual(dataset_resp['type'], 'dataset')
		self.assertEqual(dataset_resp['title'], 'Clients')
		self.assertEqual(dataset_resp['ref']['type'], 'dwh')
		self.assertEqual(dataset_resp['ref']['subtype'], 'basic')
		self.assertEqual(dataset_resp['ref']['primaryKey'], 'client_id')
		self.assertTrue(dataset_resp['ref']['categorizable'])
		self.assertEqual(len(dataset_resp['ref']['properties']), 3)
		self.assertFalse(dataset_resp['ref']['properties'][0]['filterable'])
		self.assertEqual(dataset_resp['ref']['properties'][0]['name'], 'client_id')
		self.assertEqual(dataset_resp['ref']['properties'][0]['title'], 'Client ID')
		self.assertEqual(dataset_resp['ref']['properties'][0]['column'], 'client_id')
		self.assertEqual(dataset_resp['ref']['properties'][0]['type'], 'integer')

	def assert_pagination(self, page_resp):
		self.assertEqual(page_resp['page']['size'], 5)
		self.assertEqual(page_resp['page']['totalElements'], 1)
		self.assertEqual(page_resp['page']['totalPages'], 1)
		self.assertEqual(page_resp['page']['number'], 1)
		self.assertEqual(len(page_resp['links']), 1)
		self.assertEqual(page_resp['links'][0]['rel'], 'self')
		self.assertEqual(page_resp['links'][0]['href'], '/datasets?page=1&size=5')

	def test_rest(self):
		test_client = app.test_client(self)
		dataset = read_file('./test/json/clients.json')

		# POST /datasets
		post_response = test_client.post('/datasets', data=json.dumps(dataset), content_type='application/json')
		self.assertEqual(post_response.status_code, 200)
		dataset_resp = json.loads(post_response.data)
		dataset_id = dataset_resp.get('id')
		dataset_name = dataset_resp.get('name')
		self.assert_dataset(dataset_resp)

		# GET /datasets/<id>
		get_by_id_response = test_client.get('/datasets/' + dataset_id)
		self.assertEqual(get_by_id_response.status_code, 200)
		dataset_by_id_resp = json.loads(get_by_id_response.data)
		self.assert_dataset(dataset_by_id_resp)

		# GET /datasets?name=<name>
		get_by_name_response = test_client.get('/datasets?name=' + dataset_name)
		self.assertEqual(get_by_name_response.status_code, 200)
		dataset_by_id_resp = json.loads(get_by_name_response.data)
		self.assert_dataset(dataset_by_id_resp)

		# GET /datasets
		get_all_response = test_client.get('/datasets')
		self.assertEqual(get_all_response.status_code, 200)
		datasets_resp = json.loads(get_all_response.data)
		self.assert_dataset(datasets_resp['content'][0])
		self.assert_pagination(datasets_resp)

		# PUT /datasets/<id>
		dataset['name'] = 'customers'
		dataset['ref']['primaryKey'] = 'postcode'
		dataset['ref']['properties'][0]['title'] = 'Customer ID'
		put_response = test_client.put('/datasets/' + dataset_id, data=json.dumps(dataset), content_type='application/json')
		self.assertEqual(put_response.status_code, 200)
		dataset_put_resp = json.loads(put_response.data)
		self.assertEqual(dataset_put_resp['name'], 'customers')
		self.assertEqual(dataset_put_resp['ref']['primaryKey'], 'postcode')
		self.assertEqual(dataset_put_resp['ref']['properties'][0]['title'], 'Customer ID')

		# DELETE /datasets/<id>
		delete_response = test_client.delete('/datasets/' + dataset_id)
		self.assertEqual(delete_response.status_code, 204)


if __name__ == '__main__':
	unittest.main()
