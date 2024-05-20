import os
import time
import pytest
from PIL import Image
from io import BytesIO
import numpy as np
from API.BeeFreeAPI import BeeFreeAgro


class TestImage(BeeFreeAgro):

    # Test the functionality to retrieve a drone by image.
    @pytest.mark.parametrize("drone_code", ["M3T", "M3M"])
    def test_getDroneByImage(self, drone_code):
        # Send a request to the API with the given drone code and verify the response status is 200 (OK)
        response = self.get_getDroneByImage(drone_code)
        assert response.status_code == 200

        if response.status_code == 200:
            # Read the sourceImage data from the response content
            image_data = BytesIO(response.content)
            # Open the sourceImage using PIL (Python Imaging Library)
            img = Image.open(image_data)

            # Get the current directory path of the script
            current_directory = os.path.dirname(os.path.abspath(__file__))
            # Go one directory up
            parent_directory = os.path.dirname(current_directory)

            # Build relative paths based on the parent directory path
            downloadImage = os.path.join(parent_directory, "downloadImage", f"{drone_code}.png")
            sourceImage = os.path.join(parent_directory, "sourceImage", f"{drone_code}.png")

            # Save the image
            img.save(downloadImage)

            image1 = np.array(Image.open(downloadImage))
            image2 = np.array(Image.open(sourceImage))
            # Compare shapes
            assert image1.shape == image2.shape, "Images have different shapes."

            # Compare pixel values
            difference = np.sum(image1 != image2)
            assert difference == 0, "Images are not identical."

    # Ensure image is a PNG
    @pytest.mark.parametrize("drone_code", ["M3T", "M3M"])
    def test_getDroneByImage_png_format(self, drone_code):
        response = self.get_getDroneByImage(drone_code)
        assert response.status_code == 200

        if response.status_code == 200:
            image_data = BytesIO(response.content)
            img = Image.open(image_data)
            assert img.format == "PNG", "Image is not in PNG format"

    # Test to ensure the API returns 404 for invalid drone codes, without returning an image.
    @pytest.mark.parametrize("drone_code", ["", "INVALID_CODE", "12345", "!@#$%"])
    def test_getDroneByImageInvalidCode(self, drone_code):
        response = self.get_getDroneByImage(drone_code)
        assert response.status_code == 404
        data = response.json()
        assert "Drone not found" in data["detail"]

    # Performance Testing : Ensures the API response time is within acceptable limits,
    # useful for performance Testing
    @pytest.mark.parametrize("drone_code", ["M3T", "M3M"])
    def test_getDroneByImage_performance(self, drone_code):
        start_time = time.time()
        response = self.get_getDroneByImage(drone_code)
        end_time = time.time()
        assert response.status_code == 200
        assert (end_time - start_time) < 2, "API response time is too slow"
