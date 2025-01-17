import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_passes():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Pas olaylarını filtreleme  ve kopya oluşturma
    passes = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Pass'].copy()

    # Pas yapan oyuncu isimlerini ekleme
    passes.loc[:, 'player_name'] = passes['player'].apply(lambda x: x['name'] if isinstance(x, dict) else None)
    top_passers = passes['player_name'].value_counts().head(10)

    # En çok pas yapan oyuncuları yazdırma
    print("En Çok Pas Yapan Oyuncular:")
    print(top_passers)

    # En çok pas yapan oyuncuları görselleştirme
    top_passers.plot(kind='bar', figsize=(10, 6), title='En Çok Pas Yapan Oyuncular')
    plt.xlabel('Oyuncular')
    plt.ylabel('Pas Sayısı')
    plt.show()

    # Pasların saha üzerindeki dağılımını görselleştirme
    pass_locations = passes['location'].dropna()
    x_coords = [loc[0] for loc in pass_locations]
    y_coords = [loc[1] for loc in pass_locations]

    plt.figure(figsize=(12, 8))
    sns.kdeplot(
        x=x_coords,
        y=y_coords,
        fill=True,
        cmap="Blues",
        n_levels=50,
        thresh=0.05
    )
    plt.title('Pas Dağılımı Sıcaklık Haritası', fontsize=16)
    plt.xlabel('Saha X Koordinatı', fontsize=12)
    plt.ylabel('Saha Y Koordinatı', fontsize=12)
    plt.grid(False)
    plt.show()
