import urllib3
import certifi
import re
import connection
import mysql.connector as sql
from datetime import date, timedelta, datetime
from bs4 import BeautifulSoup

#Connection and urllib3
http = urllib3.PoolManager()

def generate_date(prev_date):
    date_list = []
    for i in range(0, prev_date):
        tanggal = date.today() - timedelta(i)
        date_list.append(tanggal)
    
    return date_list

def insert(title, image, url, date):
    db_connection = sql.connect(host='127.0.0.1', database='news_aggregator', user='root', password='')
    cursor = db_connection.cursor()
    
    #Try Except
    try:
        data_table = ("INSERT INTO data (TITLE, IMAGE, URL, DATE) VALUES (%s, %s, %s, %s)")
        data_value = (title, image, url, date)

        cursor.execute(data_table, data_value)
        db_connection.commit()
        
    except sql.IntegrityError:
        print('duplicate entry')
        
    cursor.close()
    db_connection.close()