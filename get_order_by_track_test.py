# Екатерина Байдакова, 49-я когорта — Финальный проект. Инженер по тестированию плюс
from sender_stand_request import create_order, get_order_by_track
from data import order_data

def test_create_order():
    response = create_order(order_data)
    assert response.status_code == 201
    assert "track" in response.json()

def test_get_order_by_track():
    create_response = create_order(order_data)
    track = create_response.json()["track"]

    response = get_order_by_track(track)
    assert response.status_code == 200