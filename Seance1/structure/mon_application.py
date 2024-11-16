from app.app import app

if __name__ == "__main__":
    print(app.config["DEBUG"])
    app.run(debug=app.config["DEBUG"])