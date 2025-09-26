import pandas as pd

df = pd.read_csv("example.csv")

# print(df.to_string())

# df.to_excel("example.xlsx", index=False)

print(df["profesion"])

# print(df.iloc[2])

# print(df[["profesion", "nombre"]])
