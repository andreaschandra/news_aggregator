import header

def pull_data_tempo(domain, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        url = domain + date_current.strftime('%Y/%m/%d/')
        print(url)

        #Get article from website
        req = header.https.request('GET', url)
        soup = header.BeautifulSoup(req.data, 'lxml')

        try:
            container = soup.find('ul', attrs={'class':'wrapper'})
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
                url = box.find_all('a')[0].get('href')
            except:
                print('href not found')
                break

            #Get Date
            date = date_current

            header.insert(title, image, url, date)
                
    return "done"