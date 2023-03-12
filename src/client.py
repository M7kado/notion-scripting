import requests

from dto.page import Page

class Client:

    base_headers = {}
    BASE_URL = "https://api.notion.com/v1/"

    def __init__(self, auth):
        self._auth = auth
        self.base_headers = {
            "accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Authorization": f'Bearer {auth}'
        }

    def get(self, endpoint):
        response = requests.get(self.BASE_URL + endpoint, headers=self.base_headers)

        return response.json()

    def get_block(self, block_id):
        return self.get(f"blocks/{block_id}")

    def get_children(self, block_id):
        return self.get(f"blocks/{block_id}/children")

    def get_db(self, db_id):
        return self.get(f"databases/{db_id}")

    def get_page(self, page_id):
        json_response = self.get(f"pages/{page_id}")
        return Page(page_id, self, json_response["properties"])

    def get_property(self, page_id, property_id):
        return self.get(f"pages/{page_id}/properties/{property_id}")

    def patch(self, endpoint, body):
        response = requests.patch(self.BASE_URL + endpoint, headers=self.base_headers, json=body)

        return response.json()

    def change_page_title(self, page_id, new_title):
        body = {
            "properties" : {
            'title': {'title': [{'text': {'content': new_title}}]}}
        }
        return self.patch(f"pages/{page_id}", body)