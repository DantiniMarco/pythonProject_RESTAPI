from flask import Flask, jsonify
import requests
app = Flask(__name__)


@app.route('/health')
def health_check():
    health_data = {'status': 'ok'}
    response = jsonify(health_data)
    print(response.get_data(as_text=True))
    return response

# Endpoint /users
@app.route('/users')
def get_users():
    users_data = [
        {'id': 1},
        {'id': 2},
        {'id': 3}
    ]
    #response = customize_response(request, users_data)
    return jsonify(users_data)

if __name__ == '__main__':
    app.run(debug=True)
