from flask import Flask, request, jsonify

app = Flask(__name__)

DATA_FILE = "user_data.txt"

@app.route('/api/checkID', methods=['POST'])
def check_id():
    data = request.json
    user_id = data.get('userId')
    server_id = data.get('serverId')

    if not user_id or not server_id:
        return jsonify({"success": False, "message": "User ID and Server ID are required"}), 400

    with open(DATA_FILE, "a") as file:
        file.write(f"User ID: {user_id}, Server ID: {server_id}\n")

    return jsonify({"success": True, "message": "ID checked successfully", "userId": user_id, "serverId": server_id})

@app.route('/api/getData', methods=['GET'])
def get_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = file.readlines()
        return jsonify({"success": True, "data": data})
    except FileNotFoundError:
        return jsonify({"success": False, "message": "No data found"}), 404

if __name__ == '__main__':
    app.run(debug=True)