import header

def pull_data_hipwee(domain, pagination):
    
    for i in range(1, pagination):
        url = domain + str(i)
        print(url)

        #Get article from website
        req = header.http.request('GET', url)
        soup = header.BeautifulSoup(req.data, 'lxml')
        
        try:
            archive = soup.find('div', attrs={'class': 'archive-post'})
        except:
            print('archive not found')
            break
            
        try:
            containers = archive.find_all('div', attrs={'class':'row'})
        except:
            print('container not found')
            break

        for cont in range(0, len(containers)):
            container = soup.find_all('div', attrs={'class':'row'})[cont]

            try:
                boxes = container.find_all('div', attrs={'class': 'col-sm-4'})
            except:
                print('box not found')
                break

            for bo in range(0, len(boxes)):
                box = container.find_all('div', attrs={'class': 'col-sm-4'})[bo]

                #Get Title Article
                try:
                    title = box.find('h2').text
                except:
                    print('h2.text not found')
                    break

                #Get Image
                try:
                    image = box.find('img').get('data-src')
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
                today = header.date.today()

                header.insert(title, image, url, today)

    return "done"