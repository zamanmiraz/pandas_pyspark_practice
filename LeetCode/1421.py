import pandas as pd

def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:
    df = npv.merge(queries, how='right', on=['id', 'year']).fillna(0)
    return df
