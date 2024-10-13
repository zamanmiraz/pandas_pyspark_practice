import pandas as pd

def friendly_movies(tv_program: pd.DataFrame, content: pd.DataFrame) -> pd.DataFrame:
    df1 = tv_program[(tv_program.program_date.dt.year == 2020) & (tv_program.program_date.dt.month == 6)]
    df2 = content[(content.Kids_content == "Y") & (content.content_type == "Movies")]
    df2['content_id'] = df2['content_id'].astype(int)
    merge_df = pd.merge(df1, df2, on = "content_id")
    return merge_df[['title']].drop_duplicates()
