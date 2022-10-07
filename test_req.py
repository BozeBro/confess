import requests
if __name__ == "__main__":
    data = {"confessions" : ["I like peanuts", "YOLO", "LOREM IPSUM IS THE BEST CHEESE"]}
    r = requests.post("http://localhost:8080/get_image", json=data)
    print(r.json())

