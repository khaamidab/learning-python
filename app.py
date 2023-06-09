from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Configure PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="your_database",
    user="your_username",
    password="your_password"
)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/users', methods=['POST'])
def create_user():
    try:
        # Get the user data from the request
        user_data = request.get_json()
        name = user_data['name']
        email = user_data['email']

        # Create a cursor to interact with the database
        cursor = conn.cursor()

        # Execute the SQL query to insert the user
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()

        # Close the cursor
        cursor.close()

        # Return a success response
        return jsonify({'message': 'User created successfully'})

    except (psycopg2.Error, KeyError) as error:
        # Rollback the transaction in case of an error
        conn.rollback()

        # Return an error response
        return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run()
