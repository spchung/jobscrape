# load csv and save each row as txt file 

csv_file = 'unstruct_jobs_blobs.csv'

import csv

with open('unstruct_jobs_dump.csv', 'r') as file:
    reader = csv.reader(file)
    i = 1
    for row in reader:
        title, blob = row
        title = title.replace(' ', '_').replace('/', '_')
        file_name = f'training_data/raw/{title}.train.txt'
        # remove all new line 
        blob = blob.replace('\n', ' ')
        with open(file_name, 'w') as f:
            f.write(blob)
        print(f'file {file_name} created')