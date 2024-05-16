import requests


class BeeFreeAgro:
    base_url = "https://interviews-api.beefreeagro.com/api/v1"

    def get_getAllDrones(self):
        response = requests.get(f"{self.base_url}/drones")
        return response

    def get_getDroneByModel(self, drone_code):
        response = requests.get(f"{self.base_url}/drones/{drone_code}")
        return response

    def get_getDroneByImage(self, drone_code):
        response = requests.get(f"{self.base_url}/drones/{drone_code}/image")
        return response
