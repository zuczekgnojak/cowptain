import unittest

from cowptain import Path, Query, Vars


class TestPath(unittest.TestCase):
    def test_init(self):
        p = Path("")
        self.assertEqual(len(p), 0)

    def test_single_element(self):
        p = Path("/sth")
        self.assertEqual(len(p), 1)

    def test_multiple_elements(self):
        p = Path("/sth/other/foo/bar")
        self.assertEqual(len(p), 4)

    def test_equals(self):
        p1 = Path("some/path/to/resource")
        p2 = Path("some/path/to/resource/")
        p3 = Path("/some/path/to/resource")

        self.assertEqual(p1, p2)
        self.assertEqual(p1, p3)

    def test_startswith(self):
        p1 = Path("<value>/path")
        p2 = Path("/<value>/path/")
        p3 = Path("/path/<value>")

        self.assertTrue(p1.startswith("<"))
        self.assertTrue(p2.startswith("<"))
        self.assertFalse(p3.startswith("<"))

    def test_indexing(self):
        p = Path("/some/path/somewhere/")
        p0 = Path("some")
        p1 = Path("path")
        p2 = Path("/somewhere")

        self.assertEqual(p[0], p0)
        self.assertEqual(p[1], p1)
        self.assertEqual(p[2], p2)


class TestVars(unittest.TestCase):
    def test_init(self):
        v = Vars(Path(""), Path(""))
        self.assertEqual(len(v), 0)

    def test_no_vars(self):
        path = Path("/some/path")
        pattern = Path("/some/path")
        v = Vars(path, pattern)
        self.assertEqual(len(v), 0)

    def test_single(self):
        path = Path("/some/value")
        pattern = Path("/some/<key>")
        v = Vars(path, pattern)
        self.assertEqual(v["key"], "value")

    def test_single_middle(self):
        path = Path("/first/foo/second")
        pattern = Path("/first/<bar>/second")
        v = Vars(path, pattern)
        self.assertEqual(v["bar"], "foo")

    def test_multiple(self):
        path = Path("/val1/p1/val2/val3")
        pattern = Path("/<key1>/p1/<key2>/<key3>")
        v = Vars(path, pattern)
        expected = {
            "key1": "val1",
            "key2": "val2",
            "key3": "val3",
        }
        for key, value in expected.items():
            self.assertEqual(v[key], value)


class TestQuery(unittest.TestCase):
    def test_init(self):
        q = Query("")
        self.assertEqual(len(q), 0)

    def test_simple(self):
        q = Query("some=value")
        self.assertEqual(q["some"], "value")

    def test_multiple(self):
        q = Query("some=value&foo=bar&baz&gaz=")

        expected = {
            "some": "value",
            "foo": "bar",
            "baz": "",
            "gaz": "",
        }

        for key, value in expected.items():
            self.assertEqual(q[key], value)
