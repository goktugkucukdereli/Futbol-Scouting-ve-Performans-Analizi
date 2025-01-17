import json
import pandas as pd
import os

# Gerekli dizinleri oluşturma
output_dir = 'output/processed'
os.makedirs(output_dir, exist_ok=True)

# JSON dosyasını yükle
with open('data/events/7298.json', 'r') as f:
    events = json.load(f)

df = pd.DataFrame(events)

# 1. Şut Verileri
shots = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Shot']
shots_data = shots.apply(lambda row: {
    "match_id": row['match_id'] if 'match_id' in row else None,
    "player_name": row['player']['name'] if row['player'] else None,
    "team_name": row['team']['name'] if row['team'] else None,
    "x_coord": row['location'][0] if row['location'] else None,
    "y_coord": row['location'][1] if row['location'] else None,
    "xg": row['shot']['statsbomb_xg'] if row['shot'] and 'statsbomb_xg' in row['shot'] else None,
    "outcome": row['shot']['outcome']['name'] if row['shot'] and 'outcome' in row['shot'] else None
}, axis=1).tolist()

shots_df = pd.DataFrame(shots_data)
shots_df.to_csv(os.path.join(output_dir, 'filtered_shots.csv'), index=False)

# 2. Pas Verileri
passes = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Pass']
passes_data = passes.apply(lambda row: {
    "match_id": row['match_id'] if 'match_id' in row else None,
    "passer": row['player']['name'] if row['player'] else None,
    "receiver": row['pass']['recipient']['name'] if row['pass'] and 'recipient' in row['pass'] else None,
    "team_name": row['team']['name'] if row['team'] else None,
    "start_x": row['location'][0] if row['location'] else None,
    "start_y": row['location'][1] if row['location'] else None,
    "end_x": row['pass']['end_location'][0] if row['pass'] and 'end_location' in row['pass'] else None,
    "end_y": row['pass']['end_location'][1] if row['pass'] and 'end_location' in row['pass'] else None
}, axis=1).tolist()

passes_df = pd.DataFrame(passes_data)
passes_df.to_csv(os.path.join(output_dir, 'filtered_passes.csv'), index=False)

# 3. Oyuncu Performansı
# Önce 'player' sütunundan sadece 'name' değerini al
df['player_name'] = df['player'].apply(lambda x: x['name'] if isinstance(x, dict) else None)

player_stats = df.groupby('player_name').apply(lambda group: {
    "player_name": group.name,
    "team_name": group.iloc[0]['team']['name'] if group.iloc[0]['team'] else None,
    "shots": len(group[group['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Shot']),
    "dribbles": len(group[group['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Dribble']),
    "tackles": len(group[group['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Tackle']),
    "blocks": len(group[group['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Block'])
}).tolist()

player_stats_df = pd.DataFrame(player_stats)
player_stats_df.to_csv(os.path.join(output_dir, 'player_performance.csv'), index=False)

print("CSV dosyaları başarıyla oluşturuldu!")
