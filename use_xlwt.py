'''
使用xlwt
'''
__author__ = "Haipeng Dong"
import xlwt
import xlrd
fileName = r'./tmp002.xls'
oldFile = r'./tmp001.xlsx'
bk = xlrd.open_workbook(oldFile)
try:
    sh = bk.sheet_by_name('SQL Results')
except NameError:
    print('no sheet name in %s' % fileName)
nrows = sh.nrows
ncols = sh.ncols
# 写一个新的Execl中
writeBook = xlwt.Workbook(encoding='utf-8')
sheet = writeBook.add_sheet('备份数据', cell_overwrite_ok=True)
style = xlwt.XFStyle()

for m in range(1, nrows):
    for n in range(ncols):
        sheet.write(m, n, sh.cell(m, n).value)
sheet.write(nrows, 0, xlwt.Formula('SUM(a1:a' + str(nrows) + ')'))
writeBook.save(fileName)
