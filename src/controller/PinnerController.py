from flask import Blueprint, request
from flask_cors import cross_origin

from src.controller import service
from src.controller.UtilController import UtilController
from src.library.logger.Logger import Logger

pinner_controller = Blueprint('PinnerController', __name__)


class PinnerController:
    @staticmethod
    @cross_origin()
    @pinner_controller.route('/pin', methods=['POST'])
    def create_pin():
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"create_pin: ")
            response = service.create_pin()
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @pinner_controller.route('/pin/<string:pin>', methods=['PATCH'])
    def add_user(pin: str):
        response: dict
        status_code: int = 200
        try:
            name = request.json["name"]
            Logger.info(f"add_user: pin={pin} name={name}")
            response = service.add_user(
                pin=pin,
                name=name
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @pinner_controller.route('/pin/<string:pin>/<string:user_id>', methods=['DELETE'])
    def delete_user(pin: str, user_id: str):
        response: dict = {}
        status_code: int = 200
        try:
            Logger.info(f"delete_user: pin={pin} user_id={user_id}")
            service.delete_user(
                pin=pin,
                user_id=user_id
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @pinner_controller.route('/pin/<string:pin>/users', methods=['GET'])
    def list_users(pin: str):
        response: dict
        status_code: int = 200
        try:
            ids = request.json
            Logger.info(f"list_users: pin={pin}")
            response = service.list_users(pin, ids)
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @pinner_controller.route('/pin', methods=['GET'])
    def list_pin():
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"list_pin: ")
            response = service.list_pin()
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)
