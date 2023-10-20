import subprocess
from time import sleep
import unittest
import subprocess

import requests
from time import sleep


class Mixin:
    def url(self, endpoint):
        return f"http://127.0.0.1:{self.PORT}{endpoint}"

    def check(self, response):
        self.assertEqual(response.status_code, 200)

    def test_init(self):
        self.assertTrue(True)
    
    def test_ok(self):
        r = requests.get(self.url("/"))
        self.check(r)

    def test_method(self):
        r = requests.patch(self.url("/test-method"))
        self.check(r)

    def test_headers(self):
        headers = {
            "X_HEADER_A": "valueA",
            "other": "valueB",
        }
        r = requests.get(self.url("/test-headers"), headers=headers)
        self.check(r)
    
    def test_cookies(self):
        cookies = {
            "cookie1": "val1",
            "cookie2": "val2",
        }
        r = requests.get(self.url("/test-cookies"), cookies=cookies)
        self.check(r)

    def test_path(self):
        r = requests.get(self.url("/test-path/super/duper/long"))
        self.check(r)

    def test_vars(self):
        r = requests.get(self.url("/test-vars/val1/bar/val2"))
        self.check(r)
    
    def test_query(self):
        r = requests.get(self.url("/test-query?foo=bar&baz=gaz&other=&another"))
        self.check(r)
    
    def test_input(self):
        r = requests.post(self.url("/test-input"), data="thisIsPayload")
        self.check(r)

    def test_all(self):
        r = requests.put(
            self.url(
                "/test-all/someval/value/bar/foo"
                "?company=acme&name=tom&isAdmin"
            ),
            headers={
                "X-Token": "tokentoken",
                "X-Super-Secret": "********",
            },
            cookies={
                "chocolate": "yum",
            },
            data="this Is SoMe DAATA",
        )
