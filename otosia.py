import header

def pull_data_otosia(domain, pagination):
    
    for j in range(1, pagination):
        if j == 1:
            url = domain + '.html'
        else:
            url = domain + str(j) +'.html'
        print(url)
        
        #Get article from website
        req = header.https.request('GET', url)
        soup = header.BeautifulSoup(req.data, 'lxml')

        try:
            container = soup.find('div', attrs={'id':'mobart-box-big'})
        except:
            print('container not found')
            break

        try:
            boxes = container.find_all('div', attrs={'class': 'article-index-box'})
        except:
            print('box not found')
            break

        for i in range(0, len(boxes)):
            box = container.find_all('div', attrs={'class': 'article-index-box'})[i]

            #Get Title Article
            try:
                title = box.find('h2').text
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
                url = 'https://www.otosia.com/' + box.find('a').get('href')
            except:
                print('href not found')
                break

            #Get Date
            try:
                dateraw = box.find('span', attrs={'class': 'newsdetail-schedule'}).text
                datestring = header.re.sub(r""".*, | [0-9]{2}:[0-9]{2}""", '', dateraw)
                datearr = datestring.split(' ')
                
                for key in header.month:
                    if datearr[1] in key:
                        datearr[1] = header.month[key]
                        
                datestr = '/'.join(d for d in datearr)
                date = header.datetime.strptime(datestr, '%d/%m/%Y')
            except:
                print('date not found')
                break
                    
            header.insert(title, image, url, date)

    return "done"