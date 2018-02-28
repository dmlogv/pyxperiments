"""Basic HTTP Server with dynamic page generation"""

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer


class Content:
    """HTTP Content wrapper"""
    def __init__(self, template, mime):
        self._template = template
        self.content = self._template
        self.mime = mime
    
    def substitute(self, **kwargs):
        self.content = self._template.format(**kwargs)
        return self


class MyLittleJoomla(BaseHTTPRequestHandler):
    """Simple static webserver"""
    page_tpl = Content(r"""
            <!doctype html>
            <html>
                <head>
                    <link rel="stylesheet" type="text/css" href="/style.css" />
                    <script src="/script.js"></script>
                </head>
                <body>
                    <article>{content}</article>
                </body>
            </html>
        """, 'text/html')
    
    not_found = Content(r"""<h1>"{path}" not found!</h1>""", 'text/html')
    
    content = Content(r"""
            <h1>Philippov rules!</h1>
            <p>Path: "{path}"</p>
            <p>
                This is a simple example.
            </p>
            <p>See also:
                <ul>
                    <li><a href="_/bump">Bump</a></li>
                    <li><a href="_/jump">Jump</a></li>
                    <li><a href="nope">Nope</a></li>
                </ul>
            </p>
        """, 'text/html')

    style = Content(r"""
        body {
            border: 0;
            font-family: Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        article {
            border: 1px solid #ddd;
            margin: 2em auto;
            padding: 1em;
            position: relative;
            width: 80%;
        }
        """, 'text/css')
    
    script = Content(r"""
        document.addEventListener('DOMContentLoaded', function(e){
            var article = document.querySelector("article");

            var moveOn = function(){
                article.style.left = ".1em";
            };
            var moveBack = function(){
                article.style.left = "0";
            };

            setInterval(function(){
                moveOn();
                setTimeout(moveBack, Math.random() * 1000)
            }, Math.random() * 10000);
        });
        """, 'application/javascript')

    def do_GET(self):
        code, content = self.dispatch(self.path)

        self.send_response(code)
        self.send_header('content-type', content.mime)
        self.end_headers()
        self.wfile.write(bytes(content.content, 'utf8'))
    
    def dispatch(self, path) -> (HTTPStatus, Content):
        if path == '/':
            return HTTPStatus.OK, self.page_tpl.substitute(
                content=self.content.substitute(path=path).content)
        if path.startswith('/_/'):
            return HTTPStatus.OK, self.page_tpl.substitute(content=path)
        elif path == '/style.css':
            return HTTPStatus.OK, self.style
        elif path == '/script.js':
            return HTTPStatus.OK, self.script
        
        return HTTPStatus.NOT_FOUND, self.page_tpl.substitute(
            content=self.not_found.substitute(path=path).content)


if __name__ == '__main__':
    addr = ('localhost', 8888)
    server = HTTPServer(addr, MyLittleJoomla)
    print('Started at http://{}:{}'.format(addr[0], addr[1]))
    server.serve_forever()
