import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    trav = rides.groupby('user_id')['distance'].sum().reset_index(name='travelled_distance')
    merged = users.merge(trav, how = 'left', left_on = 'id', right_on = 'user_id').fillna(0)
    res = merged[['name', 'travelled_distance']].sort_values(by=['travelled_distance','name'], ascending=[False, True])
    return res
