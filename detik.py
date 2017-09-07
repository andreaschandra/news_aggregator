import header

def pull_data_news_detik(domain, pagination, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        for j in range(1, pagination):
            url = domain + str(j) + '?date=' + date_current.strftime('%m/%d/%Y')
            print(url)
            
            #Get article from website
            req = header.https.request('GET', url)
            soup = header.BeautifulSoup(req.data, 'lxml')
            
            try:
                container = soup.find('ul', attrs={'id':'indeks-container'})
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
                    title = box.find('h2').text
                except:
                    print('h2.text not found')
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

def pull_data_finance_detik(domain, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        url = domain + '?date=' + date_current.strftime('%m/%d/%Y')
        print(url)

        #Get article from website
        req = header.https.request('GET', url)
        soup = header.BeautifulSoup(req.data, 'lxml')

        try:
            container = soup.find('div', attrs={'class':'lf_content boxlr w868 fr ml10'})
        except:
            print('container not found')
            break
        
        try:
            container = container.find('ul')
        except:
            print('container 2 not found')
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
                title = box.find('h2').text
            except:
                print('h2.text not found')
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

def pull_data_inet_detik(domain, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        url = domain + '?date=' + date_current.strftime('%m/%d/%Y')
        print(url)

        #Get article from website
        req = header.https.request('GET', url)
        soup = header.BeautifulSoup(req.data, 'lxml')

        try:
            container = soup.find('ul', attrs={'class':'list feed'})
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
                title = box.find('h2').text
            except:
                print('h2.text not found')
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

def pull_data_oto_detik(domain, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        url = domain + '?date=' + date_current.strftime('%m/%d/%Y')
        print(url)

        #Get article from website
        req = header.https.request('GET', url)
        soup = header.BeautifulSoup(req.data, 'lxml')

        try:
            container = soup.find('div', attrs={'class':'lf_content fl w870'})
        except:
            print('container not found')
            break
            
        try:
            container = container.find('ul')
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
                title = box.find('h2').text
            except:
                print('h2.text not found')
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

def pull_data_travel_detik(domain, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        url = domain + '?date=' + date_current.strftime('%m/%d/%Y')
        print(url)

        #Get article from website
        req = header.https.request('GET', url)
        soup = header.BeautifulSoup(req.data, 'lxml')

        try:
            container = soup.find('section', attrs={'class':'list__news no-img'})
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
                title = box.find('h3').text
            except:
                print('h2.text not found')
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

def pull_data_hot_sport_sb_detik(domain, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        url = domain
        print(url)

        #Get article from website
        req = header.https.request('POST', 
                           url, 
                           fields={'datepick': date_current.strftime('%m/%d/%Y')}
                          )
        soup = header.BeautifulSoup(req.data, 'lxml')

        try:
            container = soup.find('ul', attrs={'id':'indeks-container'})
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
                title = box.find('h2').text
            except:
                print('h2.text not found')
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

def pull_data_food_health_detik(domain, duration):
    date = header.generate_date(duration)
    for date_current in date:
        url = domain
        print(url)

        #Get article from website
        req = header.https.request('POST', 
                           url, 
                           fields={'tgl': date_current.strftime('%d'),
                                   'bln': date_current.strftime('%m'),
                                   'thn': date_current.strftime('%Y')}
                          )
        soup = header.BeautifulSoup(req.data, 'lxml')

        try:
            containers = soup.find_all('ul', attrs={'class':'list_indeks'})            
        except:
            print('container not found')
            break
        
        for cont in range(0, len(containers)):
            try:
                container = soup.find_all('ul', attrs={'class':'list_indeks'})[cont]
            except:
                print('list_index not found at' + str(cont))
        
            try:
                boxes = container.find_all('li')
            except:
                print('box not found')
                break

            for i in range(0, len(boxes)):
                box = container.find_all('li')[i]

                #Get Title Article
                try:
                    title = box.find('a').text
                except:
                    print('a.text not found')
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

def pull_data_wolipop_detik(domain, duration):
    date = header.generate_date(duration)
    for date_current in date:
        url = domain
        print(url)

        #Get article from website
        req = header.https.request('POST', 
                           url, 
                           fields={'tgl': date_current.strftime('%d'),
                                   'bln': date_current.strftime('%m'),
                                   'thn': date_current.strftime('%Y')}
                          )
                          
        soup = header.BeautifulSoup(req.data, 'lxml')

        kiri = soup.find('div', attrs={'class': 'kiri'})

        try:
            containers = kiri.find_all('ul', attrs={'class':'listnews4'})            
        except:
            print('container not found')
            break
        
        for cont in range(0, len(containers)):
            try:
                container = soup.find_all('ul', attrs={'class':'listnews4'})[cont]
            except:
                print('container not found at' + str(cont))
        
            try:
                boxes = container.find_all('li')
            except:
                print('box not found')
                break

            for i in range(0, len(boxes)):
                box = container.find_all('li')[i]

                #Get Title Article
                try:
                    title = box.find('h6').text
                except:
                    print('a.text not found')
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