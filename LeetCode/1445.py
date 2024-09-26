import pandas as pd

def apples_oranges(sales: pd.DataFrame) -> pd.DataFrame:
    def func(x):
        return x['sold_num'] if x['fruit'] == 'apples' else -x['sold_num']
    sales['adjusted_sold_num'] = sales.apply(func, axis = 1)
    sale_diff = sales.groupby('sale_date')['adjusted_sold_num'].sum().reset_index(name='diff')
    return sale_diff
