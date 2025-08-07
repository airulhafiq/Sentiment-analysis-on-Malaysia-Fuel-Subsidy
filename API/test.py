# import requests

# comment = "im a robot"
# url = "http://127.0.0.1:8000/predict"
# payload = {"comment": comment}
# response = requests.post(url, json=payload)
# print("Sentiment:", response.json()["sentiment"])


# import requests

# response = requests.post(
#     "http://127.0.0.1:8000/predict",
#     json={"comment": "He just read book"}
# )

# print(response.json())

import requests

payload = {"comment": "He dont like book"}
response = requests.post("http://127.0.0.1:8000/predict", json=payload)

print(response.status_code)
print(response.json())
