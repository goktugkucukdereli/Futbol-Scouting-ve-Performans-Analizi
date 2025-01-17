import json
import pandas as pd
import matplotlib.pyplot as plt

def analyze_shots():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Şut lokasyonlarını analiz etme, Şut olaylarını filtreleme
    shots = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Shot']
    shot_locations = shots['location'].dropna()

    # Lokasyonları ayırma
    x_coords = [loc[0] for loc in shot_locations]
    y_coords = [loc[1] for loc in shot_locations]

    # Şut lokasyonlarını görselleştirme
    plt.figure(figsize=(10, 7))
    plt.scatter(x_coords, y_coords, c='blue', alpha=0.7)
    plt.title('Şut Lokasyonları')
    plt.xlabel('Saha X Koordinatı')
    plt.ylabel('Saha Y Koordinatı')
    plt.grid(True)
    plt.show()
