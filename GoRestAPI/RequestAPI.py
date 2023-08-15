import json

import requests

from Utilities import Generic

base_url = "https://gorest.co.in"


# GET Request
def get_request():
    url = base_url + "/public/v2/users/"
    print("Get url: " + url)
    headers = {"Authorization": Generic.GenericPage.bearerToken()}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_string_get = json.dumps(json_data, indent=4)
    print("json response body:", json_data)
    print("json GET response body:", json_string_get)  # pretty format version
    print("GET user is done")
    print("**********************************************")


# POST Request
def post_request():
    url = base_url + "/public/v2/users/"
    print("Get url: " + url)
    headers = {"Authorization": Generic.GenericPage.bearerToken()}
    data = {
        "name": "Tech Automation",
        "email": Generic.GenericPage.generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_string_post = json.dumps(json_data, indent=4)
    print("json POST response body:", json_string_post)
    user_id = json_data["id"]
    print("User id ====>", user_id)
    assert response.status_code == 201
    assert "name" in json_data
    assert json_data["name"] == "Tech Automation"
    return user_id


# PUT Request
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("PUT url: " + url)
    headers = {"Authorization": Generic.GenericPage.bearerToken()}
    data = {
        "name": "Tech Automation Labs",
        "email": Generic.GenericPage.generate_random_email(),
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_string_put = json.dumps(json_data, indent=4)
    print("json PUT response body:", json_string_put)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Tech Automation Labs"
    assert json_data["gender"] == "male"
    print("PUT user is done")
    print("**********************************************")


# DELETE Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("DELETE url: " + url)
    headers = {"Authorization": Generic.GenericPage.bearerToken()}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("DELETE user is done")
    print("**********************************************")


# Call Requests
get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)
