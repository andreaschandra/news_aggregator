import header

def pull_data_cnn(domain, pagination, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        for j in range(1, pagination):
            url = domain + '?page=' + str(j) + '&date=' + date_current.strftime('%Y-%m-%d')
            print(url)
    
            #Get article from website
            req = header.https.request('GET', url)
            soup = header.BeautifulSoup(req.data, 'lxml')
            
            try:
                container = soup.find('ul', attrs={'class':'list_indeks'})
            except:
                print('container not found')
                break
                
            try:
                boxes = container.find_all('li')
            except:
                print('box not found')
                break

            for i in range(0, len(boxes)):
                box = container.find_all('li')[i]
                
                #Get Title Article
                try:
                    title = box.find('h3').text
                except:
                    print('h2.text not found')
                    break
                    
                #Get Image
                try:
                    image = box.find('img').get('src')
                except:
                    print('image not found')
                    break

                #Get URL Article
                try:
                    url = box.find('a').get('href')
                except:
                    print('href not found')
                    break
                    
                #Get Date
                try:
                    dateraw = box.find('span', attrs={'class': 'date'}).text
                    date_re = header.re.sub('.*, | [0-9]{2}:[0-9]{2}','',dateraw)
                    date = header.datetime.strptime(date_re, '%d/%m/%Y')
                except:
                    print('date not found')
                    break
                    
                header.insert(title, image, url, date)