# 🚀 Build a Sample Python REST API using FastAPI

A simple example project demonstrating how to build a REST API using [FastAPI](https://fastapi.tiangolo.com/) in Python.

---

## 📄 Script 1 — Using Query Parameters (`main_item_str.py`)

### ▶️ Run the App

```bash
uvicorn main_item_str:app --reload --no-use-colors
```

### 🧪 Curl Test Examples

#### ➕ Add Items

[Input]:

```bash
curl -X POST "http://127.0.0.1:8000/items?item=apple"
```

[Output]:

```json
["apple"]
```

[Input]:

```bash
curl -X POST "http://127.0.0.1:8000/items?item=orange"
```

[Output]:

```json
["apple", "orange"]
```

#### 📦 Get Items by Index

[Input]:

```bash
curl -X GET "http://127.0.0.1:8000/items/0"
```

[Output]:

```json
"apple"
```

[Input]:

```bash
curl -X GET "http://127.0.0.1:8000/items/1"
```

[Output]:

```json
"orange"
```

[Input]:

```bash
curl -X GET "http://127.0.0.1:8000/items/2"
```

[Output]:

```json
{"detail":"Item 2 not found"}
```

#### 📜 Get Items with Limit

[Input]:

```bash
curl -X GET "http://127.0.0.1:8000/items?limit=2"
```

[Output]:

```json
["apple", "orange"]
```

[Input]:

```bash
curl -X GET "http://127.0.0.1:8000/items?limit=4"
```

[Output]:

```json
["apple", "orange"]
```

---

## 📄 Script 2 — Using Pydantic Object with JSON Input (`main_item_object.py`)

### ▶️ Run the App

```bash
uvicorn main_item_object:app --reload --no-use-colors
```

### 🧪 Curl Test Example

#### ➕ Add Items

[Input]:

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"text\":\"apple\"}" "http://127.0.0.1:8000/items"
```

#### 📦 Get Items

[Input]:

```bash
curl -X GET "http://127.0.0.1:8000/items"
```

[Output]:

```json
[{"text":"apple","is_done":false}]
```

[Input]:

```bash
curl -X GET "http://127.0.0.1:8000/items?limit=3"
```

[Output]:

```json
[{"text":"apple","is_done":false}]
```

## 📄 View the Endpoints in an Interactive page documentation (Swagger page)

### ▶️ Acces the Swagger Page

[Input]:

```bash
127.0.0.1/docs/```