import sys, os 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from api import create_app
# from api.todo.model import TodoModel

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.headers = {'Authorization': f'{self.__get_test_token()}'}

    def __get_test_token(self):
        # 테스트용 토큰 발급 로직
        response = self.client.post('/users/signin', json={
            'email': 'test@gmail.com',
            'password': '1234'
        })
        return response.json['data']['token']

    def test_get_todo(self):
        print(f'##### {self.headers}')
        response = self.client.get('/todos/', 
            headers=self.headers
        )
        print(f'##### {response.data}')
        self.assertEqual(response.status_code, 200) 

    def test_get_todo_with_invaild_jwt(self):
        print(f'##### {self.headers}')
        response = self.client.get('/todos/', 
            headers={'Authorization': 'wrong jwt'}
        )
        print(f'##### {response.data}')
        self.assertEqual(response.status_code, 401) 