import pandas as pd

# Solution to https://leetcode.com/problems/not-boring-movies/
def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    mask = (cinema['description']!='boring') & (cinema['id'] % 2 != 0)
    return cinema[mask].sort_values(by = 'rating', ascending=False)

# Solution to https://leetcode.com/problems/biggest-single-number/
def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    s = my_numbers['num'].value_counts()
    max_num = None if len(s[s==1].index) == 0 else s[s==1].index.max()
    return pd.DataFrame({'num': [max_num]})

# Solution to https://leetcode.com/problems/sales-analysis-iii/
def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    q1_2019 = sales[(sales['sale_date'] >= '2019-01-01') & (sales['sale_date'] <= '2019-03-31')]
    other_q = sales[(sales['sale_date'] < '2019-01-01') | (sales['sale_date'] > '2019-03-31')]
    exclusive_ids = q1_2019[~q1_2019['product_id'].isin(other_q['product_id'].unique())]['product_id'].unique()
    return product[product['product_id'].isin(exclusive_ids)][['product_id', 'product_name']]

# Solution to https://leetcode.com/problems/market-analysis-i/
