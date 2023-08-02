import logging
from prettycord.__meta__ import __version__
import sys
import aiohttp

logger = logging.getLogger("prettycord")


class BaseSession:
    @staticmethod
    def _get_user_agent():
        user_agent = 'DiscordBot (https://github.com/gfnprodev/prettycord {0}) Python/{1[0]}.{1[1]} aiohttp/{2}'
        return user_agent.format(__version__, sys.version_info, aiohttp.__version__)

    @staticmethod
    def _log_request(request) -> None:
        request_pre = f"{request.method} {request.url}"
        logger.info(f"{request_pre} - Sent")
        logger.debug(f"{request_pre} - {request.headers}")
        request.read()
        logger.debug(f"{request_pre} - {request.content}")

    @staticmethod
    def _log_response(response):
        request = response.request
        logger.info(f"{request.method} {request.url} - "
                    f"Status {response.status_code}")
        logger.debug(response.headers)

    # @classmethod
    # def _convert_and_raise(cls, error):
    #     response = error.response
    #
    #     error_types = {
    #         HTTPStatus.BAD_REQUEST: exceptions.BadQuery,
    #         HTTPStatus.UNAUTHORIZED: exceptions.InvalidAPIKey,
    #         HTTPStatus.FORBIDDEN: exceptions.NoPermission,
    #         HTTPStatus.NOT_FOUND: exceptions.MissingResource,
    #         HTTPStatus.CONFLICT: exceptions.Conflict,
    #         HTTPStatus.TOO_MANY_REQUESTS: exceptions.TooManyRequests,
    #         HTTPStatus.INTERNAL_SERVER_ERROR: exceptions.ServerError,
    #         HTTPStatus.BAD_GATEWAY: exceptions.BadGateway
    #     }
    #     error_type = error_types.get(response.status_code, exceptions.APIError)
    #     raise error_type(response.text)

    # @classmethod
    # def _raise_for_status(cls, response):
    #     if response.is_error:
    #         try:
    #             response.raise_for_status()
    #         except httpx.HTTPStatusError as e:
    #             e.response.read()
    #             cls._convert_and_raise(e)
    #
    #     return
