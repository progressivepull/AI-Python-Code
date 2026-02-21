import pandas as pd

# Read Excel file
df = pd.read_excel("vehicle.xlsx")

# Print file structure
print("=== File Structure ===")
print("Columns:", df.columns.tolist())
print("\nData Types:")
print(df.dtypes)
print("\nFirst 5 Rows:")
print(df.head())

# Filter vehicles by color
colors_to_filter = ["Black", "Blue", "Red"]
filtered_df = df[df["colors"].isin(colors_to_filter)]

print("\n=== Black, Blue, and Red Vehicles ===")
print(filtered_df)