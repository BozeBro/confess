import requests
# http://127.0.0.1:8080
# https://marine-alchemy-363921.uk.r.appspot.com/get_image
if __name__ == "__main__":
    data = {"confessions": ["I like peanuts", "YOLO", "LOREM IPSUM IS THE BEST CHEESE"]}
    r = requests.post("http://127.0.0.1:8080/get_image", json=data)
    print(r.json())
