import pandas as pd, numpy as np, time

excel_path = r"original_data/6.6. Production_of_Mineral_Raw_Materials_of_individual_Countries_by_Countries.xlsx"

years = ["2019","2020","2021","2022","2023"]

t0 = time.time()
xlsx = pd.ExcelFile(excel_path)
rows = []

for sheet in xlsx.sheet_names:
    try:
        df = pd.read_excel(excel_path, sheet_name=sheet, header=1, nrows=150)
        avail = [y for y in years if y in df.columns]
        if not avail:
            continue
        for y in avail:
            df[y] = pd.to_numeric(df[y], errors="coerce")
        totals = {y: float(np.nansum(df[y].values)) for y in avail}
        if any(np.isfinite(v) and v != 0 for v in totals.values()):
            row = {"Country": sheet}
            row.update({y: totals.get(y, 0.0) for y in years})
            rows.append(row)
    except Exception as e:
        print("Skipped:", sheet)

df_out = pd.DataFrame(rows).fillna(0.0)
for y in years:
    if y not in df_out.columns:
        df_out[y] = 0.0
df_out = df_out[["Country"] + years].sort_values("Country")

# 保存
df_out.to_csv("ALL_country_total_production_2019_2023.csv", index=False)
df_out[["Country","2019","2023"]].to_csv("ALL_country_total_production_2years.csv", index=False)

print("✅ Done:", len(df_out), "countries processed in", round(time.time()-t0,1), "sec")
