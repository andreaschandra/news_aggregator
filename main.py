import domain
import bintang

for url in domain.bintang_list:
	bintang.pull_data_bintang(url, 2, 1)
