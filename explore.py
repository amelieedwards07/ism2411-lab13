# Self-assessment
#
# 1. A boolean filter asks a yes-or-no question about each row. Pandas
#    keeps the rows where the answer is True. For example, I can keep
#    only orders from the South region.
#
# 2. df["revenue"] gives me a one-dimensional Series, while
#    df[["revenue"]] gives me a two-dimensional DataFrame with one column.
#    This matters when a function expects a Series or a table as input.
#
# 3. I would choose pandas because I can rerun the same analysis on a
#    new sales file without repeating the filters and formulas by hand.

from pathlib import Path

import pandas as pd

data_dir = Path(__file__).resolve().parent / "data"

print("Exercise 1 - Load the data")
df = pd.read_csv(data_dir / "retail_sales.csv")
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.dtypes)

print("\nExercise 2 - Filter by region")
south = df[df["region"] == "South"]
print("South orders:", len(south))
print(south.head())

print("\nExercise 3 - Top five orders by revenue")
print(df.sort_values("revenue", ascending=False).head(5))

print("\nExercise 4 - South orders with revenue above 1000")
big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]
print("Matching orders:", len(big_south))
print(big_south.head())

print("\nExercise 5 - Revenue per unit")
df["per_unit"] = df["revenue"] / df["quantity"]
print(df.head())
print("Mean per-unit price:", df["per_unit"].mean())

print("\nExercise 6 - Unique regions and order counts")
print(df["region"].unique())
print(df["region"].value_counts())

print("\nExercise 7 - Select three columns")
selected = df[["region", "product", "revenue"]]
print("Shape:", selected.shape)

print("\nExercise 8 - Save the explored data")
output_path = data_dir / "explored.csv"
df.to_csv(output_path, index=False)
with output_path.open(encoding="utf-8") as output_file:
    print("Saved data/explored.csv")
    print("Header:", output_file.readline().strip())
