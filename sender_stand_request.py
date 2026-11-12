import requests
from configuration import BASE_URL, CREATE_ORDER_PATH

def create_order(post_body):
    url = BASE_URL + CREATE_ORDER_PATH
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(
        url=url,
        json=post_body,
        headers=headers
    )
    return response
def get_order_by_track(track):
    url = BASE_URL + GET_ORDER_BY_TRACK_PATH
    params = {"t": track}
    response = requests.get(url, params=params)
    return response