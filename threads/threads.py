import requests
import threading
import concurrent.futures
import psycopg2
from pytube import YouTube
from dotenv import load_dotenv
import os
load_dotenv()

video_urls = [
    'https://youtu.be/1rZsW0IWdIs',
    'https://youtu.be/AbCO4lW0G60',
    'https://youtu.be/Fw0-51X0t8I',
    'https://youtu.be/dnnh8unDP4Y',
    'https://youtu.be/ZF-w__uUs8c'
]

dataUrl = []


def get_service_register(url):
    response = requests.get(url)
    if response.status_code == 200 :
        data = response.json()
        write_db(data)

def connect_db():
    conn = psycopg2.connect(
    host=os.getenv("HOST"),
    database=os.getenv("DATABASE"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"))
    print('Successful conection...')
    conn.autocommit = True
    return conn

def write_db(data):
    conn = connect_db()
    cur = conn.cursor()
    for dataOut in data:    
        title = dataOut['title']
        query = f""" INSERT INTO photostest (title) VALUES ('{title}') """
        cur.execute(query)
    print('Data saved successfully')
        

def get_services_names(dato=0):
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[dato].get('name').get('first')
        print(f'{dato+1}. {name}')

def get_videos(video_url):
    yt = YouTube(video_url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print(f'{video_url} was downloaded...')     
 
if __name__ == '__main__':
    url_site = ["https://jsonplaceholder.typicode.com/photos"]
    th1 = threading.Thread(target = get_service_register, args=url_site)
    th1.start()
    for dataUrl in video_urls:
        th2 = threading.Thread(target = get_videos, args = [dataUrl])
        th2.start()
    for x in range(0,50):
        th3 = threading.Thread(target = get_services_names, args = [x])
        th3.start()