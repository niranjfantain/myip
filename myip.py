from bottle import route, run, request


@route('/')
def hello():
    return request.remote_addr

run(host='localhost', port=8080, debug=True)
