import pandas as pd

csv_file = pd.read_csv(r'C:\Users\RajeshKorumilli\Downloads\Data Migration\MIB - Data Update in Production\Update Missing Fulfilments for Public Training Products.csv')

df = pd.DataFrame(csv_file)

df