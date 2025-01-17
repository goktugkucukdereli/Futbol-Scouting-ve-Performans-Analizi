import json
import pandas as pd
import matplotlib.pyplot as plt

def analyze_xg():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Şut olaylarını filtreleme ve kopya oluşturma
    shots = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Shot'].copy()

    # xG değerlerini çıkarma
    shots.loc[:, 'xG'] = shots['shot'].apply(lambda x: x['statsbomb_xg'] if isinstance(x, dict) and 'statsbomb_xg' in x else None)

    # xG değerlerini yazdırma
    print("Beklenen Gol (xG) Değerleri:")
    print(shots[['player', 'xG']])

    # xG değerlerini görselleştirme
    plt.figure(figsize=(10, 6))
    plt.hist(shots['xG'].dropna(), bins=10, color='blue', edgecolor='black')
    plt.title('Beklenen Gol (xG) Dağılımı', fontsize=16)
    plt.xlabel('xG Değeri', fontsize=12)
    plt.ylabel('Şut Sayısı', fontsize=12)
    plt.show()
