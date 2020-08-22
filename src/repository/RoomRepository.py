import os

import requests


class RoomRepository:
    def __init__(self):
        self.__host = os.getenv("ROOM_HOST")
        self.__port = os.getenv("ROOM_PORT")
        self.__room_url = f"http://{self.__host}:{self.__port}"

    def create_room(self, pin: str):
        requests.post(
            url=f"{self.__room_url}/room/{pin}"
        )