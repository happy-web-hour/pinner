from src.repository.PinnerRepository import PinnerRepository
from src.repository.RoomRepository import RoomRepository
from src.service.PinnerService import PinnerService

pinner_repository = PinnerRepository()
room_repository = RoomRepository()

service = PinnerService(
    pinner_repository=pinner_repository,
    room_repository=room_repository
)
