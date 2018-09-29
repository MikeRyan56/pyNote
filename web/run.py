from flask import Flask
from app import app

# app.run(host='localhost','0.0.0.0', port=8080, debug=True)
app.run(host='0.0.0.0', port=5000, debug=True)
