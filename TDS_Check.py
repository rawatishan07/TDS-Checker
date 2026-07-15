import pandas as pd

df = pd.read_excel("TDS_Check.xlsx")

df["Invoice Total Amt."] = pd.to_numeric(df["Invoice Total Amt."], errors="coerce")
df["Debit BAL"] = pd.to_numeric(df["Debit BAL"], errors="coerce")
df["Debit %"] = ((df["Debit BAL"] / df["Invoice Total Amt."]) * 100)

def identify_tds(debit_pct):

    tolerance = 0.1

    if abs(debit_pct - 10) <= tolerance:
        return "10%"
    elif abs(debit_pct - 4) <= tolerance:
        return "4%"
    elif abs(debit_pct - 2) <= tolerance:
        return "2%"
    elif abs(debit_pct - 2.1) <= tolerance:
        return "2.1%"
    elif abs(debit_pct - 0.01) <= tolerance:
        return "0.01%"
    else:
        return "No Match"

df["Detected TDS Rate"] = df["Debit %"].apply(identify_tds)

# Remove rows that don't match any TDS rate
df = df[df["Detected TDS Rate"] != "No Match"]

print(df)
df.to_excel("tds_check_01.xlsx", index=False)
