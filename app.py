from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    pass

def list_programs():
    """
    Handles:
    - GET /programs → list all
    - GET /programs?year_length=4
    - GET /programs?name=BSIT
    - GET /programs?degree_type=Bachelor
    """
    year_length = request.args.get('year_length')
    name = request.args.get('name')
    degree_type = request.args.get('degree_type')

    # TODO(Franco): Implement logic to filter based on the above query params
    pass

@app.route('/programs/<int:id>', methods=['PUT', 'PATCH'])
def update_program(id):
    #TODO(Causon): Implement logic to update a program
    pass

@app.route('/programs', methods=['POST'])
def create_program():
    #TODO(Efondo): Implement logic to create a program
    pass

@app.route('/programs/<int:id>', methods=['DELETE'])
def delete_program(id):
    #TODO(Lopez): Implement logic to delete a program
    pass

if __name__ == "__main__":
    app.run(debug=True)