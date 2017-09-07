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

# for url_komp in domain.kompas_list:
#     kompas.pull_data_kompas(url_komp, 20, 5)
    
# cnn.pull_data_cnn(domain.cnn, 20, 5)

# detik.pull_data_news_detik(domain.detik_news, 20, 5)
# detik.pull_data_finance_detik(domain.detik_finance, 5)
# detik.pull_data_inet_detik(domain.detik_inet, 5)
# detik.pull_data_oto_detik(domain.detik_oto, 5)
# detik.pull_data_travel_detik(domain.detik_travel, 5)

# for url in domain.detik_hot_sport_sepakbola_list:
#     detik.pull_data_hot_sport_sb_detik(url, 5)

# for url2 in domain.detik_food_health_list:
#     detik.pull_data_food_health_detik(url2, 5)

detik.pull_data_wolipop_detik(domain.detik_wolipop, 1)

for url in domain.bintang_list:
    bintang.pull_data_bintang(url, 1, 1)

# hipwee.pull_data_hipwee(domain.hipwee, 5)

# for url_jt in domain.jalantikus_list:
#     jalantikus.pull_data_jalantikus(url_jt, 5)

# for url_kl in domain.kapanlagi_list:
#     kapanlagi.pull_data_kapanlagi(url_kl, 20)

# kapanlagi.pull_data_kapanlagi_video(domain.kapanlagi_video, 5)



# for url_kumparan in domain.kumparan_list:
# 	kumparan.pull_data_kumparan(url_kumparan, 5)

# liputan6.pull_data_liputan6(domain.liputan6, 25, 5)

# for url_muvila in domain.muvila_list:
#     muvila.pull_data_muvila(url_muvila, 5)

# okezone.pull_data_okezone(domain.okezone, 400, 5)

# for url_otosia in domain.otosia_list:
#     otosia.pull_data_otosia(url_otosia, 5)

# for url_techno in domain.techno_list:
#     techno.pull_data_techno(url_techno, 5)

# tempo.pull_data_tempo(domain.tempo, 5)

# tirto.pull_data_tirto(domain.tirto, 4, 5)

# tribunnews.pull_data_tribunnews(domain.tribunnews, 30, 5)

# for url_vemale in domain.vemale_list:
#     vemale.pull_data_vemale(url_vemale, 10, 5)