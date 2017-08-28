import header

def pull_data_jalantikus(domain, pagination):
    
    for j in range(1, pagination):
        url = domain + str(j) + '/'
        print(url)

        #Get article from website
        req = header.https.request('GET', url)
        soup = header.BeautifulSoup(req.data, 'lxml')

        try:
            container = soup.find('div', attrs={'class':'content-list'})
        except:
            print('container not found')
            break

        try:
            boxes = container.find_all('div', attrs={'class': 'article-detail horizontal mSz cf mainspring-track'})
        except:
            print('box not found')
            break

        for i in range(0, len(boxes)):
            box = container.find_all('div', attrs={'class': 'article-detail horizontal mSz cf mainspring-track'})[i]

            #Get Title Article
            try:
                title = box.find('span', attrs={'class': 'title-text fs1 lSz text-link cl1 trs entry-title'}).text
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
            tanggal = header.date.today()
            
            header.insert(title, image, url, tanggal)