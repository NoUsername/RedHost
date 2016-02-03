from six.moves.urllib.parse import urlparse, urlunparse
import re
import flask
import sys
import yaml
app = flask.Flask(__name__)

portRedirects = {
    'example.lan': '8080'
}

redirects = {
    'test.bla' : 'https://google.at'
}

@app.route('/')
def hello():
    urlparts = urlparse(flask.request.url)
    hostname = urlparts.hostname
    if hostname in portRedirects:
        port = portRedirects[hostname]
        urlparts = list(urlparts)
        urlparts[1] = '%s:%s'%(hostname, port)
        return flask.redirect(urlunparse(urlparts))
    if hostname in redirects:
        return flask.redirect(redirects[hostname])
    return 'sorry, i don\'t know: %s'%hostname

if __name__ == '__main__':
    with open('red.yaml', 'r') as f:
        config = yaml.load(f)
        portRedirects = config.get('portRedirects')
        redirects = config.get('redirects')
    app.run(host='0.0.0.0', port=80, debug='debug' in sys.argv)
