from project.config import DevelopmentConfig
from server import create_app

app = create_app(DevelopmentConfig)


if __name__ == '__main__':
    app.run(host="localhost", port=25000, debug=True)
