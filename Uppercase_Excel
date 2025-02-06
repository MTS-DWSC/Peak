import os
import pandas as pd
import openpyxl
import sqlite3
from openpyxl import load_workbook


def spell_words(text):
    words = text.split()
    corrected_words = [words[0]] + [
        spell_out_words.get(word, word) for word in words[1:]
    ]
    return ' '.join(corrected_words)

def proper_case(text):
    words = text.lower().split()

    for i, word in enumerate(words):
        if word not in lowercase_words:
            words[i] = word.capitalize()

    return ' '.join(words)

def cap_state(text):
    words = text.split()

    if len(words[-1]) == 2:
        words[-1] = words[-1].upper()
    else:
        words[-1]

    return ' '.join(words)

spell_out_words = {
    'NR': 'near',
    'TRIB': 'Tributary',
    'R': 'River'
}

db_fp = r"C:\Users\mtsullivan\OneDrive - DOI\Python\Automate\words.db"
conn = sqlite3.connect(db_fp)
cursor = conn.cursor()
cursor.execute("SELECT word FROM wordbank")
lowercase_words = [row[0] for row in cursor.fetchall()]
conn.close()

# Folder path
folder_path = r'C:\Users\mtsullivan\OneDrive - DOI\In_Depth_Analysis\NameCorrect'
out = 'C:/Users/mtsullivan/OneDrive - DOI/In_Depth_Analysis/NameCorrect/Finished/'


for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):  
        file = os.path.join(folder_path, filename)
        file_name, file_extension = os.path.splitext(filename)  
        file_with_suffix = file_name + '_conv' + file_extension
        df = pd.read_excel(file)

        df['station_nm'] = df['station_nm'].astype(str)

        df['station_nm'] = df['station_nm'].apply(spell_words)  
        df['station_nm'] = df['station_nm'].apply(proper_case) 
        df['station_nm'] = df['station_nm'].apply(cap_state) 

        print(df.head())

        res = os.path.join(out, file_with_suffix)
        df.to_excel(res, index=False)
