import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from imblearn.over_sampling import SMOTE

def train_xg_model():
    # JSON dosyasını okuma
    with open('data/events/7298.json', 'r') as f:
        events = json.load(f)
    df = pd.DataFrame(events)

    # Şut olaylarını filtreleme
    shots = df[df['type'].apply(lambda x: x['name'] if isinstance(x, dict) else None) == 'Shot'].copy()

    # Özellikleri çıkarma
    shots['X'] = shots['location'].apply(lambda x: x[0] if isinstance(x, list) else None)
    shots['Y'] = shots['location'].apply(lambda x: x[1] if isinstance(x, list) else None)
    shots['outcome'] = shots['shot'].apply(lambda x: 1 if x['outcome']['name'] == 'Goal' else 0 if isinstance(x, dict) else None)

    # Kale merkezine göre mesafe ve açı hesaplama
    goal_center = [120, 40]
    shots['distance'] = shots.apply(lambda row: np.sqrt((goal_center[0] - row['X'])**2 + (goal_center[1] - row['Y'])**2), axis=1)
    shots['angle'] = shots.apply(lambda row: np.arctan2(goal_center[1] - row['Y'], goal_center[0] - row['X']), axis=1)

    # Gerekli sütunlar ve temizleme
    features = ['X', 'Y', 'distance', 'angle']
    shots = shots.dropna(subset=['X', 'Y', 'distance', 'angle', 'outcome'])

    # Özellikler ve hedef değişkeni ayırma
    X = shots[features]
    y = shots['outcome']

    # SMOTE ile veri çoğaltma
    smote = SMOTE(random_state=42, k_neighbors=min(3, len(X[y == 1]) - 1))  # Komşu sayısını veri setine uyarlayın
    X_resampled, y_resampled = smote.fit_resample(X, y)

    # Resampled veri setlerini kontrol et
    print("SMOTE Sonrası Sınıf Dağılımı:")
    print(pd.Series(y_resampled).value_counts())

    # Eğitim ve test veri setlerini ayırma
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

    # Model eğitimi
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Model değerlendirme
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    print("Sınıflandırma Raporu:")
    print(classification_report(y_test, y_pred))

    # ROC-AUC hesaplama
    try:
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        print(f"xG Model ROC-AUC: {roc_auc:.2f}")
    except ValueError:
        print("ROC-AUC Skoru hesaplanamadı: Veri setinde sadece tek bir sınıf mevcut.")

    return model
