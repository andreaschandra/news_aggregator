import domain
import bintang
import cnn
import detik
import hipwee
import jalantikus
import kapanlagi
import kompas
import kumparan

# for url in domain.bintang_list:
# 	bintang.pull_data_bintang(url, 2, 1)

# cnn.pull_data_cnn(domain.cnn, 2, 1)

# detik.pull_data_news_detik(domain.detik_news, 20, 2)
# detik.pull_data_finance_detik(domain.detik_finance, 2)
# detik.pull_data_inet_detik(domain.detik_inet, 2)
# detik.pull_data_oto_detik(domain.detik_oto, 2)
# detik.pull_data_travel_detik(domain.detik_travel, 1)

# for url in domain.detik_hot_sport_sepakbola_list:
#     detik.pull_data_hot_sport_sb_detik(url, 2)

# for url2 in domain.detik_food_health_list:
#     detik.pull_data_food_health_detik(url2, 2)

# detik.pull_data_wolipop_detik(domain.detik_wolipop, 2)

# hipwee.pull_data_hipwee(domain.hipwee, 5)

# for url_jt in domain.jalantikus_list:
#     jalantikus.pull_data_jalantikus(url_jt, 2)

# for url_kl in domain.kapanlagi_list:
#     kapanlagi.pull_data_kapanlagi(url_kl, 20)

# kapanlagi.pull_data_kapanlagi_video(domain.kapanlagi_video, 2)

# for url_komp in domain.kompas_list:
# 	kompas.pull_data_kompas(url_komp, 20, 2	)

for url_kumparan in domain.kumparan_list:
	kumparan.pull_data_kumparan(url_kumparan, 2)
