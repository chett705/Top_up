from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS if you're dealing with cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory storage for demonstration purposes
data_store = []

@app.route('/api/checkID', methods=['POST'])
def check_id():
    data = request.json
    user_id = data.get('userId')
    server_id = data.get('serverId')

    if not user_id or not server_id:
        return jsonify({"success": False, "message": "User ID and Server ID are required"}), 400

    # Here you can add logic to validate the user ID and server ID
    # For demonstration, we'll just store the data and return a success message

    data_store.append({"userId": user_id, "serverId": server_id})
    return jsonify({"success": True, "message": "ID checked successfully", "userId": user_id, "serverId": server_id})

@app.route('/api/getData', methods=['GET'])
def get_data():
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(debug=True)