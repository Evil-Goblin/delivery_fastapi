import asyncio
import json
import os
from typing import Any

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from pymongo.errors import BulkWriteError


def create_mongo_url(host: str = "localhost", port: int = 27017) -> str:
    return f"mongodb://{host}:{port}"


DATABASE_NAME = os.environ.get("MONGO_DATABASE", "yorigin")
HOST = os.environ.get("MONGO_HOST", "localhost")
PORT = os.environ.get("MONGO_PORT", 27017)

client: Any = AsyncIOMotorClient(create_mongo_url(HOST, int(PORT)))
db: Any = client[DATABASE_NAME]
shop_collection: Any = AsyncIOMotorCollection(db, "shops")


async def insert_all() -> None:
    """
    프로젝트 root 에서 실행하세요
    :return:
    """
    for filename in os.listdir("assets/shops"):
        if not os.path.isfile(f"assets/shops/{filename}"):
            continue
        with open(f"assets/shops/{filename}") as f:
            data = json.load(f)
            print(f"start to insert {filename}")
            try:
                await shop_collection.insert_many(data)
            except BulkWriteError:
                print(f"{filename} failed")
                continue
            print(f"{filename} inserted")


asyncio.run(insert_all())
