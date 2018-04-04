import requests


# def test_server_sends_200_response():
#     response = requests.get('http://127.0.0.1:3020')
#     assert response.status_code == 200


def test_server_sends_404_response():
    response = requests.get('http://127.0.0.1:3020/not_a_thing')
    assert response.status_code == 404
    assert response.text == 'Not Found'


# def test_server_sends_200():
#     response = requests.get('http://127.0.0.1:3020/cowsay')
#     assert response.status_code == 200
#     assert response.text == '"messege about stuff"'


# def test_server_sends_qs_response():
#     response = requests.get('http://127.0.0.1:3020/cow?msg=meseegeback')
#     assert response.status_code == 200
#     assert response.text == '"meseegeback"'


# def test_server_json():
#     response = requests.post('http://127.0.0.1:3020/cow?msg=meseegeback')
#     assert response.status_code == 200
#     assert response.text == '"meseegeback"'
#     assert response.headers == '' 