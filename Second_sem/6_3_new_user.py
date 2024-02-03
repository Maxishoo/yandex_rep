import requests

address = "http://" + input() + "/users/" + input()
requests.delete(address)
