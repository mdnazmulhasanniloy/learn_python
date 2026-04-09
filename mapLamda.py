import pandas as pd


#lambda function
# lambda arguments: expression
squire = lambda x: x ** 2
print(squire(5))


df = pd.DataFrame({ "A":[1, 2, 3], "B":[2, 3, 4], "F": [32, 68, 100] })

df['C'] = df['F'].apply(lambda x: (x - 32) * 5 / 9)

df["A+B"] = df.apply(lambda row: row["A"] + row["B"], axis=1)
df["square of A"] = df["A"].map(lambda x: x ** 2)
df["A power by B"] = df.apply(lambda row: pow(row["A"], row["B"]), axis=1)
print(df)