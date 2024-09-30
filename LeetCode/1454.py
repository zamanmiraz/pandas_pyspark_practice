import pandas as pd

def active_users(accounts: pd.DataFrame, logins: pd.DataFrame) -> pd.DataFrame:
    # MERGE_ # DISTINCT # CHECK THE DIFFERENCE WITH THE PREVIOUS FIVE 
    loginAccount = pd.merge(accounts, logins, on = 'id').drop_duplicates().sort_values(['id', 'login_date'])
    res_dict = {'id':[], 'name': []}
    for (i_d, name), group in loginAccount.groupby(['id', 'name']):
        dates = [date for date in group['login_date']]
        for i in range(4, len(dates)):
            if (dates[i] - dates[i - 4]).days == 4:
                res_dict['id'].append(i_d)
                res_dict['name'].append(name)
                break
    return pd.DataFrame(res_dict)
