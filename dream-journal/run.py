import os
import webbrowser

from waitress import serve

from app import app, create_db


def main():
    # initialize database if it doesn't exist
    current_path = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(os.path.join(current_path, "entries.db")):
        create_db()
        print("Database initialized")

    # auto-open the application
    webbrowser.open("http://0.0.0.0:8080/")
    serve(app, port=8080)


if __name__ == "__main__":
    main()
