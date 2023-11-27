import os

from motor.motor_asyncio import AsyncIOMotorClient


def create_mongo_url(host: str = "localhost", port: int = 27017) -> str:
    return f"mongodb://{host}:{port}"


DATABASE_NAME = os.environ.get("MONGO_DATABASE", "yorigin")
HOST = os.environ.get("MONGO_HOST", "localhost")
PORT = os.environ.get("MONGO_PORT", 27017)


def create_client(host: str = "localhost", port: int = 27017, event_loop=None) -> AsyncIOMotorClient:
    if event_loop is None:
        return AsyncIOMotorClient(create_mongo_url(host, port))
    return AsyncIOMotorClient(create_mongo_url(host, port), io_loop=event_loop)


def get_client(event_loop=None):
    global __client
    if __client is None:
        __client = create_client(host=HOST, port=int(PORT), event_loop=event_loop)
    return __client


def get_db(event_loop=None):
    global __db
    if __db is None:
        __db = get_client(event_loop)[DATABASE_NAME]
    return __db


__client = (
    None  # AsyncIOMotorClient(create_mongo_url(HOST, int(PORT)))  # db 를 외부 서버에 둠에 따라 이와 같이  환경변수를 통해 세팅되도록 수정하였다.
)
__db = None  # client[DATABASE_NAME]
