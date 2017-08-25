import header

def pull_data_bintang(domain, pagination, duration):
    
    date = header.generate_date(duration)
    for j in date:
        for i in range(1, pagination):
            url = domain + j.strftime('%Y/%m/%d') + '?page=' + str(i)
            print(url)

            req = header.http.request('GET', url)
            soup = header.BeautifulSoup(req.data, 'html.parser')

            try:
                container = soup.find('div', attrs={'class': 'articles--list articles--list_rows'})
            except:
                break

            try:
                box = container.find_all('article', attrs={'class': 'articles--rows--item'})
            except:
                print('article not found')
                break

            for i in range(0, len(box)):
                box_title = container.find_all('article', attrs={'class': 'articles--rows--item'})[i]

                #get title
                try:
                    titleraw = box_title.find('h4').text
                    strencode = titleraw.encode('utf-8')
                    title = header.re.sub(r'\\x[a-z0-9]{2}', '', str(strencode))
                except:
                    print('title not found')
                    break

                #get image
                image = box_title.find('img').get('src')

                #get url
                try:
                    url = box_title.find('a').get('href')
                except:
                    print('href not found')
                    next

                #get date
                date = j

                header.insert(title, image, url, date)
                        
    return "done"