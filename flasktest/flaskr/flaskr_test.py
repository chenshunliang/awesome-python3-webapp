import os
import flaskr
import unittest
import tempfile


# 单元测试
class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkdtemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])


if __name__ == '__main__':
    unittest.main()
