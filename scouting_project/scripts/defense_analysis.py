import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_defensive_actions():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Savunma olaylarını filtreleme
    defensive_types = ['Block', 'Interception', 'Ball Recovery']
    defenses = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None).isin(defensive_types)].copy()

    # Savunma yapan oyuncuları ekleme
    defenses.loc[:, 'player_name'] = defenses['player'].apply(lambda x: x['name'] if isinstance(x, dict) else None)
    top_defenders = defenses['player_name'].value_counts().head(10)

    # En etkili savunma oyuncularını yazdırma
    print("En Etkili Savunma Oyuncuları:")
    print(top_defenders)

    # En etkili savunma oyuncularını görselleştirme
    top_defenders.plot(kind='bar', figsize=(10, 6), title='En Etkili Savunma Oyuncuları')
    plt.xlabel('Oyuncular')
    plt.ylabel('Savunma Aksiyon Sayısı')
    plt.show()

    # Savunma hareketlerinin saha üzerindeki dağılımını görselleştirme
    defense_locations = defenses['location'].dropna()
    x_coords = [loc[0] for loc in defense_locations]
    y_coords = [loc[1] for loc in defense_locations]

    plt.figure(figsize=(12, 8))
    sns.kdeplot(
        x=x_coords,
        y=y_coords,
        fill=True,
        cmap="Greens",
        n_levels=50,
        thresh=0.05
    )
    plt.title('Savunma Hareketleri Sıcaklık Haritası', fontsize=16)
    plt.xlabel('Saha X Koordinatı', fontsize=12)
    plt.ylabel('Saha Y Koordinatı', fontsize=12)
    plt.grid(False)
    plt.show()
