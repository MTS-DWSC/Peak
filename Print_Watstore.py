import pandas as pd
import sqlite3

db_path = r"C:\Users\mtsullivan\OneDrive - DOI\Python\FFQ\Databases\Watstore.db"


select_arr = ['05070000.00', '05082500.00', '05082600.00']
select_tuple = tuple(select_arr)

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

sql_query = f"""
SELECT 
Site, ZCode, HCode, Geometry, Code1, Code2, NCode, 
Location, YearCode, Height, Float, one_code, two_code
FROM WatstoreRec
WHERE Site IN {select_tuple}
ORDER BY
    Site,
    SUBSTR(YearCode, 1, 4)
;
"""

# Execute Query
cursor.execute(sql_query)

# Fetch Results
results = cursor.fetchall()

# Print Results
check = results[0][0]
count = 0
arr = []
master_arr = []
for row in results:
    if row[0] == check and count < 4:
        if count == 0:
            line1 = row[1] + (' ' * 20) + 'USGS'
            arr.append(line1)
        if count == 1:
            if row[4] != '' and row[5] != '':
                line2 = row[2] + (' ' * 4) + row[3] + (' ' * 2) + row[4] + (' ' * 2) + row[5]
            elif row[4] == '' and row[5] != '':
                line2 = row[2] + (' ' * 4) + row[3] + (' ' * 9) + row[5]
            else:
                line2 = row[2] + (' ' * 4) + row[3]
            arr.append(line2)
        if count == 2:
            line3 = row[6] + (' ' * 4) + row[7]
            arr.append(line3)
        if count == 3:
            line4 = 'Y' + row[0]
            arr.append(line4)
        count += 1
    elif row[0] == check and count > 3:
        base_string = '3' + row[0] + (' ' * 4) + row[8] + (' ' * 3) + row[9] + (' ' * 12) + row[10] + ' ' 
        if row[8] != '':
            arr.append(base_string + row[11]+ row[12])

    # Append lengths
    elif row[0] != check:
        master_arr.append(arr)
        check = row[0]
        count = 0
        arr = []
        
    else:
        print('NA')

master_arr.append(arr)

conn.close()

file_path = r'C:\Users\mtsullivan\OneDrive - DOI\Python\FFQ\HoldFiles\output.txt'

with open(file_path, 'w') as file:
    for row in master_arr:
        for x in row:
            if len(str(x)) != 31:
                file.write(str(x) + '\n')


print(f"Results written to {file_path}")

print(len(master_arr))
