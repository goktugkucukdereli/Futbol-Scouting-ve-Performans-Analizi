import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_shot_heatmap():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Şut olaylarını filtreleme
    shots = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Shot']

    # Şut lokasyonlarını alma
    shot_locations = shots['location'].dropna()

    # Lokasyonları X ve Y olarak ayırma
    x_coords = [loc[0] for loc in shot_locations]
    y_coords = [loc[1] for loc in shot_locations]

    # Saha boyutları için bir heatmap oluşturma
    plt.figure(figsize=(12, 8))
    pitch = sns.kdeplot(
        x=x_coords,
        y=y_coords,
        fill=True,
        cmap="coolwarm",
        n_levels=50,
        thresh=0.05
    )
    plt.title('Şut Yoğunluğu Sıcaklık Haritası', fontsize=16)
    plt.xlabel('Saha X Koordinatı', fontsize=12)
    plt.ylabel('Saha Y Koordinatı', fontsize=12)
    plt.grid(False)
    plt.show()
