import json
import pandas as pd
import matplotlib.pyplot as plt

def analyze_shot_success():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Şut olaylarını filtreleme
    shots = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Shot'].copy()

    # Şutların sonuçlarını çıkarma
    shots.loc[:, 'outcome'] = shots['shot'].apply(lambda x: x['outcome']['name'] if isinstance(x, dict) else None)
    shot_outcomes = shots['outcome'].value_counts()

    # Sonuçları yazdırma
    print("Şut Sonuçları:")
    print(shot_outcomes)

    # Şut sonuçlarını görselleştirme
    shot_outcomes.plot(kind='bar', title='Şut Başarı Oranı', figsize=(8, 5))
    plt.xlabel('Sonuçlar')
    plt.ylabel('Şut Sayısı')
    plt.show()
