import requests

res = requests.get("https://www.learn-drl.com")
for chunk in res.iter_content(chunk_size=100):
    print(chunk)