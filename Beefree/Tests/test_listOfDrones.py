import json
import pytest
from jsonschema import validate
from API.BeeFreeAPI import BeeFreeAgro


class Test_allDrones(BeeFreeAgro):

    def test_dronesSchema(self):
        response_data = self.get_getAllDrones()
        assert response_data.status_code == 200
        data = response_data.json()

        # Load the schema
        with open('../jsonSchema/dronesSchema.json') as schema_file:
            schema = json.load(schema_file)

        # Validate the response data against the schema
        validate(instance=data, schema=schema)

    @pytest.mark.parametrize("count", [8])
    def test_dronesCount(self, count):
        response_data = self.get_getAllDrones()
        assert response_data.status_code == 200
        data = response_data.json()
        assert len(data) == count

    #   new test

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