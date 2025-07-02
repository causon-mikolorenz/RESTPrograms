from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    pass

@app.route('/programs', methods=['GET'])
def list_programs():
    #TODO(Franco): Implement logic to list all programs
    pass

@app.route('/programs/<int:id>', methods=['GET'])
def get_program(id):
    #TODO(Franco): Implement logic to get a specific program by ID
    pass

if __name__ == "__main__":
    app.run(debug=True)