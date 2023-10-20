import subprocess
from time import sleep
import unittest
import subprocess

import requests
from time import sleep
from wsgi.tests import Mixin


class TestUwsgi(Mixin, unittest.TestCase):
    PORT = 8003
    BASE_URL = "http://127.0.0.1"

    @classmethod
    def setUpClass(cls):
        cls.server = subprocess.Popen(
            [
                "/usr/local/bin/uwsgi",
                "--http", "127.0.0.1:8003", "--wsgi-file", "wsgi/app.py", "--callable", "app",
            ],
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
