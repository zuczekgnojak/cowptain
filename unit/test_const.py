import unittest

from cowptain import Method, Status


class TestStatus(unittest.TestCase):
    def test_str(self):
        status = Status.Ok
        self.assertEqual(str(status), "200 OK")

    def test_both_variants_equal(self):
        status_a = Status.NOT_FOUND_404
        status_b = Status.NotFound
        self.assertEqual(status_a, status_b)


class TestMethod(unittest.TestCase):
    def test_str(self):
        method = Method.get
        self.assertEqual(str(method), "GET")
