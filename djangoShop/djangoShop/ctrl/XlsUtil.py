import os

import xlrd

from djangoShop.ctrl import RedisUtil
from djangoShop.settings import BASE_DIR


class XlsUtil():
    def readXls(self, fileName):
        book = xlrd.open_workbook(os.path.join(BASE_DIR, 'static','file','message.xls'))
        sheet = book.sheet_by_name("Sheet1")
        for item in range(sheet.nrows):
            key = sheet.cell_value(item, 0)
            val = sheet.cell_value(item, 1)
            print(key, val)
            RedisUtil.setProp(key, val)
