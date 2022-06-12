import requests
from .models import Data
from multiprocessing import cpu_count, Pool
from concurrent.futures import ThreadPoolExecutor

def fetch_links():
    data_lst = []
    url = "https://v1.nocodeapi.com/pocopes373game4hr/instagram/dVeQbYMnCPlMxNnL"
    res = requests.get(url = url)
    for data in res.json()["data"]:
        data_lst.append([data["media_url"], data["timestamp"]])
    return data_lst

def link_exists_or_not(link):
    try:
        Data.objects.get(link=link)
    except Exception:
        return False
    return True

def add_data(data):
    if not link_exists_or_not(data[0]):
        url = "http://127.0.0.1:8000/links/add/"
        requests.post(url, json={"link": data[0], "timestamp": data[1]})

# multiprocessing (personally preferred)
def main():
    with Pool(cpu_count()) as p:
        p.map(add_data, fetch_links())

# multithreading
# def main():
#     data = fetch_links()
#     with ThreadPoolExecutor(max_workers=len(data)) as exe:
#         exe.map(add_data, data)
