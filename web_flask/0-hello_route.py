#!/usr/bin/python3
#creating a flask app for web

from flask import Flask

app = Flask(__name__)

#defining the route for the root /

@app.route('/', strict_slashes=False)

def my_route():
	return 'Hello HBNB!'
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

