import header

def pull_data_kompas(domain, pagination, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        for j in range(1, pagination):
            url = domain + str(date_current) + '/' + str(j)
            print(url)
    
            #Get article from website
            req = header.http.request('GET', url)
            soup = header.BeautifulSoup(req.data, 'lxml')
            
            try:
                container = soup.find('div', attrs={'class':'latest--indeks mt2 clearfix'})
            except:
                print('container not found')
                break
                
            try:
                boxes = container.find_all('div', attrs={'class': 'article__list clearfix'})
            except:
                print('box not found')
                break

            for i in range(0, len(boxes)):
                box = container.find_all('div', attrs={'class': 'article__list clearfix'})[i]
                
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
                date = date_current
                
                header.insert(title, image, url, date)

    return "done"