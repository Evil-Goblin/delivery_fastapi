def create_mongo_url(host: str = "localhost", port: int = 27017) -> str:
    return f"mongodb://{host}:{port}"
