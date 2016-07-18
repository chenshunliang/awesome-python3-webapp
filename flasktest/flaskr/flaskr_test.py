import os
import flaskr
import unittest
import tempfile


# 单元测试
class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        # self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkdtemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        # flaskr.init_db()

    def tearDown(self):
        pass

    # os.close(self.db_fd)
    # os.unlink(flaskr.app.config['DATABASE'])

    def test_add_data(self):
        rv = self.app.post('http://127.0.0.1:5000/add', data=dict(title='abc', text='cececece'), follow_redirects=True)
        assert rv._status_code == 200


if __name__ == '__main__':
    unittest.main()
