import pandas as pd

def create_bar_chart(sessions: pd.DataFrame) -> pd.DataFrame:
    def func(x):
        if x['duration'] / 60 >= 0 and x['duration'] / 60 < 5:
            return "[0-5>"
        elif x['duration'] / 60 >= 5 and x['duration'] / 60 < 10:
            return "[5-10>"
        elif x['duration'] / 60 >= 10 and x['duration'] / 60 < 15:
            return "[10-15>"
        else:
            return "15 or more"
    sessions['bin'] = sessions.apply(func, axis = 1)
    derived_df = pd.DataFrame({
        "bin": ["[0-5>", "[5-10>", "[10-15>", "15 or more"]
    })
    df = sessions.groupby('bin')['session_id'].count().reset_index(name = 'total')
    merged_df = pd.merge(derived_df, df, on='bin', how='left').fillna(0)
    return merged_df
