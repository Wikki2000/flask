#!/usr/bin/python3
"""This program illustrate how to use errorhandler() functon

Usage: curl http://127.0.0.1:5000/example -X POST -H \
        'Content-Type: application/json' \ 
            -d '{"data": "hi"}'
"""
from flask import Flask, jsonify, request, abort


app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    """ Defines the behavior of program when encounter a 404 error. """
    return jsonify({"status": "Bad Requests",
                    "message": "Requested page not available"}), 404

@app.route('/example', methods=['POST'])
def example():
    """ An example Function. """
    data = request.get_json()
    if not data:
        abort(404)
    return jsonify({"message": "Success"}), 200

if __name__ == '__main__':
    app.run(debug=True)
