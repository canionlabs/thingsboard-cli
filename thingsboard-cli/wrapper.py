import requests

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

    def login(self):
        auth_url = f"{self.URL}/api/auth/login"

        response = self.session.post(
            auth_url, 
            json={
            "username": self.USERNAME,
            "password": self.PASSWORD,
            }
        )

        self._response_handler(200, response)

        auth_data = response.json()

        self._update_headers({
            "X-Authorization": f"Bearer {auth_data['token']}"
        })

    def create_group(self, params: dict):
        group_url = f"{self.URL}/api/entityGroup"

        response = self.session.post(
            group_url,
            params,
        )
    
    def create_costumer(self, params: dict):
        customer_url = f"{self.URL}/api/customer{?entityGroupId}"

        response = self.session.post(
            customer_url,
            params,
        )
    
    def create_user_of_costumer(self, params: dict):
        user_costumer_url = f"{self.URL}/api/user{?sendActivationMail,entityGroupId}"

        response = self.session.post(
            user_costumer_url,
            params,
        )
    
    def create_device(self, params: dict):
        device_url = f"{self.URL}/api/device{?accessToken,entityGroupId}"

        response = self.session.post(
            device_url,
            params,
        )

    def create_dashboard(self, params: dict):
        dashboard_url = f"{self.URL}/api/dashboard{?entityGroupId}"

        response = self.session.post(
            dashboard_url,
            params,
        )