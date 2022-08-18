import csv
import datetime

def convert():
    data = []
    with open("cases.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # format category
            if 'not' in row['Category']:
                row['Category'] = False
            else:
                row['Category'] = True
            # formate date
            batchDate = row['AsOf'][11:23].strip()
            date = datetime.datetime.strptime(batchDate, '%d %b %Y').strftime('%Y-%m-%d')
            data.append({'country': row['Country'], 'cases': row['Cases'], 'deaths': row['Deaths'], 'endemic': row['Category'], 'date': date})
    return data