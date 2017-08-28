import header

def pull_data_kapanlagi(domain, pagination):
    
    for j in range(1, pagination):
        if j == 1:
            url = domain + '.html'
        else:
            url = domain + str(j) + '.html'
        print(url)

        
        #Get article from website
        req = header.https.request('GET', url)
        soup = header.BeautifulSoup(req.data, 'lxml')
        
        try:
            container = soup.find('div', attrs={'class':'artikel-detail-flat'})
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
                print('title not found')
                break
                
            #Get Image
            try:
                image = box.find('img').get('src')
            except:
                print('image not found')

            #Get URL Article
            try:
                url = 'https://kapanlagi' + box.find('a').get('href')
            except:
                print('href not found')
                break
                
            #Get Date
            date = header.date.today()
            
            header.insert(title, image, url, date)
                
    return "done"

def pull_data_kapanlagi_video(domain, pagination):
    
    for j in range(1, pagination):
        if j == 1:
            url = domain + '.html'
        else:
            url = domain + str(j) + '.html'
        print(url)

        
        #Get article from website
        req = header.https.request('GET', url)
        soup = header.BeautifulSoup(req.data, 'lxml')
        
        try:
            container = soup.find('div', attrs={'id':'v6-tags-populer'})
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
                box_title = box.find('div', attrs={'class': 'desc'})
                title = box_title.find_all('a', attrs={})[1].text
            except:
                print('title not found')
                break
                
            #Get Image
            try:
                image = box.find('img').get('src')
            except:
                print('image not found')

            #Get URL Article
            try:
                url = box.find('a').get('href')
            except:
                print('href not found')
                break
                
            #Get Date
            date = header.date.today()
            
            header.insert(title, image, url, date)
                
    return "done"