import json
import pandas as pd
import matplotlib.pyplot as plt

def analyze_team_shots():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Şut olaylarını filtreleme
    shots = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Shot']

    # Takım bazlı şut sayısını hesaplama
    team_shots = shots['team'].apply(lambda x: x['name'] if isinstance(x, dict) else None).value_counts()

    # Takım şut sayılarını yazdırma
    print("Takım Bazlı Şut Sayıları:")
    print(team_shots)

    # Takım şut sayılarını görselleştirme
    team_shots.plot(kind='bar', title='Takım Bazlı Şut Sayıları', figsize=(8, 5))
    plt.xlabel('Takımlar')
    plt.ylabel('Şut Sayısı')
    plt.show()
