import os
import pytest
from PIL import Image
from io import BytesIO
import numpy as np
from API.BeeFreeAPI import BeeFreeAgro


class Test_image(BeeFreeAgro):

    @pytest.mark.parametrize("drone_code", ["M3T", "M3M"])  # Add test if not exist
    def test_getDroneByImage(self, drone_code):
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

