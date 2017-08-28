import header

def pull_data_kumparan(domain, pagination):
    
    for j in range(1, pagination):
        url = domain + str(j)
        print(url)

        #Get article from website
        req = header.https.request('GET', url)
        jsondata = header.json.loads(req.data)
        results = jsondata['results']
        
        for i in range(0, len(results)):
            
            #Get Title Article
            try:
                title = results[i]['title']
            except:
                print('title not found')
                break

            #Get Image
            try:
                image = results[i]['lead_media']['urls'][0]
            except:
                print('image not found')
                break

            #Get URL Article
            try:
                url = 'https://kumparan.com/' + results[i]['author']['username'] + '/' + results[i]['slug']
            except:
                print('href not found')
                break
                
            #Get Date
            try:
                dateraw = results[i]['date']['publish']
                date = dateraw[:10]
            except:
                print('date not found')
                break

            header.insert(title, image, url, date)
                
    return "done"