# -*- coding: utf-8 -*-
#
# Usage: Load all Taiwan stock code info from csv file
#
# TWSE equities = 上市證券
# TPEx equities = 上櫃證券
#

import csv
import os
from collections import namedtuple


ROW = namedtuple('StockCodeInfo', ['type', 'code', 'name', 'ISIN', 'start',
                                   'market', 'group', 'CFI'])
PACKAGE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
TPEX_EQUITIES_CSV_PATH = os.path.join(PACKAGE_DIRECTORY, 'tpex_equities.csv')
TWSE_EQUITIES_CSV_PATH = os.path.join(PACKAGE_DIRECTORY, 'twse_equities.csv')

codes = {}
tpex = {}
twse = {}
frank_twse ={}
stock_twse = {}

def read_csv(path, types):
    global codes, twse, tpex, frank_twse ,stock_twse
    with open(path, newline='', encoding='utf-8', errors="ignore") as csvfile:
        reader = csv.reader(csvfile)
        csvfile.readline()
        for row in reader:
            row = ROW(*(item.strip() for item in row))
            codes[row.code] = row
            if types == 'tpex':
                tpex[row.code] = row
            else:
                if row.type == '股票':
                    frank_twse[row.code+ " " + row.name] = row
                    stock_twse[row.code] = row
                    # print(row)
                twse[row.code] = row


read_csv(TPEX_EQUITIES_CSV_PATH, 'tpex')
read_csv(TWSE_EQUITIES_CSV_PATH, 'twse')
