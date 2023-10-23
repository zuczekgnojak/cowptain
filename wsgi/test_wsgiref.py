import subprocess
import unittest
from time import sleep

from wsgi.tests import Mixin


class TestWsgiRef(Mixin, unittest.TestCase):
    PORT = 8001
    COMMAND = ["/usr/local/bin/python", "wsgi/app.py"]
    gunicorn = "/usr/local/bin/gunicorn --bind '127.0.0.1:8002' wsgi.app:app"
    BASE_URL = "http://127.0.0.1"

    @classmethod
    def setUpClass(cls):
        cls.server = subprocess.Popen(
            cls.COMMAND,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.server.terminate()
        print()
        print("SERVER LOGS")
        print(cls.server.stdout.read().decode("utf8"))
