import pytest
from API.BeeFreeAPI import BeeFreeAgro
from dataModel.fullDataModel import *


class Test_model(BeeFreeAgro):

    # Test case for checking if drone model exists
    @pytest.mark.parametrize("drone_code", ["M2P"])
    def test_droneModelExists(self, drone_code):
        # Get the expected data for M2P model
        exceptedM2pData = m2pFullData()

        # Make a request to get drone data by model code
        response = self.get_getDroneByModel(drone_code)
        # Assert that the request was successful (status code 200)
        assert response.status_code == 200

        # Extract the actual data from the response
        actualData = response.json()

        # Assert various properties of the drone match the expected data
        assert actualData["drone_code"] == exceptedM2pData["drone_code"]
        assert actualData["cameras"][0]["name"] == exceptedM2pData["cameras"][0]["name"]
        assert actualData["cameras"][0]["megapixels"] == exceptedM2pData["cameras"][0]["megapixels"]
        assert actualData["cameras"][0]["type"] == exceptedM2pData["cameras"][0]["type"]

    # Test case for checking if drone model does not exist
    @pytest.mark.parametrize("drone_code", ["NotExist"])
    def test_droneModelNotExists(self, drone_code):
        response = self.get_getDroneByModel(drone_code)
        # Assert that the request returns a 404 error (drone not found)
        assert response.status_code == 404
        assert response.json()["detail"] == "Drone not found"

