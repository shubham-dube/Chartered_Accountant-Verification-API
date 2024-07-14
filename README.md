# Chartered Accountant Verification API

This API fetches Chartered Accountant Details with their Membership Number in JSON format

## Table of Contents

- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Endpoints](#EndPoints)
- [Support](#Support)
- [Contribution](#Contribution)

## Features
- It Needs only Membership Number to check their Details.
- Returns the CA Details along with their Personal Details also.
- Easy to integrate in any of your application.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shubham-dube/Chartered_Accountant-Verification-API.git
   cd Chartered_Accountant-Verification-API
   
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate # On Linux use `source venv/bin/activate`
   
3. Install the dependencies:
   ```bash
   pip install flask requests bs4 html

4. Run the Application:
   ```bash
   python app.py
 *The API will be available at http://127.0.0.1:5000.*
 
## Usage
- Show the Membership Number input Field to the user.
- Send the entered Membership Number to the given endpoint acc. to request body.
- You will get all the details of CA with Membership Number in the JSON format.
  
## EndPoints

### Fetching CA Details

**Endpoint:** `/api/v1/getCADetails`

**Method:** `POST`

**Description:** `This Endpoint takes only the Mempership Number as Payload and return the full data of that Chatered Accountant holding that Membership Number.`

**Request Body:**
```json
{
    "membershipNumber": 558360
}
```
**Response**
```json
{
    "COPStatus": "NO COP",
    "associateYear": "A2020",
    "fellowYear": "",
    "foreignAddress": "NOT APPLICABLE      ",
    "gender": "M",
    "indianAddress": "WZ-127 BASAI DARA PUR   NEW DELHI 110015",
    "membershipNumber": 558360,
    "name": "TYAGI VISHAL , ACA",
    "qualification": "",
    "regionInIndia": ""
}
```
**Status Codes**
- 200 OK : `Details Recieved`

## Support
For Support Contact me at itzshubhamofficial@gmail.com
or Mobile Number : `+917687877772`

## Contribution

We welcome contributions to improve this project. Here are some ways you can contribute:

1. **Report Bugs:** If you find any bugs, please report them by opening an issue on GitHub.
2. **Feature Requests:** If you have ideas for new features, feel free to suggest them by opening an issue.
3. **Code Contributions:** 
    - Fork the repository.
    - Create a new branch (`git checkout -b feature-branch`).
    - Make your changes.
    - Commit your changes (`git commit -m 'Add some feature'`).
    - Push to the branch (`git push origin feature-branch`).
    - Open a pull request.

4. **Documentation:** Improve the documentation to help others understand and use the project.
5. **Testing:** Write tests to improve code coverage and ensure stability.

Please make sure your contributions adhere to our coding guidelines and standards.
