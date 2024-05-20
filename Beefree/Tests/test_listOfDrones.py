import json
import pytest
from jsonschema import validate
from API.BeeFreeAPI import BeeFreeAgro


class TestAllDrones(BeeFreeAgro):

    @pytest.fixture
    def JsonSchema(self):
        """Fixture to load the schema from file."""
        with open('../jsonSchema/dronesSchema.json') as schema_file:
            return json.load(schema_file)

    def test_dronesSchema(self, JsonSchema):
        response_data = self.get_getAllDrones()
        assert response_data.status_code == 200
        data = response_data.json()
        # Validate the response data against the schema
        validate(instance=data, schema=JsonSchema)

    @pytest.mark.parametrize("count", [8])
    def test_dronesCount(self, count):
        response_data = self.get_getAllDrones()
        assert response_data.status_code == 200
        data = response_data.json()
        assert len(data) == count

    # This test checks that the API responds within 2 seconds
    def test_responseTime(self):
        response = self.get_getAllDrones()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 2, "Response time is too slow"

    # This test asserts that the response contains data and is not empty.
    def test_nonEmptyResponse(self):
        response = self.get_getAllDrones()
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0, "Response data is empty"

    # Test for unique drone IDs
    def test_uniqueDroneIDs(self):
        response = self.get_getAllDrones()
        assert response.status_code == 200
        data = response.json()
        # Initialize an empty list to store drone codes
        ids = []
        # Loop through each drone in the data and append its code to the list
        for drone in data:
            ids.append(drone['drone_code'])
        # Check for duplicate drone IDs
        assert len(ids) == len(set(ids)), "There are duplicate drone IDs"
