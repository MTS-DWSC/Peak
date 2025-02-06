import pandas as pd
import sqlite3

db_path = r"C:\Users\mtsullivan\OneDrive - DOI\Python\FFQ\Databases\Watstore.db"
fp = "C:/Users/mtsullivan/OneDrive - DOI/Python/FFQ/HoldFiles/test_watstore_LRR.txt"

# Connect to the database
conn = sqlite3.connect(db_path)

with open(fp, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Lists for storing extracted values
site_code, z_val, h_val, n_val, location_code, code1, code2, geometry_code = [], [], [], [], [], [], [], []
year_code, height_code, float_code, one_code, two_code = [], [], [], [], []

# Initialize variables
site_code_val, z_val_code, h_val_code, geometry, code1_code, code2_code = "", "", "", "", "", ""
n_val_code = lines[2][:9].strip()
h_val_code = lines[1][:9].strip()

checker = ['H', 'Z', 'N', 'Y']

iso_line = lines[1].split('  ')
h_val_code = iso_line[0].strip() + '.00'
geometry = iso_line[3].strip()
code1_code = iso_line[4].strip()
code2_code = iso_line[5].strip()

iso_line = lines[2].split('  ')
n_val_code = iso_line[0].strip() + '.00'
location = iso_line[3].strip()

for line in lines:
    first_char = line[0]

    if first_char in checker:
        #site_code.append('')
        year_code.append('')
        height_code.append('')
        float_code.append('')
        one_code.append('')  # Changed from 'two_code' to match 'one_code'
        two_code.append('')
    else:
        # Extract values common to all lines
        site_code.append(f"{line[1:9]}.00")
        year_code.append(line[16:24])
        height_code.append(line[27:34])
        float_code.append(line[46:51])
        one_code.append(line[52:67]) 
        two_code.append(line[68:73])

    # Handle 'Z' lines
    if first_char == 'Z':
        z_val_code = line[:9] + '.00'
    z_val.append(z_val_code)

    # Handle 'H' lines
    if first_char == 'H':
        parts = line.split('  ')  # Split by double spaces
        if len(parts) > 5:  # Ensure expected indices exist
            h_val_code, geometry = parts[0].strip() + '.00', parts[3].strip()
            code1_code, code2_code = parts[4].strip(), parts[5].strip()
    h_val.append(h_val_code)
    geometry_code.append(geometry)  # Renaming to match 'location' in headers
    code1.append(code1_code)
    code2.append(code2_code)

    # Handle 'N' lines
    if first_char == 'N':
        n_val_code = line[:9].rstrip() + '.00'
        location = line[16:].rstrip()
    n_val.append(n_val_code)
    location_code.append(location)
# Define headers
headers = ['Site', 'ZCode', 'HCode', 'Geometry', 'Code1', 'Code2', 'NCode', 'Location', 'YearCode',
           'Height', 'Float', 'one_code', 'two_code']

# Create a DataFrame
df = pd.DataFrame(list(zip(
    site_code, z_val, h_val, geometry_code, code1, code2, n_val, location_code, 
    year_code, height_code, float_code, one_code, two_code
)), columns=headers)

# Display the DataFrame
print(df)

# Insert DataFrame into SQLite
df.to_sql("WatstoreRec", conn, if_exists="replace", index=False)

# Commit & close connection
conn.commit()
conn.close()

print("Data inserted successfully!")
