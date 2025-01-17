import json
import pandas as pd
import matplotlib.pyplot as plt

def analyze_player_shot_success():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Şut olaylarını filtreleme  ve kopya oluşturma
    shots = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Shot'].copy()

    # Şutların sonuçlarını ve oyuncu isimlerini ekleme
    shots.loc[:, 'outcome'] = shots['shot'].apply(lambda x: x['outcome']['name'] if isinstance(x, dict) else None)
    shots.loc[:, 'player_name'] = shots['player'].apply(lambda x: x['name'] if isinstance(x, dict) else None)

    # Oyuncu bazlı şut başarı oranını hesaplama
    player_outcomes = shots.groupby(['player_name', 'outcome']).size().unstack(fill_value=0)

    # Sonuçları yazdırma
    print("Oyuncu Bazlı Şut Başarı Oranı:")
    print(player_outcomes)

    # İlk 5 oyuncuyu görselleştirme
    top_players = player_outcomes.sum(axis=1).nlargest(5).index
    player_outcomes.loc[top_players].plot(kind='bar', figsize=(12, 6), title='Oyuncu Bazlı Şut Başarı Oranı')
    plt.xlabel('Oyuncular')
    plt.ylabel('Şut Sayısı')
    plt.legend(title="Sonuçlar")
    plt.show()
