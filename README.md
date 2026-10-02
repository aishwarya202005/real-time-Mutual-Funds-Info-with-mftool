# Real-Time Mutual Funds Info with mftool

A Python script to fetch, analyze, and visualize Indian Mutual Fund data in real-time. This project uses the `mftool` library to interact with Association of Mutual Funds in India (AMFI) data, parses historical Net Asset Value (NAV) records into a Pandas DataFrame, and plots the NAV trend using Matplotlib.

## Features
*   **Scheme Discovery:** Fetches a complete list of available mutual fund schemes and their unique identification codes.
*   **Real-Time Quotes:** Retrieves the latest available quote details for a specific mutual fund scheme.
*   **Data Analysis:** Converts historical NAV dictionary payloads into a clean structured Pandas DataFrame.
*   **Data Visualization:** Generates a clean line chart illustrating the NAV trend over the last 30 recorded days.

---

## Prerequisites & Installation

Make sure you have Python installed on your system. You will need to install the required external libraries using `pip`:

```bash
pip install mftool pandas matplotlib
```

---

## Getting Started

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt and navigate to the project folder.
3. Run the script using Python:

```bash
python main.py
```
---

## Code Overview

The script executes the following key workflow operations:
1. **Initializes the API wrapper:** Connects to AMFI endpoints using `Mftool()`.
2. **Fetches Total Inventory:** Discovers and logs the total volume of active mutual fund schemes.
3. **Retrieves Specific Meta:** Fetches live quotes for an explicit scheme asset code (Default: `119551` - *HDFC Balanced Advantage Fund - Growth*).
4. **Cleans Data:** Parses the nested JSON structure into a structured Pandas DataFrame and casts target data strings to numeric formats.
5. **Generates Visuals:** Crops the timeline to the most recent 30 trading entries and renders an explicit, clean Matplotlib plot.

---

## Sample Output

### Terminal Metrics
```text
Total schemes found: 14245

--- Scheme Quote ---
{
  "scheme_name": "HDFC Balanced Advantage Fund - Growth Option",
  "scheme_code": 119551,
  "isin_growth": "INF179K01135",
  "last_nav": "456.7890",
  "date": "02-Oct-2026"
}

    date      nav
0  02-Oct-2026  456.7890
1  01-Oct-2026  454.1200
2  30-Sep-2026  455.3400
```

### Visual Trend Graph
The execution will initialize an interactive window displaying a configured timeline graph looking similar to this:
<img width="1000" height="500" alt="DSP_Stock_performance_graph" src="https://github.com/user-attachments/assets/c578ce1d-5741-4736-8677-4708f23eaf1b" />

---

## Customization

To look up data for a different mutual fund:
1. Locate the 6-digit scheme code you want from the printed `all_schemes` list or the AMFI website.
2. Replace `'119551'` in the script with your target scheme code string, eg 124182:
   ```python
   scheme_quote = mf.get_scheme_quote('YOUR_SCHEME_CODE')
   hist_data = mf.get_scheme_historical_nav('YOUR_SCHEME_CODE')
   ```
