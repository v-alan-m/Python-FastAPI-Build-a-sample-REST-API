# Build a Sample Python REST API using FastAPI
A sample REST API using FastAPI with python

Script for when the input is done using query parameters (main_item_str.py)

To run the app run:
uvicorn main_item_str:app --reload --no-use-colors

Curl test request example:

Add items:
curl -X POST "http://127.0.0.1:8000/items?item=apple"
["apple"]
curl -X POST "http://127.0.0.1:8000/items?item=orange"
["apple","orange"]

Get items:
curl -X GET "http://127.0.0.1:8000/items/0"
"apple"
curl -X GET "http://127.0.0.1:8000/items/1"
"orange"
curl -X GET "http://127.0.0.1:8000/items/2"
{"detail":"Item 2 not found"}
curl -X GET "http://127.0.0.1:8000/items?limit=2"
["apple","orange"]
curl -X GET "http://127.0.0.1:8000/items?limit=4"
["apple","orange"]


Script for when the input is done using a Pydantic type-object by using JSON input (main_item_object.py)

To run the app run:
uvicorn main_item_object:app --reload --no-use-colors

Curl test request example:

Add items:
curl -X POST -H "Content-Type: application/json" -d '{"text":"apple"}' "http://127.0.0.1:8000/items"

Get items: