import os
import pandas as pd

def ensure_directory_exists(directory):
    """
    Verilen dizinin var olup olmadığını kontrol eder, yoksa oluşturur.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def load_json_as_dataframe(json_path):
    """
    JSON dosyasını pandas DataFrame olarak yükler.
    """
    try:
        data = pd.read_json(json_path)
        return data
    except Exception as e:
        print(f"JSON dosyası yüklenirken hata oluştu: {e}")
        return pd.DataFrame()

def save_dataframe_to_csv(dataframe, output_path):
    """
    Bir DataFrame'i CSV dosyası olarak kaydeder.
    """
    try:
        dataframe.to_csv(output_path, index=False)
        print(f"Veriler başarıyla kaydedildi: {output_path}")
    except Exception as e:
        print(f"Veriler CSV olarak kaydedilirken hata oluştu: {e}")
