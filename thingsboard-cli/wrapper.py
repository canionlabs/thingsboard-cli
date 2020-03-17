import requests
import asyncio

from .exceptions import Exception;

class ThingsBoardAuth:
    URL = 
    USERNAME = 
    PASSWORD = 

    def __init__(self):
        self.session = requests.Session()
        self.login()

    @staticmethod
    def _response_handler(status_code, response):
        if status_code != response.status_code:
            raise TBException(
                f"Unexpected Response ({response.status_code}) \n"
                f"{response.content}"
            )

    def _update_headers(self, new_header: dict):
        self.session.headers.update(new_header)

    async def login(self):
        auth_url = f"{self.URL}/api/auth/login"

        response = await self.session.post(
            auth_url, 
            json={
            "username": self.USERNAME,
            "password": self.PASSWORD,
            }
        )

        self._response_handler(200, response)

        auth_data = response.json()

        await self._update_headers({
            "X-Authorization": f"Bearer {auth_data['token']}"
        })

    async def create_group(self, params: dict):
        group_url = f"{self.URL}/api/entityGroup"

        response = await self.session.post(
            group_url,
            params,
        )

        return response
    
    async def create_customer(self, params: dict):
        customer_url = f"{self.URL}/api/customer{?entityGroupId}"

        response = await self.session.post(
            customer_url,
            params,
        )

        return response
    
    async def create_user_of_customer(self, params: dict):
        user_costumer_url = f"{self.URL}/api/user{?sendActivationMail,entityGroupId}"

        response = await self.session.post(
            user_costumer_url,
            params,
        )

        return response
    
    async def create_device(self, params: dict):
        device_url = f"{self.URL}/api/device{?accessToken,entityGroupId}"

        response = await self.session.post(
            device_url,
            params,
        )

        return response

    async def create_dashboard(self, params: dict):
        dashboard_url = f"{self.URL}/api/dashboard{?entityGroupId}"

        response = await self.session.post(
            dashboard_url,
            params,
        )

        return response