import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.endpoint = os.getenv("SHEET_ENDPOINT")
        self.headers = {
            "Authorization": f"Bearer {os.getenv('SHEET_TOKEN')}",
        }
    
    def get_rows(self):
        response = requests.get(self.endpoint, headers=self.headers)
        
        return response.json()["prices"]
    
    def update_row(self, row_id, data):
        response = requests.put(f"{self.endpoint}/{row_id}", headers=self.headers, json=data)
        
        print(response.text)