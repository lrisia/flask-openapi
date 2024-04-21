from config import Config
from api.server import Server

def main():
    app = Server()
    app.run()


if __name__ == "__main__":
    main()
