import header

def pull_data_liputan6(domain, pagination, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        for j in range(1, pagination):
            url = domain + date_current.strftime('%Y/%m/%d') + '?page=' + str(j)
            print(url)
            
            #Get article from website
            req = header.http.request('GET', url)
            soup = header.BeautifulSoup(req.data, 'lxml')
            
            try:
                container = soup.find('div', attrs={'class':'articles--list articles--list_rows'})
            except:
                print('container not found')
                break
                
            try:
                boxes = container.find_all('article')
            except:
                print('box not found')
                break

            for i in range(0, len(boxes)):
                box = container.find_all('article')[i]
                
                #Get Title Article
                try:
                    title = box.find('h4').text
                except:
                    print('h4.text not found')
                    break
                    
                #Get Image
                try:
                    image = box.find('img').get('src')
                except:
                    print('image not found')
                    break

                #Get URL Article
                try:
                    url_box = box.find('figure', attrs={'class': 'articles--rows--item__figure-thumbnail'})
                    url = url_box.find('a').get('href')
                except:
                    print('href not found')
                    break
                    
                #Get Date
                date = date_current
                
                header.insert(title, image, url, date)
                
    return "done"