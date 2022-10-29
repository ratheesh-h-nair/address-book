
# Address Book using Fast Api

The app contains the code to retrieve a person's address nearby and within a specific radius. 


## Tech Stack

**API:** Python Fast API

**Database:** SQLite



## Installation

Clone the repository to the desired location

```bash
  git clone https://github.com/ratheesh-h-nair/address-book.git
```

## API Reference

#### Filter based on the locations

```http
  POST /api/v1/address/list
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `coordinates` | `array` | **Required**. |
| `distance` | `integer` | **Required**. |

#### Get item

```http
  POST /api/v1/address/create
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Id of item to fetch |
| `email`      | `string` | **Required**. Id of item to fetch |
| `address`      | `string` | **Required**. Id of item to fetch |
| `phone`      | `string` | **Required**. Id of item to fetch |
| `coordinates`      | `array` | **Required**. Id of item to fetch |



## Running Tests

To run tests, run the following command
```bash
  uvicorn main:app --reload
```


Application Starts Running under the port - 8000
```bash
  http://127.0.0.1:8000
```


## Free to hear! Thank You!
