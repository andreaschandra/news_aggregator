import header

def pull_data_tirto(domain, pagination, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        for j in range(1, pagination):
            url = domain + str(j) + '?date=' + date_current.strftime('%Y-%m-%d')
            print(url)
            
            #Get article from website
            req = header.https.request('GET', url)
            soup = header.BeautifulSoup(req.data, 'lxml')
            
            try:
                container = soup.find('ul', attrs={'class':'media-list main-list'})
            except:
                print('container not found')
                break
                
            try:
                boxes = container.find_all('li', attrs={'class': 'media'})
            except:
                print('box not found')
                break

            for i in range(0, len(boxes)):
                box = container.find_all('li', attrs={'class': 'media'})[i]
                
                #Get Title Article
                try:
                    title = box.find('h4').text
                except:
                    print('h2.text not found')
                    break
                    
                #Get Image
                image = ""

                #Get URL Article
                try:
                    url = 'https:' + box.find('a').get('href')
                    
                    if url == 'https://tirto.id/suara-pembaca':
                        break
                except:
                    print('href not found')
                    break
                    
                #Get Date
                date = date_current
                
                header.insert(title, image, url, date)
                
    return "done"