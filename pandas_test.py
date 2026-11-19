import pandas as pd
 
df = pd.read_csv('lotto.csv', encoding='utf-8-sig')
print(df.shape)            # (행 수, 열 수)
print(df.head(3))          # 처음 3줄
print(df['당첨번호1'].head(5).tolist())
