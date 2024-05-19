**BeeFreeAgro API Testing**

BeeFreeAgro API

Description

The BeeFreeAgro API provides access to data about drones manufactured by BeeFreeAgro.

**Base URL**

- [**https://interviews-api.beefreeagro.com/api/v1**](https://interviews-api.beefreeagro.com/api/v1)

**Endpoints**

1. GET All Drones : **GET /drones**
- Retrieves information about all available drones.

2. GET Drone By Model : **GET /drones/{drone\_code}**
- Retrieves information about a specific drone identified by its model code.

3. GET Drone Image : **GET /drones/{drone\_code}/image**
- Retrieves the image of a specific drone identified by its model code.

This repository contains tests for the BeeFreeAgro API, which provides endpoints to interact with drone data.

**Overview**

The API testing is organized into several test files, each targeting different aspects of the API:

- test\_droneModel.py: Tests related to querying drone models.
- test\_imageDrone.py: Tests related to retrieving drones by image.
- test\_listOfDrones.py: Tests related to retrieving a list of all drones.

**Getting Started**

To run the tests, make sure you have Python installed on your system. You may also need to install the required dependencies using pip:

pip install -r requirements.txt


**Test Files**

**test\_droneModel.py**

This file contains tests related to querying drone models.

**Test Functions**:

- **test\_droneModelExists**: Checks if a drone model exists by querying its model code. It verifies that the response status is 200 and compares the retrieved data with expected data.

- **test\_droneModelNotExists**: Tests if the API returns a 404 error for invalid drone model codes, ensuring that the response indicates "Drone not found".

- **test\_droneModelValidSchema**: Validates the response schema for querying drone models against a predefined JSON schema.

**test\_imageDrone.py**

This file contains tests related to retrieving drones by image.

**Test Functions:**

- **test\_getDroneByImage**: Tests the functionality to retrieve a drone by image. It verifies that the response status is 200, compares the retrieved image with the expected image, and checks for PNG format.
- **test\_getDroneByImageInvalidCode**: Ensures the API returns 404 for invalid drone codes without returning an image, and verifies the response message.
- **test\_getDroneByImage\_performance**: Performs performance testing to ensure that the API response time is within acceptable limits.

**test\_listOfDrones.py**

This file contains tests related to retrieving a list of all drones.

**Test Functions**:

- **test\_dronesSchema**: Validates the response schema for retrieving a list of all drones against a predefined JSON schema.
- **test\_dronesCount**: Verifies that the API returns the expected number of drones.
- **test\_responseTime**: Checks that the API responds within 2 seconds.
- **test\_nonEmptyResponse**: Asserts that the response contains data and is not empty.
- **test\test_uniqueDroneIDs**:This test extracts the id field from each drone and ensures all IDs are unique by comparing the list length with the length of the set of IDs.

**Running Tests**

Since this project operates within a virtual environment using Python, follow these steps to execute the tests:

1. Open your command prompt (**CMD**).
1. Navigate to the directory named **Beefree**
1. Choose the directory **.venv\Scripts**
1. Run the command **activate.bat**.
1. Return to the directory **Beefree\Tests**
1. Execute the command **pytest -v -s**

**Notes**

Install all dependencies from :

pip install -r requirements.txt, make sure pip belongs to your virtualenv python
