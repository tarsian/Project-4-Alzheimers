from flask import Flask, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)

# SQLAlchemy engine creation (connect to the database)
engine = create_engine('sqlite:///alzheimers.db')

@app.route('/data', methods=['GET'])
def get_data():
    # Query data from the database
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM alzheimers_data"))
        data = [dict(zip(result.keys(), row)) for row in result]
        return jsonify(data)

if __name__ == '__main__':
    # Running the Flask app
    app.run(debug=True)
    
    # Print the URL to access data
    print("\nServer is running. Visit http://localhost:5000/data to see the data.\n")
