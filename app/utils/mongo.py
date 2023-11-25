import os

from motor.motor_asyncio import AsyncIOMotorClient


def create_mongo_url(host: str = "localhost", port: int = 27017) -> str:
    return f"mongodb://{host}:{port}"


DATABASE_NAME = os.environ.get("MONGO_DATABASE", "yorigin")
HOST = os.environ.get("MONGO_HOST", "localhost")
PORT = os.environ.get("MONGO_PORT", 27017)

client = AsyncIOMotorClient(create_mongo_url(HOST, int(PORT)))  # db 를 외부 서버에 둠에 따라 이와 같이  환경변수를 통해 세팅되도록 수정하였다.
db = client[DATABASE_NAME]


import asyncio


async def print_mongo_version() -> None:
    status = await client.test.command("serverStatus")
    print(status["version"])


asyncio.run(print_mongo_version())
