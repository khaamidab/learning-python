from flask import Flask
from routes import hello_route, user_route

app = Flask(__name__)

# Register routes
app.register_blueprint(hello_route)
app.register_blueprint(user_route)

if __name__ == '__main__':
    app.run()
