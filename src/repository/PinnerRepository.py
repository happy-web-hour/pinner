import os
from typing import List

from src.library.database.Mongo import Mongo


class PinnerRepository:
    def __init__(self):
        self.__mongo: Mongo = Mongo(
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
            default_db=os.getenv("MONGO_INITDB_DATABASE")
        )
        self.__pinner = os.getenv("MONGO_PINNER_DB")

    def create_room(self, pin: dict):
        self.__mongo.insert_one(
            collection=self.__pinner,
            elem=pin
        )

    def list_pin(self):
        return [elem for elem in self.__mongo.find_all(self.__pinner)]

    def add_user(self, pin: str, user: dict):
        self.__mongo.push_element(
            collection=self.__pinner,
            query={"pin": pin},
            obj={
                "users": user
            }
        )

    def delete_user(self, pin: str, user_id: str):
        self.__mongo.pull_element(
            collection=self.__pinner,
            query={
                "pin": pin
            },
            obj={"users": {"userId": user_id}}
        )

    def list_users(self, pin: str, ids: List[str]):
        users = self.__mongo.find_by(
            collection=self.__pinner,
            query={
                "pin": pin
            }
        )["users"]

        return list(filter(lambda user: user["userId"] in ids, users))
