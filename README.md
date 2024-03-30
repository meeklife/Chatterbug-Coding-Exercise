# Password Generator API

This is a simple REST API's built using FastAPI that allows users to generate secure passwords based on specified criteria and also that allows you to get the public, local, religious, and other holidays of a particular country.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/meeklife/Chatterbug-Coding-Exercise.git
```

2. Navigate to the project directory:

```bash
cd Chatterbug-Coding-Exercise
```

3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

4. Run the FastAPI application using uvicorn:

```bash
uvicorn main:app --reload
```

## Usage - Password Generator

To generate a password, send a POST request to the /generate-password endpoint with a JSON payload containing the desired length of the password and two criterias the password should contain (criteria1, criteria2)

```json
{
  "length": 12,
  "criteria1": "58CR8T",
  "criteria2": "4noth8r"
}
```

You can use tools like Postman or curl to send the request. Here's an example using curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"length": 16, "criteria1": "MYSEcretKEy", "criteria2": "AnotherSecret" }' http://localhost:8000/generate-password
```

Replace 16 with the desired length of the password. The API will respond with a JSON object containing the generated password and the specified length:

```json
{
  "password": "S(cM4$[5$^*KS|@,",
  "length": 16
}
```

That's it! You have successfully setup and used the Password Generator API.

## Usage - Holidays

To search a holiday, send a GET request to the /get_holiday endpoint with a query string of a two letter country code, also specify the day, month, or year. The API will return the public holidays for that country.

```json
{
  "country": "GB",
  "year": "2024",
  "month": "12",
  "day": "25"
}
```

You can use tools like Postman or curl to send the request. Here's an example using curl:

```bash
curl -X GET "http://localhost:8000/api/holiday?country=GB&year=2024&month=12&day=25"
```

Replace with the desired country and date. The API will respond with a JSON object containing the holiday information

```json
{
  "name": "Christmas Day",
  "name_local": "",
  "language": "",
  "description": "",
  "country": "GB",
  "location": "United Kingdom",
  "type": "National",
  "date": "12/25/2024",
  "date_year": "2024",
  "date_month": "12",
  "date_day": "25",
  "week_day": "Wednesday"
}
```
