#Adrian Valdez
#CS350 Lab4
#Feb. 26, 2018


from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import json

f = open('cve.json', 'r')
db = json.loads(f.read())
f.close()


def home_view(request):
    return Response('To search, type /search/ then the word or letter you would like to search. Research if nothing is found')

def search_view(request):
    output = ''
    myinput = request.matchdict
    for item in db:
        letter = myinput['query']
        word = item.lower()

        if letter.lower() in word.split():
            output += item + "\n"

    if output != '':
        return Response(output)
    else:
        return Response("No results found.")

if __name__ == '__main__':
    with Configurator() as config:

        config.add_route('home', '/home')
        config.add_route('search', 'search/{query}')

        config.add_view(home_view, route_name='home')
        config.add_view(search_view, route_name='search')

        app = config.make_wsgi_app()
        server = make_server('0.0.0.0', 8080, app)
server.serve_forever()
