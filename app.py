from flask import Flask, request, jsonify
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

def get_programs():
    year_length = request.args.get('year_length')
    name = request.args.get('name')
    degree_type = request.args.get('degree_type')

    query = "SELECT * FROM program WHERE 1=1"
    params = []

    if year_length:
        try:
            int(year_length) 
            query += " AND year_duration = ?"
            params.append(year_length)
        except ValueError:
            return jsonify({"error": "year_length must be an integer"}), 400

    if name:
        query += " AND LOWER(name) = ?"
        params.append(name.lower())

    if degree_type:
        query += " AND LOWER(degree_type) = ?"
        params.append(degree_type.lower())

    try:
        with sqlite3.connect(PROGRAMS_DB) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()

            programs = [dict(row) for row in rows]
            return jsonify(programs), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/')
def home():
    pass

@app.route('/programs', methods=['GET'])
def list_programs():
    return get_programs()

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
    data = request.get_json()

    name = data.get('name')
    year_duration = data.get('year_duration')
    level = data.get('level')
    degree_type = data.get('degree_type')

    if not all([name, year_duration, level, degree_type]):
        return jsonify({"Error": "All fields are required"}), 400
    
    with sqlite3.connect(PROGRAMS_DB) as connection:
        cursor = connection.cursor()
        cursor.execute("""
                INSERT INTO program (
                        name, 
                        year_duration, 
                        level, 
                        degree_type
                )VALUES (?, ?, ?, ?)""",
                (name, year_duration, level, degree_type))
        connection.commit()
        program_id = cursor.lastrowid

    return jsonify({
        "Message": "Program created successfully",
        "Program": {
            "Program ID": program_id,
            "Program Name": name, 
            "Year Duration": year_duration,
            "Level": level,
            "Degree Type": degree_type
        }
    }), 201

@app.route('/programs/<int:id>', methods=['DELETE'])
def delete_program(id):
    """Delete a program by ID"""
    with sqlite3.connect(PROGRAMS_DB) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM program WHERE id = ?", (id,))
        connection.commit()

    if cursor.rowcount == 0:
        return jsonify({"Error": "Program not found"}), 404        
    return jsonify({"Message": "Program deleted successfully"}), 200

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)