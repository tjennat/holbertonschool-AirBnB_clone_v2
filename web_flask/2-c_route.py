from flask import Flask, escape, abort

app = Flask(__name__)


# Route definition with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/', strict_slashes=False)
@app.route('/c/<text>', strict_slashes=False)
def c(text='is_fun'):
    return "C {}".format(escape(text).replace('_', ' '))


# Custom error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(e):
    return "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\">\n" \
           "<title>404 Not Found</title>\n" \
           "<h1>Not Found</h1>\n" \
           "<p>The requested URL was not found on the server. " \
           "If you entered the URL manually please check your spelling and try again.</p>", 404


if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
