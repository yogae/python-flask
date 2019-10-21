from flask import Flask, request, jsonify
app = Flask(__name__)

db_cache = []
@app.route('/users', methods=['POST'])
def create_users():
    new_user = request.json
    print(new_user)
    db_cache.append(new_user)
    return jsonify(new_user)


@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(db_cache)


@app.route('/users/<user_id>', methods=['GET'])
def get_users(user_id):
    userid_int = (int)(user_id)
    return jsonify(db_cache[userid_int])


@app.route('/users/<user_id>', methods=['PUT'])
def update_users(user_id):
    userid_int = (int)(user_id)
    db_cache[userid_int] = new_user = request.json
    return jsonify(db_cache[userid_int])
