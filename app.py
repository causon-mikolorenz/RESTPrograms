from flask import Flask, request
import sqlite3

PROGRAMS_DB = "programs.db"

app = Flask(__name__)

def create_tables():
    """Create programs table if they don't exist"""
    with sqlite3.connect(PROGRAMS_DB) as connection:
        cursor = connection.cursor()
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS program (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(255) NOT NULL,
                       year_duration INTEGER NOT NULL,
                       level VARCHAR(100) NOT NULL,
                       degree_type VARCHAR(100) NOT NULL)""")
        
        connection.commit()
        print("Program table has been created successfully!")

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

@app.route('/programs/<int:id>', methods=['PUT'])
def replace_program(id):
    # TODO(Causon): Implement logic to fully replace a program
    pass

@app.route('/programs/<int:id>', methods=['PATCH'])
def modify_program(id):
    # TODO(Causon): Implement logic to partially update a program
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
    create_tables()
    app.run(debug=True)