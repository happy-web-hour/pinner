import uuid
from typing import List

from src.repository.PinnerRepository import PinnerRepository
from src.repository.RoomRepository import RoomRepository


class PinnerService:
    def __init__(self, pinner_repository: PinnerRepository, room_repository: RoomRepository):
        self.__pinner_repository = pinner_repository
        self.__room_repository = room_repository

    def create_pin(self) -> dict:
        pin = {
            "pin": str(uuid.uuid4()),
            "users": []
        }
        self.__pinner_repository.create_room(pin)
        self.__room_repository.create_room(pin["pin"])
        return {
            "pin": pin["pin"]
        }

    def add_user(self, pin: str, name: str):
        user = {
            "userId": str(uuid.uuid4()),
            "name": name
        }
        self.__pinner_repository.add_user(pin, user)
        return user

    def delete_user(self, pin: str, user_id: str):
        self.__pinner_repository.delete_user(
            pin=pin,
            user_id=user_id
        )

    def list_users(self, pin: str, ids: List[str]):
        return self.__pinner_repository.list_users(pin, ids)

    def list_pin(self):
        return self.__pinner_repository.list_pin()