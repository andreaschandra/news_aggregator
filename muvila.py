import header

def pull_data_muvila(domain, pagination):
    
    for pag in range(1, pagination):
        if pag == 1:
            url = domain + '.html'
        else:
            url = domain + str(pag) + '.html'
        print(url)

        #Get article from website
        req = header.http.request('GET', url)
        soup = header.BeautifulSoup(req.data, 'lxml')

        try:
            container = soup.find('ul', attrs={'class':'list-article-left detail-section list-unstyled clearfix'})
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
                title = box.find('h6').text
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
                if 'entertainment' in url:
                    dateraw = box.find('span', attrs={'class': 'date'}).text
                    datestring = header.re.sub(r""" [0-9]{2}:[0-9]{2}""", '', dateraw)
                    datearr = datestring.split(' ')

                    for key in datearr:
                        if datearr[1] in key:
                            datearr[1] = header.month[key]

                    datestr = '/'.join(d for d in datearr)
                    date = header.datetime.strptime(datestr, '%d/%m/%Y')
                else:
                    dateraw = box.find('span', attrs={'class': 'date'}).text
                    datestring = header.re.sub(r""" \| | [0-9]{2} : [0-9]{2}""", '', dateraw)
                    datearr = datestring.split(' ')

                    for key in datearr:
                        if datearr[1] in key:
                            datearr[1] = header.month[key]

                    datestr = '/'.join(d for d in datearr)
                    date = header.datetime.strptime(datestr, '%d/%m/%Y')
            except:
                print('date not found')
                break
                    
            header.insert(title, image, url, date)