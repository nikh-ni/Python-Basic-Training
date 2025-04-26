import pandas as pd

# 1. 讀取 Excel 檔案
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# 2. 選取需要的欄位
df = df[['Name', 'Age', 'Salary']]

# 3. 刪除 Age 為空值的行
df = df.dropna(subset=['Age'])

# 4. 篩選 Salary > 50000 的資料
df = df[df['Salary'] > 50000]

# 5. 依 Age 由大到小排序
df = df.sort_values(by='Age', ascending=False)

# 6. 存回 Excel 檔案
df.to_excel("output.xlsx", index=False)

print("Data processing completed and saved to output.xlsx")