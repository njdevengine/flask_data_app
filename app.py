import flask
#https://nordicapis.com/how-to-create-an-api-from-a-dataset-using-python-and-flask/
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "Distant Reading Archive: This site is a prototype API for distant reading of science fiction novels."

@app.route('/test', methods=['GET'])
def test():
	return "this is a test"

app.run()
