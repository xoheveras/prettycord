import ssl
from typing import Optional, Type, Dict, Any

import aiohttp
import certifi
from aiohttp import ClientSession, TCPConnector

from .base import BaseSession


class Session(BaseSession):
    def __init__(self, token: str) -> None:
        self.token = token
        self._headers = {
            'User-Agent': self._get_user_agent(),
            'Authorization': 'Bot' + token
        }
        self._session: Optional[ClientSession] = None
        self._connector_init: Dict[str, Any] = {
            "ssl": ssl.create_default_context(cafile=certifi.where()),
        }
        self._connector_type: Type[TCPConnector] = TCPConnector
        self._should_reset_connector = True

    async def create_session(self) -> ClientSession:
        if self._should_reset_connector:
            await self.close()

        if self._session is None or self._session.closed:
            self._session = ClientSession(
                connector=self._connector_type(**self._connector_init),
                headers=self._headers
            )
            self._should_reset_connector = False

        return self._session

    async def close(self) -> None:
        if self._session is not None and not self._session.closed:
            await self._session.close()
