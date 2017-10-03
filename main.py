import domain
import bintang
import cnn
import detik
import hipwee
import jalantikus
import kapanlagi
import kompas
import kumparan
import liputan6
import muvila
import okezone
import otosia
import techno
import tempo
import tirto
import tribunnews
import vemale

for url_komp in domain.kompas_list:
    kompas.pull_data_kompas(domain = url_komp, pagination = 20, duration = 30)
    
detik.pull_data_news_detik(domain = domain.detik_news, pagination = 20, duration = 30)
detik.pull_data_finance_detik(domain = domain.detik_finance, duration = 30)
detik.pull_data_inet_detik(domain = domain.detik_inet, duration = 30)
detik.pull_data_oto_detik(domain = domain.detik_oto, duration = 30)
detik.pull_data_travel_detik(domain = domain.detik_travel, duration = 30)

# for url in domain.detik_hot_sport_sepakbola_list:
#     detik.pull_data_hot_sport_sb_detik(domain = url, duration = 5)

# for url2 in domain.detik_food_health_list:
#     detik.pull_data_food_health_detik(domain = url2, duration = 5)

# detik.pull_data_wolipop_detik(domain = domain.detik_wolipop, duration = 1)

# cnn.pull_data_cnn(domain = domain.cnn, pagination = 20, duration = 7)

liputan6.pull_data_liputan6(domain = domain.liputan6, pagination = 25, duration = 30)

# okezone.pull_data_okezone(domain = domain.okezone, pagination = 400, duration = 5)

tempo.pull_data_tempo(domain = domain.tempo, duration = 30)

# tirto.pull_data_tirto(domain = domain.tirto, pagination = 4, duration = 5)

# tribunnews.pull_data_tribunnews(domain = domain.tribunnews, pagination = 30, duration = 5)

# kapanlagi.pull_data_kapanlagi_video(domain = domain.kapanlagi_video, pagination = 5)

# hipwee.pull_data_hipwee(domain = domain.hipwee, pagination = 5)

# for url_kumparan in domain.kumparan_list:
# 	kumparan.pull_data_kumparan(domain = url_kumparan, pagination = 5)

# for url_bintang in domain.bintang_list:
#     bintang.pull_data_bintang(domain = url_bintang, pagination = 2, duration = 1)

# for url_vemale in domain.vemale_list:
#     vemale.pull_data_vemale(domain = url_vemale, pagination = 10, duration = 5)

# for url_jt in domain.jalantikus_list:
#     jalantikus.pull_data_jalantikus(domain = url_jt, pagination = 5)

# for url_kl in domain.kapanlagi_list:
#     kapanlagi.pull_data_kapanlagi(domain = url_kl, pagination = 20)

# for url_otosia in domain.otosia_list:
#     otosia.pull_data_otosia(domain = url_otosia, pagination = 5)

# for url_techno in domain.techno_list:
#     techno.pull_data_techno(domain = url_techno, pagination = 5)

# for url_muvila in domain.muvila_list:
    # muvila.pull_data_muvila(domain = url_muvila, pagination = 5)