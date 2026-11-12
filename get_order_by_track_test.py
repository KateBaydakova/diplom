from sender_stand_request import create_order, get_order_by_track
from data import order_data

def test_get_order_by_track():
    # 1. Создать заказ
    create_response = create_order(order_data)
    assert create_response.status_code == 201

    # 2. Сохранить номер трека
    track = create_response.json()["track"]

    # 3. Получить заказ по треку
    get_response = get_order_by_track(track)

    # 4. Проверить код ответа
    assert get_response.status_code == 200