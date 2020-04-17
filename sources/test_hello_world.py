# test_hello.py
from sources.hello import app
import unittest


class TestHelloWorld(unittest.TestCase):

  def test_hello(slef):
      response = app.test_client().get('/')

      assert response.status_code == 200
      assert response.data == b'Hello, World!'

  def test_greet(self):
      response = app.test_client().get('/greet')

      assert response.status_code == 200
      assert response.data == b'greetings'


if __name__ == '__main__':
    unittest.main()