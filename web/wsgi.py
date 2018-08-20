from app import app

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8080, debug=True) # This is the default port for Flask-Appbuilder
    app.run(host='0.0.0.0', port=5000, debug=False) # Changing to port 5000 as it is the default for Flask