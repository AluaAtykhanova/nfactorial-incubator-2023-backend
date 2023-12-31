from datetime import datetime

from bson.objectid import ObjectId
from pymongo.database import Database


class ShanyraksRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_post(self, user_id: str, post: dict):
        payload = {
            "user_id": ObjectId(user_id),
            "type": post["type"],
            "price": post["price"],
            "address": post["address"],
            "area": post["area"],
            "rooms_count": post["rooms_count"],
            "description": post["description"],
            "created_at": datetime.utcnow(),
        }

        posts = self.database["posts"].insert_one(payload)

        post_id = posts.inserted_id

        post = self.database["posts"].find_one({"_id": post_id})

        return str(post_id)

    def get_post_by_id(self, post_id: str):
        post = self.database["posts"].find_one({"_id": ObjectId(post_id)})

        return post

    def update_post_by_id(self, post_id: str, post: dict):
        filter_query = {"_id": ObjectId(post_id)}
        update_query = {"$set": post}

        self.database["posts"].update_one(filter_query, update_query)

        result = self.database["posts"].find_one(
            {
                "_id": ObjectId(post_id),
            }
        )
        return result

    def delete_post(self, post_id: str):
        self.database["posts"].delete_one({"_id": ObjectId(post_id)})
