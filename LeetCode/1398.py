import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    buyA = orders.loc[orders['product_name'] == 'A', 'customer_id'] # loc specify the rows with the product name 'A' and columns of 'customer_id'
    buyB = orders.loc[orders['product_name'] == 'B', 'customer_id'] # loc specify the rows with the product name 'B' and columns of 'customer_id'
    buyC = orders.loc[orders['product_name'] == 'C', 'customer_id'] # loc specify the rows with the product name 'C' and columns of 'customer_id'
    condA = customers['customer_id'].isin(buyA) # check the customer_id in the buyA series
    condB = customers['customer_id'].isin(buyB) # check the customer_id in the buyB series
    condC = customers['customer_id'].isin(buyC) # check the customer_id in the buyC series
    df = customers[condA & condB & ~condC] # 
    return df.sort_values(by = 'customer_id')
