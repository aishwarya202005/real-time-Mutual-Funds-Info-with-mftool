from mftool import Mftool
import json
import pandas as pd
import matplotlib.pyplot as plt

mf = Mftool()

# # 1. Get a list of all mutual fund schemes and their unique codes
all_schemes = mf.get_scheme_codes()
print(f"Total schemes found: {len(all_schemes)}")

# 2. Get the latest quote and layout for a specific fund (Example scheme code: '119551')
try:
    scheme_quote = mf.get_scheme_quote('119551')
    print("\n--- Scheme Quote ---")
    print(json.dumps(scheme_quote, indent=2))
except Exception as e:
    print(f"Error fetching quote: {e}")

# 3. Fetch historical NAV data (Returns a dict containing daily NAV historical records)
hist_data = mf.get_scheme_historical_nav('119551')

# Extract data details and convert to a clean DataFrame
df = pd.DataFrame(hist_data['data'])
df['nav'] = pd.to_numeric(df['nav'])
# df['date'] = pd.to_datetime(df['date'], format='%d-%b-%Y')
# df = df.sort_values('date').reset_index(drop=True)

print(df.head())
df = df[:30]
# print(len(df))

# 3. Create the plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["date"], df["nav"], marker="o", linestyle="-", color="b")

# 4. Add labels, title, and grid
ax.set(xlabel="Date", ylabel="NAV", title="NAV Trend Over Time")
ax.grid(True)

# 5. Rotate date labels for better readability
plt.xticks(rotation=45, ha="right")

# Adjust layout to fit rotated dates nicely
plt.tight_layout()

# 6. Display the graph
plt.show()
