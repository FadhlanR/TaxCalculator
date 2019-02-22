**Tax Calculator API**
----
  For using this api, please follow this step:
  1. You have to clone this repo first.
  2. Start server with docker command "docker-compose up".
  3. Wait 15 seconds.
  4. Then you can use postman for request to this API.
  4. Example of request and response can you see in section below.

  If you want to run test case, please follow this step:
  1. Start server with docker command "docker-compose up -d".
  2. Wait 15 seconds.
  3. Type "docker-compose exec django bash".
  4. And then "python manage.py test --keepdb".

**API Example**
----
**Sign Up User**

* **URL**
    http://localhost:8000/user/signup

* **Method:**
  `POST`
  
*  **URL Params**
    all param is required
    ```json
    {
	    "name": "Fadhlan Ridhwanallah",
	    "handphone": "089658825175",
	    "password": "password"
    }
    ```

* **Success Response:**
  * **Code:** 200 <br />
    **Content:** 
    ```json
        {}```
 
* **Error Response:**
  * **Code:** 404 <br />
    **Content:** `{ message : "Password must not blank" }`

**Sign In User**

* **URL**
    http://localhost:8000/user/signin

* **Method:**
  `POST`
  
*  **Data Params**
    all param is required
    ```json
    {
	    "handphone": "089658825175",
	    "password": "password"
    }
    ```

* **Success Response:**
  * **Code:** 200 <br />
    **Content:** 
    ```json
    {
        "user_id": "d7ef0752-367c-11e9-a0bc-0242ac150003",
        "name": "Fadhlan Ridhwanallah",
        "handphone": "089658825175"
    }```
 
* **Error Response:**
  * **Code:** 404 <br />
    **Content:** `{ message : "Password is not valid" }`

**Create Tax Object**

* **URL**
    http://localhost:8000/user/{user_id}/tax/insert

    example: http://localhost:8000/user/d7ef0752-367c-11e9-a0bc-0242ac150003/tax/insert

* **Method:**
  `POST`
  
*  **Data Params**
    all param is required
    ```json
    {
	    "tax_code": 3,
	    "name": "Movie",
	    "price": "100"
    }
    ```

* **Success Response:**
  * **Code:** 200 <br />
    **Content:** 
    ```json
    {
        "tax_id": "5c6ef690-367d-11e9-a0bc-0242ac150003",
        "name": "Movie",
        "tax_code": 3,
        "type": "entertainment",
        "refundable": "No",
        "price": 100,
        "tax": 0,
        "amount": 100
    }```
 
* **Error Response:**
  * **Code:** 404 <br />
    **Content:** `{ message : "ORMUser matching query does not exist." }`

**Get Tax Calculation**

* **URL**
    http://localhost:8000/user/{user_id}/tax/insert

    example: http://localhost:8000/user/d7ef0752-367c-11e9-a0bc-0242ac150003/tax/get

* **Method:**
  `GET`
  
*  **Data Params**

* **Success Response:**
  * **Code:** 200 <br />
    **Content:** 
    ```json
    {
        "tax_object": [
            {
                "tax_id": "5c6ef690-367d-11e9-a0bc-0242ac150003",
                "name": "Movie",
                "tax_code": 3,
                "type": "entertainment",
                "refundable": "No",
                "price": 100,
                "tax": 0,
                "amount": 100
            },
            {
                "tax_id": "c21e0dbe-367d-11e9-a0bc-0242ac150003",
                "name": "Big Mac",
                "tax_code": 1,
                "type": "entertainment",
                "refundable": "No",
                "price": 1000,
                "tax": 9,
                "amount": 1009
            }
        ],
        "price_sub_total": 1100,
        "tax_sub_total": 9,
        "grand_total": 1109
    }```
 
* **Error Response:**
  * **Code:** 404 <br />
    **Content:** `{ message : "ORMUser matching query does not exist." }`