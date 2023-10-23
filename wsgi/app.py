from logging import getLogger

from cowptain import (
    Application,
    Headers,
    Method,
    Path,
    Request,
    Response,
    Status,
    View,
)

logger = getLogger(__name__)


class TestException(Exception):
    pass


class TestFailed(Response):
    def __init__(self):
        super().__init__(Headers({}), Status.BadRequest, [])


class TestPassed(Response):
    def __init__(self):
        super().__init__(Headers({}), Status.Ok, [])


class TestView(View):
    def __call__(self, request: Request) -> Response:
        try:
            self.test(request)
            return TestPassed()
        except AssertionError:
            logger.exception("test failed")
            return TestFailed()

    def test(self, request):
        pass


class OkView(TestView):
    def test(self, request):
        assert True


class TestMethod(TestView):
    def test(self, request):
        assert request.method == Method.patch


class TestHeaders(TestView):
    def test(self, request):
        assert request.headers["X-Header-A"] == "valueA"
        assert request.headers["Other"] == "valueB"


class TestCookies(TestView):
    def test(self, request):
        assert request.cookies["cookie1"] == "val1"
        assert request.cookies["cookie2"] == "val2"


class TestPath(TestView):
    def test(self, request):
        expected_path = Path("/test-path/super/duper/long")
        assert request.path == expected_path
        assert len(request.path) == 4


class TestVars(TestView):
    def test(self, request):
        assert request.vars["foo"] == "val1"
        assert request.vars["baz"] == "val2"


class TestQuery(TestView):
    def test(self, request):
        assert request.query["foo"] == "bar"
        assert request.query["baz"] == "gaz"
        assert request.query["other"] == ""
        assert request.query["another"] == ""


class TestInput(TestView):
    def test(self, request):
        body = request.input.read()
        assert body == b"thisIsPayload"


class TestAll(TestView):
    def test(self, request):
        # method
        assert request.method == Method.put
        # headers
        headers = request.headers
        assert headers["X-Token"] == "tokentoken"
        assert headers["X-Super-Secret"] == "********"
        # cookies
        assert request.cookies["chocolate"] == "yum"
        # path
        expected = Path("/test-all/someval/value/bar/foo")
        assert request.path == expected
        assert len(request.path) == 5
        # vars
        vars = request.vars
        assert vars["some"] == "someval"
        assert vars["foo"] == "bar"
        assert vars["bar"] == "foo"
        # query
        query = request.query
        assert query["company"] == "acme"
        assert query["name"] == "tom"
        assert query["isAdmin"] == ""
        # input
        body = request.input.read()
        assert body == b"this Is SoMe DAATA"


app = Application()
app.add_route("/", OkView)
app.add_route("/test-method", TestMethod)
app.add_route("/test-headers", TestHeaders)
app.add_route("/test-cookies", TestCookies)
app.add_route("/test-path/super/duper/long", TestPath)
app.add_route("/test-vars/<foo>/bar/<baz>", TestVars)
app.add_route("/test-query", TestQuery)
app.add_route("/test-input", TestInput)
app.add_route("/test-all/<some>/value/<foo>/<bar>", TestAll)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    with make_server("127.0.0.1", 8001, app) as server:
        server.serve_forever()
