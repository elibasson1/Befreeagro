import json
import pytest
from API.BeeFreeAPI import BeeFreeAgro
from dataModel.fullDataModel import *
from jsonschema import validate


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

        # i Change here delete all assert add only one
        assert actualData == exceptedM2pData

    # Test case for checking if drone model does not exist
    @pytest.mark.parametrize("drone_code", ["NotExist", "INVALID_CODE", "12345", "!@#$%"])
    def test_droneModelNotExists(self, drone_code):
        response = self.get_getDroneByModel(drone_code)
        # Assert that the request returns a 404 error (drone not found)
        assert response.status_code == 404
        assert response.json()["detail"] == "Drone not found"

    # Test case for validating drone model response schema
    @pytest.mark.parametrize("drone_code", ["M2P"])
    def test_droneModelValidSchema(self, drone_code):
        # Make a request to get drone data by model code
        response = self.get_getDroneByModel(drone_code)
        # Assert that the request was successful (status code 200)
        assert response.status_code == 200
        data = response.json()

        # Load the schema from file
        with open('../jsonSchema/droneByModelSchema.json') as schema_file:
            schema = json.load(schema_file)

        # Validate the response data against the schema
        validate(instance=data, schema=schema)
