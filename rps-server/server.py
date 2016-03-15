from persistence.mongo_database import Persistence
from rest.rest_server import run_rest_server


def main():
    Persistence.initialize()
    run_rest_server()


if __name__ == '__main__':
    main()