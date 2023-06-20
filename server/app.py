#!/usr/bin/env python3

from flask import Flask
# from werkzeug.wrappers import Request, Response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route('/print/<string:parameter>')
def print_string(parameter):
    return f'<h1>Profile for {parameter}</h1>'


@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join([str(x) for x in range(1, parameter+1)])
    return numbers


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
        return str(result)

    elif operation == '*':
        result = num1 * num2
        return str(result)


    elif operation == '-':
        result = num1 - num2
        return str(result)

    elif operation == 'div':
        result = num1 / num2
        return str(result)

    else:
        return "not a valid operation"
    


# @Request.application
# def application(request):
#     print(f'This web server is running at {request.remote_addr}')
#     return Response('A WSGI generated this response!')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
