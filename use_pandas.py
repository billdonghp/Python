import pandas as pd

sExcelFile = './tmp001.xlsx'
df = pd.read_excel(sExcelFile, sheet_name='SQL Results')
nrows = df.shape[0]
ncols = df.columns.size
print(
    "========================================================================="
)
print('Max Rows:' + str(nrows))
print('Max Columns:' + str(ncols))

print(df.columns)
for iCol in range(ncols):
    print(iCol, ':', df.columns[iCol])

for iRow in range(nrows):
    for iCol in range(ncols):
        print(df.iloc[iRow, iCol], end="\t")
    print('\n')