import pandas as pd

def eval_expression(variables: pd.DataFrame, expressions: pd.DataFrame) -> pd.DataFrame:
    exp = expressions.merge(variables, left_on='left_operand', right_on='name').rename(columns={'value': 'left_val'})
    exp = exp.merge(variables, left_on='right_operand', right_on='name').rename(columns={'value': 'right_val'})
    def func(x):
        if x['operator'] == '>' and x['left_val'] > x['right_val']: return 'true'
        elif x['operator'] == '<' and x['left_val'] < x['right_val']: return 'true'
        elif x['operator'] == '=' and x['left_val'] == x['right_val']: return 'true'
        else:
            return 'false'
    exp['value'] = exp.apply(func, axis=1)
    return exp[['left_operand', 'operator', 'right_operand', 'value']]
