import header

def pull_data_okezone(domain, pagination, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        for j in range(0, pagination, 15):
            url = domain + date_current.strftime('%Y/%m/%d/') + str(j)
            print(url)
            
            #Get article from website
            req = header.http.request('GET', url)
            soup = header.BeautifulSoup(req.data, 'lxml')
            
            try:
                container = soup.find('div', attrs={'class':'d638 bg1 b1 fl r1 p3'})
            except:
                print('container not found')
                break
                
            try:
                container = container.find('ol')
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
                    title = box.find('h4').text
                except:
                    print('h4.text not found')
                    break
                    
                #Get Image
                image = ""

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