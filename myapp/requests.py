import requests as requests


# {
#  "origin": "xxx.xxx.xxx.xxx"
# }
def get_my_ip() -> str:
    response = requests.get("https://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()["origin"]
