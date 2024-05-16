import re

import pytest

from API.BeeFreeAPI import BeeFreeAgro


class Test_allDrones(BeeFreeAgro):

    def test_dronesKeys(self):
        response_data = self.get_getAllDrones()
        assert response_data.status_code == 200
        data = response_data.json()

        expected_keys = ["drone_code", "name", "range", "release_date"]

        # Iterate over each dictionary in the list
        for item in data:
            # Iterate over the keys in the current dictionary
            for key in item.keys():
                # Assert that the key exists in the expected_keys set
                assert key in expected_keys

    def test_dataType(self):
        response_data = self.get_getAllDrones()
        assert response_data.status_code == 200
        data = response_data.json()

        expected_keys = ["drone_code", "name", "range", "release_date"]

        # Iterate over each dictionary in the list
        for item in data:
            # Iterate over the keys in the current dictionary
            for key in item.keys():
                # Assert that the key exists in the expected_keys set
                assert key in expected_keys

            # Additional checks for data types
            assert isinstance(item["drone_code"], str)
            assert isinstance(item["name"], str)
            assert isinstance(item["range"], (int, float))  # Assuming range can be integer or float
            assert isinstance(item["release_date"], str)  # Assuming release_date is a string
            # Additional check for release_date format
            assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$', item["release_date"])

    @pytest.mark.parametrize("count", [8])
    def test_dronesCount(self, count):
        response_data = self.get_getAllDrones()
        assert response_data.status_code == 200
        data = response_data.json()
        assert len(data) == count
