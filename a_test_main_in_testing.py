from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_one_student():
    response = client.get("/students/1")
    assert response.status_code == 200

    assert response.json()["id"] == 1
    assert response.json()["name"] == "John"
    assert response.json()["age"] == 20


def test_student_not_found():
    response = client.get("/students/100")
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"


def test_create_item(client):
    item_data = {"name": "Laptop", "price": 50000, "in_stock": True}
    response = client.post("/item", json=item_data)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Laptop"
    assert data["price"] == 50000
    assert data["in_stock"] is True


def test_create_item_invalid_data(client):
    item_data = {"name": "Laptop", "in_stock": True}
    response = client.post("/item", json=item_data)
    assert response.status_code == 422


def test_Get_all_itmes(client):
    client.post("/item", json={"name": "Laptop", "price": 50000, "in_stock": True})
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Laptop"


def test_get_single_item(client):
    create_response = client.post(
        "/item", json={"name": "Mouse", "price": 500, "in_stock": True}
    )
    item_id = create_response.json()["id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["id"] == item_id
    assert response.json()["name"] == "Mouse"


def test_get_item_not_found(client):
    response = client.get("/items/854")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not fount, try again"


def test_update_item(client):
    create_response = client.post(
        "/item", json={"name": "Mouse", "price": 500, "in_stock": True}
    )
    item_id = create_response.json()["id"]

    updated_data = {"name": "Mouse updated", "price": 511, "in_stock": False}
    response = client.put(f"/item/{item_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Mouse updated"
    assert response.json()["price"] == 511
    assert response.json()["in_stock"] == False


def test_delete_item(client):
    create_response = client.post(
        "/item", json={"name": "Mouse", "price": 500, "in_stock": True}
    )
    item_id = create_response.json()["id"]
    response = client.delete(f"/item/{item_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted successfully"
    assert response.json()["id"] == item_id

    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404
