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
    url_health = "http://127.0.0.1:5000/health"
    url_users = "http://127.0.0.1:5000/users"
    response_health = requests.get(url_health)
    response_users = requests.get(url_users)
    json_data1 = response_health.json()
    json_data2 = response_users.json()
    print(json_data1)
    print(json_data2)
