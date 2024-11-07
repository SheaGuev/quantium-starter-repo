import pandas as pd

data_1 = pd.read_csv('data/daily_sales_data_0.csv', index_col="date")
data_2 = pd.read_csv('data/daily_sales_data_1.csv', index_col="date")
data_3 = pd.read_csv('data/daily_sales_data_2.csv', index_col="date")

all_data = pd.concat([data_1, data_2, data_3])

# all_data.where(all_data['product'] != "pink morsel").dropna()
# print(all_data.head())


ad = all_data[all_data['product'] == "pink morsel"]
ad["sales"] = ad.apply(lambda row: f"${row['quantity'] * 3}", axis=1)
ad.drop_duplicates()
ad.drop(columns=["price", "quantity", "product"], inplace=True)
ad.groupby("date").sum()
print(ad.head())