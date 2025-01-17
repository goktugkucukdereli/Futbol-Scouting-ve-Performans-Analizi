import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_shot_blocks():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Şut bloklarını filtreleme
    blocks = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Block']

    # Oyuncu bazlı blok sayısı
    blocks['player_name'] = blocks['player'].apply(lambda x: x['name'] if isinstance(x, dict) else None)
    top_blockers = blocks['player_name'].value_counts().head(10)

    print("En Çok Şut Bloklayan Oyuncular:")
    print(top_blockers)

    # Şut blok lokasyonlarını görselleştirme
    block_locations = blocks['location'].dropna()
    x_coords = [loc[0] for loc in block_locations]
    y_coords = [loc[1] for loc in block_locations]

    plt.figure(figsize=(12, 8))
    sns.kdeplot(
        x=x_coords,
        y=y_coords,
        fill=True,
        cmap="Oranges",
        n_levels=50,
        thresh=0.05
    )
    plt.title('Şut Blokları Sıcaklık Haritası', fontsize=16)
    plt.xlabel('Saha X Koordinatı', fontsize=12)
    plt.ylabel('Saha Y Koordinatı', fontsize=12)
    plt.grid(False)
    plt.show()
