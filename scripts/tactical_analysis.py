import json
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

def analyze_formations():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Starting XI olaylarını filtreleme
    starting_xi = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Starting XI']

    # Her takımın formasyonunu ve oyuncu listesini yazdırma
    for _, row in starting_xi.iterrows():
        team_name = row['team']['name']
        formation = row['tactics']['formation']
        lineup = row['tactics']['lineup']
        print(f"Takım: {team_name}, Formasyon: {formation}")
        for player in lineup:
            player_name = player['player']['name']
            position = player['position']['name']
            print(f"- {player_name} ({position})")
        print("-" * 30)

def analyze_pass_network():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Geçerli pasları filtreleme ve kopya oluşturma
    passes = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Pass'].copy()

    # Pas veren ve alan oyuncuları belirleme
    passes.loc[:, 'passer'] = passes['player'].apply(lambda x: x['name'] if isinstance(x, dict) else None)
    passes.loc[:, 'receiver'] = passes['pass'].apply(lambda x: x['recipient']['name'] if isinstance(x, dict) and 'recipient' in x else None)

    # Geçerli pasları filtreleme
    valid_passes = passes.dropna(subset=['passer', 'receiver']).copy()

    # Graf oluşturma
    G = nx.DiGraph()
    for _, row in valid_passes.iterrows():
        G.add_edge(row['passer'], row['receiver'])

    # Graf görselleştirme
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(
        G, pos, with_labels=True, node_color='skyblue', edge_color='gray',
        node_size=2000, font_size=10, font_weight='bold'
    )
    plt.title('Pas Zinciri Ağı', fontsize=16)
    plt.show()