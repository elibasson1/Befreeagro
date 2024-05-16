**BeeFreeAgro API**

**Description**

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

**Usage**

- You can use the provided Python scripts to interact with the BeeFreeAgro API.

**Test Files**

1. **test\_droneModel.py**

This file contains tests for the **get\_getDroneByModel** endpoint of the BeeFreeAgro API.

**Tests:**

- test\_droneModelExists:  Tests if a drone model exists and returns a status code of 200.
- test\_droneModelNotExists: Tests if a non-existing drone model returns a status code of 404.

**2. test\_imageDrone.py**

This file contains tests for the get\_getDroneByImage endpoint of the BeeFreeAgro API.

**Tests**:

- test\_getDroneByImage: Tests if the drone image can be retrieved correctly and compares it with the expected image.

**3. test\_listOfDrones.py**

This file contains tests for the get\_getAllDrones endpoint of the BeeFreeAgro API.

**Tests**:

- test\_dronesKeys: Tests if the response contains expected keys.
- test\_dataType: Tests if the data types of the response are as expected.
- test\_dronesCount: Tests if the number of drones returned is as expected.

**Running Tests**

Since this project operates within a virtual environment using Python, follow these steps to execute the tests:

1. Open your command prompt (**CMD**).
1. Navigate to the directory named **Beefree**  
1. Choose the directory **.venv\Scripts** 
1. Run the command **activate.bat**.
1. Return to the directory **Beefree\Tests**
1. Execute the command **pytest -v -s**

**Notes**

**Install all dependencies from it: pip install -r requirements.txt, make sure pip belongs to your virtualenv python other than OS default pip**
