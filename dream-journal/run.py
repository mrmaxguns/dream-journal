import webbrowser
from os import path

from waitress import serve

from app import app, create_db


def main():
    if not path.exists("entries.db"):
        create_db()
        print("Database initialized")

    webbrowser.open("http://0.0.0.0:8080/")
    serve(app, port=8080)


if __name__ == "__main__":
    main()
