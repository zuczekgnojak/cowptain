import subprocess
from time import sleep
import unittest
import subprocess

import requests
from time import sleep
from wsgi.tests import Mixin


class TestGunicorn(Mixin, unittest.TestCase):
    PORT = 8002
    BASE_URL = "http://127.0.0.1"

    @classmethod
    def setUpClass(cls):
        cls.server = subprocess.Popen(
            [
                "/usr/local/bin/gunicorn",
                "--bind", "127.0.0.1:8002", "wsgi.app:app",
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
