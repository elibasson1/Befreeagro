import json
import pytest
from API.BeeFreeAPI import BeeFreeAgro
from dataModel.fullDataModel import *
from jsonschema import validate


class TestModel(BeeFreeAgro):

    @pytest.fixture
    def exceptedM2pData(self):
        """Fixture to provide expected data for M2P model."""
        return m2pFullData()

    @pytest.fixture
    def JsonSchema(self):
        """Fixture to load the schema from file."""
        with open('../jsonSchema/droneByModelSchema.json') as schema_file:
            return json.load(schema_file)

    """
    Test case for checking if drone model exists.
    Verifies that the data for the given drone model code matches the expected data.
    """
    @pytest.mark.parametrize("drone_code", ["M2P"])
    def test_droneModelExists(self, drone_code, exceptedM2pData):
        response = self.get_getDroneByModel(drone_code)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        # Extract the actual data from the response
        actualData = response.json()
        assert actualData == exceptedM2pData, "Actual data does not match expected data"

    # Test case for checking if drone model does not exist
    @pytest.mark.parametrize("drone_code", ["NotExist", "INVALID_CODE", "12345", "!@#$%"])
    def test_droneModelNotExists(self, drone_code):
        response = self.get_getDroneByModel(drone_code)
        # Assert that the request returns a 404 error (drone not found)
        assert response.status_code == 404
        assert response.json()["detail"] == "Drone not found"

    """
    Test case for validating the response schema of the drone model.
    Ensures that the data returned by the API adheres to the defined JSON schema.
    """
    @pytest.mark.parametrize("drone_code", ["M2P"])
    def test_droneModelValidSchema(self, drone_code, JsonSchema):
        # Make a request to get drone data by model code
        response = self.get_getDroneByModel(drone_code)
        # Assert that the request was successful (status code 200)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        data = response.json()
        # Validate the response data against the schema
        validate(instance=data, schema=JsonSchema)
