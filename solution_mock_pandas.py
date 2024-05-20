import pandas as pd

# Solution to https://leetcode.com/problems/not-boring-movies/
def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    mask = (cinema['description']!='boring') & (cinema['id'] % 2 != 0)
    return cinema[mask].sort_values(by = 'rating', ascending=False)

# Solutiont to https://leetcode.com/problems/biggest-single-number/
def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    s = my_numbers['num'].value_counts()
    max_num = None if len(s[s==1].index) == 0 else s[s==1].index.max()
    return pd.DataFrame({'num': [max_num]})
