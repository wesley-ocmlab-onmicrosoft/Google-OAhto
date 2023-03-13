# -*- coding: utf-8 -*-
from google.oauth2 import id_token
from google.auth.transport import requests
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
 
GOOGLE_OAUTH2_CLIENT_ID = '1024195588208-ilmo628cbvej7t16igk41nml2pu2srcr.apps.googleusercontent.com'
 
def create_app(app_env=None):
    flask_app = Flask(__name__)
    return flask_app
app = create_app()
 
@app.route('/')
def index():
    return render_template('index.html', google_oauth2_client_id=GOOGLE_OAUTH2_CLIENT_ID)
    
    
@app.route('/google_sign_in', methods=['POST'])
def google_sign_in():
    token = request.json['id_token']
    
    try:
        id_info = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            GOOGLE_OAUTH2_CLIENT_ID
        )
        if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
    except ValueError:
        # Invalid token
        raise ValueError('Invalid token')
 
    print('登入成功')
    return jsonify({}), 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=5000)