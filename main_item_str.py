from fastapi import FastAPI, HTTPException
from kill_old_ports_being_used import is_port_in_use, free_port_windows

app = FastAPI()

items = []


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/items")
def create_items(item: str):
    items.append(item)
    return items


@app.get("/items")
def list_items(limit: int = 10):
    return items[0:limit]


@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")


if __name__ == "__main__":
    print("Port 8000 is", "in use" if is_port_in_use(8000) else "available")
    free_port_windows(8000)
