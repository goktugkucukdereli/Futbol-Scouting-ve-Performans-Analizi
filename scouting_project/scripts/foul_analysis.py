import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_fouls():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Faul yapan ve kazanan olayları filtreleme ve kopya oluşturma
    fouls_committed = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Foul Committed'].copy()
    fouls_won = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Foul Won'].copy()

    # Faul yapan oyuncuları belirleme
    fouls_committed.loc[:, 'player_name'] = fouls_committed['player'].apply(lambda x: x['name'] if isinstance(x, dict) else None)
    top_foulers = fouls_committed['player_name'].value_counts().head(10)

    # Faul kazanan oyuncuları belirleme
    fouls_won.loc[:, 'player_name'] = fouls_won['player'].apply(lambda x: x['name'] if isinstance(x, dict) else None)
    top_foul_winners = fouls_won['player_name'].value_counts().head(10)

    # En çok faul yapan oyuncuları yazdırma
    print("En Çok Faul Yapan Oyuncular:")
    print(top_foulers)

    # En çok faul kazanan oyuncuları yazdırma
    print("En Çok Faul Kazanan Oyuncular:")
    print(top_foul_winners)

    # En çok faul yapan oyuncuları görselleştirme
    top_foulers.plot(kind='bar', figsize=(10, 6), title='En Çok Faul Yapan Oyuncular')
    plt.xlabel('Oyuncular')
    plt.ylabel('Faul Sayısı')
    plt.show()

    # En çok faul kazanan oyuncuları görselleştirme
    top_foul_winners.plot(kind='bar', figsize=(10, 6), title='En Çok Faul Kazanan Oyuncular')
    plt.xlabel('Oyuncular')
    plt.ylabel('Faul Sayısı')
    plt.show()

    # Faullerin saha üzerindeki dağılımını görselleştirme
    foul_locations = fouls_committed['location'].dropna()
    x_coords = [loc[0] for loc in foul_locations]
    y_coords = [loc[1] for loc in foul_locations]

    plt.figure(figsize=(12, 8))
    sns.kdeplot(
        x=x_coords,
        y=y_coords,
        fill=True,
        cmap="Reds",
        n_levels=50,
        thresh=0.05
    )
    plt.title('Faul Dağılımı Sıcaklık Haritası', fontsize=16)
    plt.xlabel('Saha X Koordinatı', fontsize=12)
    plt.ylabel('Saha Y Koordinatı', fontsize=12)
    plt.grid(False)
    plt.show()
