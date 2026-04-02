import pandas as pd
import os

# Dapatkan folder script sekarang
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path dataset relatif dari folder script
data_path = os.path.join(script_dir, "../data/raw/global_sales.csv")

# Load dataset
df = pd.read_csv(data_path)

# Basic cleaning
df = df.drop_duplicates()  # hapus duplikat
df = df.dropna()           # hapus row kosong

# Simpan hasil bersih
processed_path = os.path.join(script_dir, "../data/processed/cleaned_sales.csv")
os.makedirs(os.path.dirname(processed_path), exist_ok=True)
df.to_csv(processed_path, index=False)

print("Data cleaning selesai. File tersimpan di:", processed_path)