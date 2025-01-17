# Ana dosya
from scripts.shot_analysis import analyze_shots
from scripts.shot_success_analysis import analyze_shot_success
from scripts.team_analysis import analyze_team_shots
from scripts.player_analysis import analyze_player_shot_success
from scripts.heatmap_analysis import generate_shot_heatmap
from scripts.pass_analysis import analyze_passes
from scripts.defense_analysis import analyze_defensive_actions
from scripts.foul_analysis import analyze_fouls
from scripts.tactical_analysis import analyze_formations, analyze_pass_network
from scripts.xg_analysis import analyze_xg
from scripts.xg_model import train_xg_model
from scripts.dribbling_analysis import analyze_dribbling, plot_dribbling_heatmap
from scripts.shot_blocks_analysis import analyze_shot_blocks

if __name__ == "__main__":
    # Şut lokasyon analizini çalıştır
    #print("Şut Lokasyon Analizi Başlıyor...")
    #analyze_shots()

    # Şut başarı oranı analizini çalıştır
    #print("Şut Başarı Oranı Analizi Başlıyor...")
    #analyze_shot_success()

    # Takım bazlı şut analizini çalıştır
    #print("Takım Bazlı Şut Analizi Başlıyor...")
    #analyze_team_shots()

    # Oyuncu bazlı şut başarı oranı analizini çalıştır
    #print("Oyuncu Bazlı Şut Başarı Analizi Başlıyor...")
    #analyze_player_shot_success()

    # Şut sıcaklık haritası analizini çalıştır
    #print("Şut Sıcaklık Haritası Analizi Başlıyor...")
    #generate_shot_heatmap()

    # Pas analizini çalıştır
    #print("Pas Analizi Başlıyor...")
    #analyze_passes()

    # Savunma hareketlerini analiz et
    #print("Savunma Hareketleri Analizi Başlıyor...")
    #analyze_defensive_actions()

    # Faul analizini çalıştır
    #print("Faul Analizi Başlıyor...")
    #analyze_fouls()

    # Taktik analiz
    #print("Taktik Analiz: Formasyonlar")
    #analyze_formations()
    #print("Taktik Analiz: Pas Zinciri")
    #analyze_pass_network()

    # xG analizi
    #print("xG (Beklenen Gol) Analizi Başlıyor...")
    #analyze_xg()

    # xG modeli eğitimi
    #print("xG Modeli Eğitiliyor...")
    #train_xg_model()

    # Dribbling analizi
    #print("Dribbling Analizi Başlıyor...")
    #analyze_dribbling()

    # Dribbling Sıcaklık Haritası
    #print("Dribbling Sıcaklık Haritası Gösteriliyor...")
    #plot_dribbling_heatmap()

    # Şut blokları analizi
    print("Şut Blokları Analizi Başlıyor...")
    analyze_shot_blocks()