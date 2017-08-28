import urllib3
import certifi
import re
import json
import MySQLdb as sql
from datetime import date, timedelta, datetime
from bs4 import BeautifulSoup

#Connection and urllib3
http = urllib3.PoolManager()
https = urllib3.PoolManager( cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

def generate_date(prev_date):
    date_list = []
    for i in range(0, prev_date):
        tanggal = date.today() - timedelta(i)
        date_list.append(tanggal)
    
    return date_list

def insert(judul, image, url, date):
    db_connection = sql.connect(host='127.0.0.1', database='news_aggregator', user='root', password='')
    cursor = db_connection.cursor()
    
    #Try Except
    if judul == None:
        print("title null")
    elif image == None:
        print("image null")
    elif url == None:
        print("url null")
    elif date == None:
        print("date null")

    try:
        cursor.execute("""INSERT INTO data (TITLE, IMAGE, URL, DATE) VALUES (%s, %s, %s, %s)""", (judul, image, url, date))
        db_connection.commit()
        
    except:
        print(url)
        print('duplicate entry')
        
    cursor.close()
    db_connection.close()

month = {'Januari': '01',
         'Februari': '02',
         'Maret': '03',
         'April': '04',
         'Mei': '05',
         'Juni': '06',
         'Juli': '07',
         'Agustus': '08',
         'September': '09',
         'Oktober': '10',
         'November': '11',
         'Desember': '12'
        }