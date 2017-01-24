from bottle import get, post, run, request, response
import json


@get('/text/<name>')
def get_text(name):
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'name': name})


@post('/text')
def get_text_from_image():
    data = request.json()  # di bayza
    image = data['image']
    #get text
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'text': image})

run(host='localhost', port=8080)
