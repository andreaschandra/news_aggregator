# API Reference

## News Aggregator
	main.py
	header.py
	<domain>.py
	
	### main.py
	<website name>.pull_data_<website>(domain = domain.<domain name>, pagination = <number>, duration = <number>)
	
	method function names: pull_data_<website name>
			var: website_name can be change as:
				bintang
				cnn
				detik
					news_detik
					finance_detik
					inet_detik
					oto_detik
					travel_detik
					sport_sb_detik
					food_health_detik
					wolipop_detik
				kompas
				kumparan
				liputan6
				muvila
				okezone
				otosia
				techno
				tempo
				tirto
				tribunnews
				vemale
				
	pull_data_<website name>(domain, pagination, duration)
				
		parameters: domain
					pagination
					duration
	