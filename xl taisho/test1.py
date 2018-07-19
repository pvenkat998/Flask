file_name = "\\fileserver\CoffeeCrazy3\その他\受け渡し用\python test\スカフロ営サポ　自動化test_柴藤\提案内容保存先\2018-06-15_営業予定\（株）丸峰観光ホテル\過去提案対象企業\対象企業【◆旅館・ホテル業 (九州）】_作成日：20170530_32件.xls"
sheet ='対象企業３'

import pandas as pd
df = pd.read_excel(io=file_name, sheet_name=sheet)
print(df.head(5))