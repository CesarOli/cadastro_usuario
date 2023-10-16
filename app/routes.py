from app import app
from flask import request, jsonify

@app.route('/cadastro', methods=['POST'])
