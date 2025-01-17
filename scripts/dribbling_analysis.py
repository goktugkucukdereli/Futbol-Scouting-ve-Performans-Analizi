import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_dribbling():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Dribbling olaylarını filtreleme
    dribbles = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Dribble']

    # Oyuncu bazlı dribbling sayısı
    dribbles['player_name'] = dribbles['player'].apply(lambda x: x['name'] if isinstance(x, dict) else None)
    top_dribblers = dribbles['player_name'].value_counts().head(10)

    print("En Çok Dribbling Yapan Oyuncular:")
    print(top_dribblers)

def analyze_shot_blocks():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Şut bloklarını filtreleme
    blocks = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Block']

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
    plt.show()

def plot_dribbling_heatmap():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Dribbling olaylarını filtreleme
    dribbles = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Dribble']
    dribble_locations = dribbles['location'].dropna()

    # Lokasyonları ayırma
    x_coords = [loc[0] for loc in dribble_locations]
    y_coords = [loc[1] for loc in dribble_locations]

    # Sıcaklık haritası görselleştirme
    plt.figure(figsize=(12, 8))
    sns.kdeplot(
        x=x_coords,
        y=y_coords,
        fill=True,
        cmap="Blues",
        n_levels=50,
        thresh=0.05
    )
    plt.title('Dribbling Sıcaklık Haritası', fontsize=16)
    plt.xlabel('Saha X Koordinatı', fontsize=12)
    plt.ylabel('Saha Y Koordinatı', fontsize=12)
    plt.grid(False)
    plt.show()
