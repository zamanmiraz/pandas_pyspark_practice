import pandas as pd

def find_safe_countries(person: pd.DataFrame, country: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:

    person['country_code'] = person['phone_number'].apply(lambda x: x.split('-')[0])
    personCountry = pd.merge(person, country, on = 'country_code')[['id', 'name_y']].rename(columns={'name_y': 'country'})
    avgDuration = calls['duration'].mean()
    caller_df = calls[['caller_id', 'duration']].rename(columns = {'caller_id': 'id'})
    callee_df = calls[['callee_id', 'duration']].rename(columns = {'callee_id': 'id'})
    callConcat = pd.concat([caller_df, callee_df], ignore_index=True)
    mergeDf = pd.merge(callConcat, personCountry, on = 'id').groupby(['country'])['duration'].agg('mean').reset_index()
    mergedDf = mergeDf[mergeDf['duration'] > avgDuration][['country']]
    return mergedDf
