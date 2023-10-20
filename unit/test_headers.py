import unittest

from cowptain import Cookies, Headers


class TestHeaders(unittest.TestCase):
    def test_init(self):
        h = Headers({})
        self.assertEqual(len(h), 0)

    def test_simple(self):
        h = Headers(
            {
                "Some": "Value",
            }
        )

        self.assertEqual(h["Some"], "Value")

    def test_multiple(self):
        h = Headers(
            {
                "Some": "Value",
                "CAPITALIZED": "foo",
                "smoll": "bar",
                "under_SCORED": "baz",
                "http_prefix1": "prefix1",
                "HTTP_pReFiX2": "prefix2",
                "HYP-HEN": "hyphen",
            }
        )

        expected = {
            "Some": "Value",
            "Capitalized": "foo",
            "Smoll": "bar",
            "Under-Scored": "baz",
            "Prefix1": "prefix1",
            "Prefix2": "prefix2",
            "Hyp-Hen": "hyphen",
        }
        for key, value in expected.items():
            self.assertEqual(h[key], value)


class TestCookies(unittest.TestCase):
    def test_init(self):
        c = Cookies("")
        self.assertEqual(len(c), 0)

    def test_simple(self):
        c = Cookies("cookie=value")
        self.assertEqual(c["cookie"], "value")

    def test_multiple(self):
        c = Cookies("cookie=value;other=foo;another=bar")
        self.assertEqual(c["cookie"], "value")
        self.assertEqual(c["other"], "foo")
        self.assertEqual(c["another"], "bar")
