import os
from App import App
import unittest


class AppTestCase(unittest.TestCase):

    def setUp(self):
        App.app.testing = True
        self.client = App.app.test_client()
        with App.app.app_context():
            App.init()

    def tearDown(self):
        App.close()

#unit tests

    def test_ID_001(self):
        rv = self.client.get('/')
        assert b'test works' in rv.data

    def test_ID_002(self):
        rv = self.client.get('/api/')
        assert b'in api' in rv.data

    def test_ID_003(self):
        rv = self.client.get('/api/sys/tg_test/1/')
        self.assertEqual('sys/tg_test/1',rv.data,'expected sys/tg_test/1, instead got '+rv.data)

    def test_ID_004(self):
        rv = self.client.post('/api/sys/tg_test/1/', json={'cmd_name': 'SwitchStates', "cmd_param": 'None'})
        self.assertEqual(rv.status_code, 200,rv.data)



if __name__ == '__main__':
    unittest.main()