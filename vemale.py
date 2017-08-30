import header

def pull_data_vemale(domain, pagination, duration):
    
    date = header.generate_date(duration)
    for date_current in date:
        for j in range(1, pagination):
            url = domain + 'index' + str(j) + '.html'
            print(url)
    
            #Get article from website
            req = header.https.request('GET', url)
            soup = header.BeautifulSoup(req.data, 'lxml')
            
            try:
                containers = soup.find_all('ul', attrs={'class':'list-article-latest list-unstyled clearfix'})
            except:
                print('container not found')
                break
                
            for cont in range(0, len(containers)):
                container = soup.find_all('ul', attrs={'class':'list-article-latest list-unstyled clearfix'})[cont]
                
                try:
                    box = container.find_all('li')
                except:
                    print('li not found')
                    break

                for i in range(0, len(box)):
                    box_title = container.find_all('li')[i]

                    #Get Title Article
                    try:
                        title = box_title.find('p').text
                    except:
                        print('p not found')
                        break

                    #Get Image
                    try:
                        image = box_title.find('img').get('src')
                    except:
                        print('image not found')
                        break

                    #Get URL Article
                    try:
                        url = box_title.find('a').get('href')
                    except:
                        print('href not found')
                        break

                    #Get Date
                    date = date_current

                    header.insert(title, image, url, date)

    return "Done"