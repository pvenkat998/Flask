from flask import Flask, render_template, url_for, request
import pandas as pd
import datetime
import os
#from openpyxl import load_workbook

path = "\\\\172.16.0.232\CoffeeCrazy3\その他\受け渡し用\\20180703橋本さん受け渡し用\加工済み会議資料"
print(path)
most_recent_file = max(
    (os.path.join(root, f) for root, _, the_files in os.walk(path) for f in the_files if f.lower().endswith(".xlsx")),
    key=os.path.getmtime)
print(most_recent_file)
#xls = pd.ExcelFile(r"\\172.16.0.232\CoffeeCrazy3\その他\受け渡し用\20180703橋本さん受け渡し用\加工済み会議資料\0207顧問\【顧問】会議資料190207.xlsx")
xls = pd.ExcelFile(most_recent_file)
df = pd.read_excel(xls, '月次進捗(事業ALL',parse_cols='B:AU',skiprows = 28,index_col=0)
df2 = pd.read_excel(xls, '月次進捗 (営業ALL (018を除く)',parse_cols='B:AU',skiprows = 30,index_col=0)
df3 = pd.read_excel(xls, '月次進捗 (営業 018生',parse_cols='B:AU',skiprows = 27,index_col=0)
df4 = pd.read_excel(xls, '月次進捗 (SSALL',parse_cols='B:AU',skiprows = 30,index_col=0)
#  df = pd.read_excel(r"C:\Users\pitchuka-ramana\PycharmProjects\Flask\行動指標管理web\data\【顧問】会議資料181213.xlsx",sheet_name='月次進捗(事業ALL',parse_cols='B:AO',skiprows = 28,index_col=0)
df_1=df.iloc[9:16]
df_1 = df_1.dropna(axis=1)
colname = df_1.columns.tolist()
for i in range(len(colname)):
    print(i)
    # looping columns nowww
    if (i % 3 == 2):
        for j in range(7):
            df_1.iloc[j][colname[i]] = (df_1.iloc[j][colname[i]] + df_1.iloc[j][colname[i - 1]] + df_1.iloc[j][
                colname[i - 2]]) / 3
# print(df_1.T)
for i in range(len(colname)):

    if (i % 3 == 2):
        df_1 = df_1.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df_1 = df_1.drop([colname[i]], axis=1)
print(df_1.columns.tolist())
df_2=df.iloc[99:106]
df_2 = df_2.dropna(axis=1)
colname = df_2.columns.tolist()
for i in range(len(colname)):

    print(i)
    # looping columns nowww
    if (i % 3 == 2):
        for j in range(7):
            df_2.iloc[j][colname[i]] = (df_2.iloc[j][colname[i]] + df_2.iloc[j][colname[i - 1]] + df_2.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):

    if (i % 3 == 2):
        df_2 = df_2.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df_2 = df_2.drop([colname[i]], axis=1)
#make a lot of temps
#need to add more
df_3=df.iloc[135:142].add(df.iloc[144:149].reindex_like(df.iloc[135:142]), fill_value=0).add(df.iloc[151:158].reindex_like(df.iloc[135:142]), fill_value=0).add(df.iloc[160:167].reindex_like(df.iloc[135:142]), fill_value=0).add(df.iloc[169:176].reindex_like(df.iloc[135:142]), fill_value=0).add(df.iloc[178:185].reindex_like(df.iloc[135:142]), fill_value=0).add(df.iloc[185:192].reindex_like(df.iloc[135:142]), fill_value=0).add(df.iloc[194:201].reindex_like(df.iloc[135:142]), fill_value=0).add(df.iloc[203:210].reindex_like(df.iloc[135:142]), fill_value=0).add(df.iloc[212:219].reindex_like(df.iloc[135:142]), fill_value=0)
df_3 = df_3.dropna(axis=1)
colname = df_3.columns.tolist()
for i in range(len(colname)):

    print(i)
    # looping columns nowww
    if (i % 3 == 2):
        for j in range(7):
            df_3.iloc[j][colname[i]] = (df_3.iloc[j][colname[i]] + df_3.iloc[j][colname[i - 1]] + df_3.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):

    if (i % 3 == 2):
        df_3 = df_3.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df_3 = df_3.drop([colname[i]], axis=1)

#2

df2_1 = df2.iloc[11:18]
df2_1 = df2_1.dropna(axis=1)
colname = df2_1.columns.tolist()
for i in range(len(colname)):

    print(i)
    # looping columns nowww
    if (i % 3 == 2):
        for j in range(7):
            df2_1.iloc[j][colname[i]] = (df2_1.iloc[j][colname[i]] + df2_1.iloc[j][colname[i - 1]] + df2_1.iloc[j][
                colname[i - 2]]) / 3
# print(df2_1.T)
for i in range(len(colname)):

    if (i % 3 == 2):
        df2_1 = df2_1.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df2_1 = df2_1.drop([colname[i]], axis=1)

df2_2 = df2.iloc[121:128]
df2_2 = df2_2.dropna(axis=1)
colname = df2_2.columns.tolist()
for i in range(len(colname)):
    print(i)
    if (i % 3 == 2):
        for j in range(7):
            df2_2.iloc[j][colname[i]] = (df2_2.iloc[j][colname[i]] + df2_2.iloc[j][colname[i - 1]] + df2_2.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):
    if (i % 3 == 2):
        df2_2 = df2_2.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df2_2 = df2_2.drop([colname[i]], axis=1)

df2_3 = df2.iloc[165:172].add(df2.iloc[176:183].reindex_like(df2.iloc[165:172]), fill_value=0).add(
    df2.iloc[187:194].reindex_like(df2.iloc[165:172]), fill_value=0).add(
    df2.iloc[198:205].reindex_like(df2.iloc[165:172]), fill_value=0).add(
    df2.iloc[209:216].reindex_like(df2.iloc[165:172]), fill_value=0).add(
    df2.iloc[220:227].reindex_like(df2.iloc[165:172]), fill_value=0).add(
    df2.iloc[231:238].reindex_like(df2.iloc[165:172]), fill_value=0).add(
    df2.iloc[242:249].reindex_like(df2.iloc[165:172]), fill_value=0).add(
    df2.iloc[253:260].reindex_like(df2.iloc[165:172]), fill_value=0).add(
    df2.iloc[264:271]   .reindex_like(df2.iloc[165:172]), fill_value=0)

df2_3 = df2_3.dropna(axis=1)
colname = df2_3.columns.tolist()
for i in range(len(colname)):
    print(i)
    if (i % 3 == 2):
        for j in range(7):
            df2_3.iloc[j][colname[i]] = (df2_3.iloc[j][colname[i]] + df2_3.iloc[j][colname[i - 1]] + df2_3.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):
    if (i % 3 == 2):
        df2_3 = df2_3.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df2_3 = df2_3.drop([colname[i]], axis=1)

#3

df3_1 = df3.iloc[11:18]
df3_1 = df3_1.dropna(axis=1)
colname = df3_1.columns.tolist()
for i in range(len(colname)):
    if (i % 3 == 2):
        for j in range(7):
            df3_1.iloc[j][colname[i]] = (df3_1.iloc[j][colname[i]] + df3_1.iloc[j][colname[i - 1]] + df3_1.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):
    if (i % 3 == 2):
        df3_1 = df3_1.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df3_1 = df3_1.drop([colname[i]], axis=1)

df3_2 = df3.iloc[101:108]
df3_2 = df3_2.dropna(axis=1)
colname = df3_2.columns.tolist()
for i in range(len(colname)):
    if (i % 3 == 2):
        for j in range(7):
            df3_2.iloc[j][colname[i]] = (df3_2.iloc[j][colname[i]] + df3_2.iloc[j][colname[i - 1]] + df3_2.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):
    if (i % 3 == 2):
        df3_2 = df3_2.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df3_2 = df3_2.drop([colname[i]], axis=1)
df3_3 = df3.iloc[137:144].add(df3.iloc[146:153].reindex_like(df3.iloc[137:144]), fill_value=0).add(
    df3.iloc[155:162].reindex_like(df3.iloc[137:144]), fill_value=0).add(
    df3.iloc[164:171].reindex_like(df3.iloc[137:144]), fill_value=0).add(
    df3.iloc[173:180].reindex_like(df3.iloc[137:144]), fill_value=0).add(
    df3.iloc[182:189].reindex_like(df3.iloc[137:144]), fill_value=0).add(
    df3.iloc[191:198].reindex_like(df3.iloc[137:144]), fill_value=0).add(
    df3.iloc[200:207].reindex_like(df3.iloc[137:144]), fill_value=0).add(
    df3.iloc[209:216].reindex_like(df3.iloc[137:144]), fill_value=0).add(
    df3.iloc[218:225].reindex_like(df3.iloc[137:144]), fill_value=0)
df3_3 = df3_3.dropna(axis=1)
colname = df3_3.columns.tolist()
for i in range(len(colname)):
    if (i % 3 == 2):
        for j in range(7):
            df3_3.iloc[j][colname[i]] = (df3_3.iloc[j][colname[i]] + df3_3.iloc[j][colname[i - 1]] + df3_3.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):
    if (i % 3 == 2):
        df3_3 = df3_3.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df3_3 = df3_3.drop([colname[i]], axis=1)

#4

df4_1 = df4.iloc[11:18]
df4_1 = df4_1.dropna(axis=1)
colname = df4_1.columns.tolist()
for i in range(len(colname)):
    if (i % 3 == 2):
        for j in range(7):
            df4_1.iloc[j][colname[i]] = (df4_1.iloc[j][colname[i]] + df4_1.iloc[j][colname[i - 1]] + df4_1.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):
    if (i % 3 == 2):
        df4_1 = df4_1.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df4_1 = df4_1.drop([colname[i]], axis=1)

df4_2 = df4.iloc[111:118]
df4_2 = df4_2.dropna(axis=1)
colname = df4_2.columns.tolist()
for i in range(len(colname)):
    if (i % 3 == 2):
        for j in range(7):
            df4_2.iloc[j][colname[i]] = (df4_2.iloc[j][colname[i]] + df4_2.iloc[j][colname[i - 1]] + df4_2.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):
    if (i % 3 == 2):
        df4_2 = df4_2.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df4_2 = df4_2.drop([colname[i]], axis=1)
df4_3 = df4.iloc[151:159].add(df4.iloc[161:169].reindex_like(df4.iloc[151:159]), fill_value=0).add(
    df4.iloc[171:179].reindex_like(df4.iloc[151:159]), fill_value=0).add(
    df4.iloc[181:189].reindex_like(df4.iloc[151:159]), fill_value=0).add(
    df4.iloc[191:199].reindex_like(df4.iloc[151:159]), fill_value=0).add(
    df4.iloc[201:209].reindex_like(df4.iloc[151:159]), fill_value=0).add(
    df4.iloc[211:219].reindex_like(df4.iloc[151:159]), fill_value=0).add(
    df4.iloc[221:229].reindex_like(df4.iloc[151:159]), fill_value=0).add(
    df4.iloc[231:239].reindex_like(df4.iloc[151:159]), fill_value=0).add(
    df4.iloc[241:249].reindex_like(df4.iloc[151:159]), fill_value=0)
df4_3 = df4_3.dropna(axis=1)
colname = df4_3.columns.tolist()
for i in range(len(colname)):
    if (i % 3 == 2):
        for j in range(7):
            df4_3.iloc[j][colname[i]] = (df4_3.iloc[j][colname[i]] + df4_3.iloc[j][colname[i - 1]] + df4_3.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):
    if (i % 3 == 2):
        df4_3 = df4_3.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df4_3 = df4_3.drop([colname[i]], axis=1)

# ------------------------------------------------------df1------------------------------------------------ the one before was to initialize all
# ------------------------------------------------------df1------------------------------------------------ the one before was to initialize all
# ------------------------------------------------------df1------------------------------------------------ the one before was to initialize all
# ------------------------------------------------------df1------------------------------------------------ the one before was to initialize all

#df initialize
df=df.iloc[0:7]
df = df.dropna(axis = 1)
colname = df.columns.tolist()
for i in range(len(colname)):
    if(i%3==2):
        for j in range(7):
            df.iloc[j][colname[i]]=(df.iloc[j][colname[i]]+df.iloc[j][colname[i-1]]+df.iloc[j][colname[i-2]])/3
for i in range(len(colname)):
    if(i%3==2):
        df = df.rename(columns={colname[i]: str(colname[i-2])[:7]+'-'+str(colname[i])[:7]})
    else:
        df=df.drop([colname[i]], axis=1)
colname = df.columns.tolist()
for i in range(len(colname)):
    a = colname[i]
    df[a] = df[a].astype(int)
pt_value = df.T['営業社数'].astype(int).tolist()
eigyoshasuu=df.T['受注案件数'].astype(int).tolist()
point_PT=df.T['平均単価'].astype(int).tolist()

for i in range(len(colname)):
    a = colname[i]
    df_1[a] = df_1[a].astype(int)
pt_value_1 = df_1.T['営業社数'].astype(int).tolist()
eigyoshasuu_1=df_1.T['受注案件数'].astype(int).tolist()
point_PT_1=df_1.T['平均単価'].astype(int).tolist()

for i in range(len(colname)):
    a = colname[i]
    df_2[a] = df_2[a].astype(int)
pt_value_2 = df_2.T['営業社数'].astype(int).tolist()
eigyoshasuu_2=df_2.T['受注案件数'].astype(int).tolist()
point_PT_2=df_2.T['平均単価'].astype(int).tolist()

for i in range(len(colname)):
    a = colname[i]
    df_3[a] = df_3[a].astype(int)
pt_value_3 = df_3.T['営業社数'].astype(int).tolist()
eigyoshasuu_3=df_3.T['受注案件数'].astype(int).tolist()
point_PT_3=df_3.T['平均単価'].astype(int).tolist()
#REALEND----------------------------------------------

#------------------------------------------------------df2------------------------------------------------
df2=df2.iloc[0:7]
df2 = df2.dropna(axis = 1)
colname = df2.columns.tolist()
for i in range(len(colname)):
    if (i % 3 == 2):
        for j in range(7):
            df2.iloc[j][colname[i]] = (df2.iloc[j][colname[i]] + df2.iloc[j][colname[i - 1]] + df2.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):
    if (i % 3 == 2):
        df2 = df2.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df2 = df2.drop([colname[i]], axis=1)
colname = df2.columns.tolist()

for i in range(len(colname)):
    a = colname[i]
    df2[a] = df2[a].astype(int)
pt_value2 = df2.T['営業社数'].astype(int).tolist()
eigyoshasuu2=df2.T['受注案件数'].astype(int).tolist()
point_PT2=df2.T['平均単価'].astype(int).tolist()
for i in range(len(colname)):
    a = colname[i]
    df2_1[a] = df2_1[a].astype(int)
pt_value2_1 = df2_1.T['営業社数'].astype(int).tolist()
eigyoshasuu2_1=df2_1.T['受注案件数'].astype(int).tolist()
point_PT2_1=df2_1.T['平均単価'].astype(int).tolist()

for i in range(len(colname)):
    a = colname[i]
    df2_2[a] = df2_2[a].astype(int)
pt_value2_2 = df2_2.T['営業社数'].astype(int).tolist()
eigyoshasuu2_2=df2_2.T['受注案件数'].astype(int).tolist()
point_PT2_2=df2_2.T['平均単価'].astype(int).tolist()

for i in range(len(colname)):
    a = colname[i]
    df2_3[a] = df2_3[a].astype(int)
pt_value2_3 = df2_3.T['営業社数'].astype(int).tolist()
eigyoshasuu2_3=df2_3.T['受注案件数'].astype(int).tolist()
point_PT2_3=df2_3.T['平均単価'].astype(int).tolist()

#------------------------------------------------------df3------------------------------------------------
df3=df3.iloc[0:7]
df3 = df3.dropna(axis = 1)
colname = df3.columns.tolist()
for i in range(len(colname)):
    if (i % 3 == 2):
        for j in range(7):
            df3.iloc[j][colname[i]] = (df3.iloc[j][colname[i]] + df3.iloc[j][colname[i - 1]] + df3.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):

    if (i % 3 == 2):
        df3 = df3.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df3 = df3.drop([colname[i]], axis=1)
colname = df3.columns.tolist()
for i in range(len(colname)):
    a = colname[i]
    df3[a] = df3[a].astype(int)
pt_value3 = df3.T['営業社数'].astype(int).tolist()
eigyoshasuu3=df3.T['受注案件数'].astype(int).tolist()
point_PT3=df3.T['平均単価'].astype(int).tolist()
for i in range(len(colname)):
    a = colname[i]
    df3_1[a] = df3_1[a].astype(int)
pt_value3_1 = df3_1.T['営業社数'].astype(int).tolist()
eigyoshasuu3_1=df3_1.T['受注案件数'].astype(int).tolist()
point_PT3_1=df3_1.T['平均単価'].astype(int).tolist()

for i in range(len(colname)):
    a = colname[i]
    df3_2[a] = df3_2[a].astype(int)
pt_value3_2 = df3_2.T['営業社数'].astype(int).tolist()
eigyoshasuu3_2=df3_2.T['受注案件数'].astype(int).tolist()
point_PT3_2=df3_2.T['平均単価'].astype(int).tolist()

for i in range(len(colname)):
    a = colname[i]
    df3_3[a] = df3_3[a].astype(int)
pt_value3_3 = df3_3.T['営業社数'].astype(int).tolist()
eigyoshasuu3_3=df3_3.T['受注案件数'].astype(int).tolist()
point_PT3_3=df3_3.T['平均単価'].astype(int).tolist()
#------------------------------------------------------df4------------------------------------------------
df4=df4.iloc[0:7]
df4 = df4.dropna(axis = 1)
colname = df4.columns.tolist()
for i in range(len(colname)):
    if (i % 3 == 2):
        for j in range(7):
            df4.iloc[j][colname[i]] = (df4.iloc[j][colname[i]] + df4.iloc[j][colname[i - 1]] + df4.iloc[j][
                colname[i - 2]]) / 3
for i in range(len(colname)):
    if (i % 3 == 2):
        df4 = df4.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
    else:
        df4 = df4.drop([colname[i]], axis=1)
colname = df4.columns.tolist()
for i in range(len(colname)):
    a = colname[i]
    df4[a] = df4[a].astype(int)
pt_value4 = df4.T['営業社数'].astype(int).tolist()
eigyoshasuu4=df4.T['受注案件数'].astype(int).tolist()
point_PT4=df4.T['平均単価'].astype(int).tolist()
for i in range(len(colname)):
    a = colname[i]
    df4_1[a] = df4_1[a].astype(int)
pt_value4_1 = df4_1.T['営業社数'].astype(int).tolist()
eigyoshasuu4_1=df4_1.T['受注案件数'].astype(int).tolist()
point_PT4_1=df4_1.T['平均単価'].astype(int).tolist()

for i in range(len(colname)):
    a = colname[i]
    df4_2[a] = df4_2[a].astype(int)
pt_value4_2 = df4_2.T['営業社数'].astype(int).tolist()
eigyoshasuu4_2=df4_2.T['受注案件数'].astype(int).tolist()
point_PT4_2=df4_2.T['平均単価'].astype(int).tolist()

for i in range(len(colname)):
    a = colname[i]
    df4_3[a] = df4_3[a].astype(int)
pt_value4_3 = df4_3.T['営業社数'].astype(int).tolist()
eigyoshasuu4_3=df4_3.T['受注案件数'].astype(int).tolist()
point_PT4_3=df4_3.T['平均単価'].astype(int).tolist()

app = Flask(__name__)
@app.route('/')
def sample():
    global xls,most_recent_file
    global df, df_1, df_2, df_3, df2, df2_1, df2_2, df2_3, df3, df3_1, df3_2, df3_3, df4, df4_1, df4_2, df4_3, pt_value, pt_value_1, pt_value_2, pt_value_3, pt_value2, pt_value2_1, pt_value2_2, pt_value2_3, pt_value3, pt_value3_1, pt_value3_2, pt_value3_3, pt_value4, pt_value4_1, pt_value4_2, pt_value4_3, eigyoshasuu, eigyoshasuu_1, eigyoshasuu_2, eigyoshasuu_3, eigyoshasuu2, eigyoshasuu2_1, eigyoshasuu2_2, eigyoshasuu2_3, eigyoshasuu3, eigyoshasuu3_1, eigyoshasuu3_2, eigyoshasuu3_3, eigyoshasuu4, eigyoshasuu4_1, eigyoshasuu4_2, eigyoshasuu4_3, point_PT, point_PT_1, point_PT_2, point_PT_3, point_PT2, point_PT2_1, point_PT2_2, point_PT2_3, point_PT3, point_PT3_1, point_PT3_2, point_PT3_3, point_PT4, point_PT4_1, point_PT4_2, point_PT4_3
    most_recent_file_check = max(
        (os.path.join(root, f) for root, _, the_files in os.walk(path) for f in the_files if
         f.lower().endswith(".xlsx")),
        key=os.path.getmtime)
    print(most_recent_file_check)
    if(most_recent_file_check!=most_recent_file):
        print("loading new file")
        xls = pd.ExcelFile(most_recent_file_check)
        most_recent_file = most_recent_file_check
        df = pd.read_excel(xls, '月次進捗(事業ALL', parse_cols='B:AU', skiprows=28, index_col=0)
        df2 = pd.read_excel(xls, '月次進捗 (営業ALL (018を除く)', parse_cols='B:AU', skiprows=30, index_col=0)
        df3 = pd.read_excel(xls, '月次進捗 (営業 018生', parse_cols='B:AU', skiprows=27, index_col=0)
        df4 = pd.read_excel(xls, '月次進捗 (SSALL', parse_cols='B:AU', skiprows=30, index_col=0)
        #  df = pd.read_excel(r"C:\Users\pitchuka-ramana\PycharmProjects\Flask\行動指標管理web\data\【顧問】会議資料181213.xlsx",sheet_name='月次進捗(事業ALL',parse_cols='B:AO',skiprows = 28,index_col=0)
        df_1 = df.iloc[9:16]
        df_1 = df_1.dropna(axis=1)
        colname = df_1.columns.tolist()
        for i in range(len(colname)):
            print(i)
            # looping columns nowww
            if (i % 3 == 2):
                for j in range(7):
                    df_1.iloc[j][colname[i]] = (df_1.iloc[j][colname[i]] + df_1.iloc[j][colname[i - 1]] + df_1.iloc[j][
                        colname[i - 2]]) / 3
        # print(df_1.T)
        for i in range(len(colname)):

            if (i % 3 == 2):
                df_1 = df_1.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df_1 = df_1.drop([colname[i]], axis=1)
        print(df_1.columns.tolist())
        df_2 = df.iloc[99:106]
        df_2 = df_2.dropna(axis=1)
        colname = df_2.columns.tolist()
        for i in range(len(colname)):

            print(i)
            # looping columns nowww
            if (i % 3 == 2):
                for j in range(7):
                    df_2.iloc[j][colname[i]] = (df_2.iloc[j][colname[i]] + df_2.iloc[j][colname[i - 1]] + df_2.iloc[j][
                        colname[i - 2]]) / 3
        for i in range(len(colname)):

            if (i % 3 == 2):
                df_2 = df_2.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df_2 = df_2.drop([colname[i]], axis=1)
        # make a lot of temps
        # need to add more
        df_3 = df.iloc[135:142].add(df.iloc[144:149].reindex_like(df.iloc[135:142]), fill_value=0).add(
            df.iloc[151:158].reindex_like(df.iloc[135:142]), fill_value=0).add(
            df.iloc[160:167].reindex_like(df.iloc[135:142]), fill_value=0).add(
            df.iloc[169:176].reindex_like(df.iloc[135:142]), fill_value=0).add(
            df.iloc[178:185].reindex_like(df.iloc[135:142]), fill_value=0).add(
            df.iloc[185:192].reindex_like(df.iloc[135:142]), fill_value=0).add(
            df.iloc[194:201].reindex_like(df.iloc[135:142]), fill_value=0).add(
            df.iloc[203:210].reindex_like(df.iloc[135:142]), fill_value=0).add(
            df.iloc[212:219].reindex_like(df.iloc[135:142]), fill_value=0)
        df_3 = df_3.dropna(axis=1)
        colname = df_3.columns.tolist()
        for i in range(len(colname)):

            print(i)
            # looping columns nowww
            if (i % 3 == 2):
                for j in range(7):
                    df_3.iloc[j][colname[i]] = (df_3.iloc[j][colname[i]] + df_3.iloc[j][colname[i - 1]] + df_3.iloc[j][
                        colname[i - 2]]) / 3
        for i in range(len(colname)):

            if (i % 3 == 2):
                df_3 = df_3.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df_3 = df_3.drop([colname[i]], axis=1)

        # 2

        df2_1 = df2.iloc[11:18]
        df2_1 = df2_1.dropna(axis=1)
        colname = df2_1.columns.tolist()
        for i in range(len(colname)):

            print(i)
            # looping columns nowww
            if (i % 3 == 2):
                for j in range(7):
                    df2_1.iloc[j][colname[i]] = (df2_1.iloc[j][colname[i]] + df2_1.iloc[j][colname[i - 1]] +
                                                 df2_1.iloc[j][
                                                     colname[i - 2]]) / 3
        # print(df2_1.T)
        for i in range(len(colname)):

            if (i % 3 == 2):
                df2_1 = df2_1.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df2_1 = df2_1.drop([colname[i]], axis=1)

        df2_2 = df2.iloc[121:128]
        df2_2 = df2_2.dropna(axis=1)
        colname = df2_2.columns.tolist()
        for i in range(len(colname)):
            print(i)
            if (i % 3 == 2):
                for j in range(7):
                    df2_2.iloc[j][colname[i]] = (df2_2.iloc[j][colname[i]] + df2_2.iloc[j][colname[i - 1]] +
                                                 df2_2.iloc[j][
                                                     colname[i - 2]]) / 3
        for i in range(len(colname)):
            if (i % 3 == 2):
                df2_2 = df2_2.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df2_2 = df2_2.drop([colname[i]], axis=1)

        df2_3 = df2.iloc[165:172].add(df2.iloc[176:183].reindex_like(df2.iloc[165:172]), fill_value=0).add(
            df2.iloc[187:194].reindex_like(df2.iloc[165:172]), fill_value=0).add(
            df2.iloc[198:205].reindex_like(df2.iloc[165:172]), fill_value=0).add(
            df2.iloc[209:216].reindex_like(df2.iloc[165:172]), fill_value=0).add(
            df2.iloc[220:227].reindex_like(df2.iloc[165:172]), fill_value=0).add(
            df2.iloc[231:238].reindex_like(df2.iloc[165:172]), fill_value=0).add(
            df2.iloc[242:249].reindex_like(df2.iloc[165:172]), fill_value=0).add(
            df2.iloc[253:260].reindex_like(df2.iloc[165:172]), fill_value=0).add(
            df2.iloc[264:271].reindex_like(df2.iloc[165:172]), fill_value=0)

        df2_3 = df2_3.dropna(axis=1)
        colname = df2_3.columns.tolist()
        for i in range(len(colname)):
            print(i)
            if (i % 3 == 2):
                for j in range(7):
                    df2_3.iloc[j][colname[i]] = (df2_3.iloc[j][colname[i]] + df2_3.iloc[j][colname[i - 1]] +
                                                 df2_3.iloc[j][
                                                     colname[i - 2]]) / 3
        for i in range(len(colname)):
            if (i % 3 == 2):
                df2_3 = df2_3.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df2_3 = df2_3.drop([colname[i]], axis=1)

        # 3

        df3_1 = df3.iloc[11:18]
        df3_1 = df3_1.dropna(axis=1)
        colname = df3_1.columns.tolist()
        for i in range(len(colname)):
            if (i % 3 == 2):
                for j in range(7):
                    df3_1.iloc[j][colname[i]] = (df3_1.iloc[j][colname[i]] + df3_1.iloc[j][colname[i - 1]] +
                                                 df3_1.iloc[j][
                                                     colname[i - 2]]) / 3
        for i in range(len(colname)):
            if (i % 3 == 2):
                df3_1 = df3_1.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df3_1 = df3_1.drop([colname[i]], axis=1)

        df3_2 = df3.iloc[101:108]
        df3_2 = df3_2.dropna(axis=1)
        colname = df3_2.columns.tolist()
        for i in range(len(colname)):
            if (i % 3 == 2):
                for j in range(7):
                    df3_2.iloc[j][colname[i]] = (df3_2.iloc[j][colname[i]] + df3_2.iloc[j][colname[i - 1]] +
                                                 df3_2.iloc[j][
                                                     colname[i - 2]]) / 3
        for i in range(len(colname)):
            if (i % 3 == 2):
                df3_2 = df3_2.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df3_2 = df3_2.drop([colname[i]], axis=1)
        df3_3 = df3.iloc[137:144].add(df3.iloc[146:153].reindex_like(df3.iloc[137:144]), fill_value=0).add(
            df3.iloc[155:162].reindex_like(df3.iloc[137:144]), fill_value=0).add(
            df3.iloc[164:171].reindex_like(df3.iloc[137:144]), fill_value=0).add(
            df3.iloc[173:180].reindex_like(df3.iloc[137:144]), fill_value=0).add(
            df3.iloc[182:189].reindex_like(df3.iloc[137:144]), fill_value=0).add(
            df3.iloc[191:198].reindex_like(df3.iloc[137:144]), fill_value=0).add(
            df3.iloc[200:207].reindex_like(df3.iloc[137:144]), fill_value=0).add(
            df3.iloc[209:216].reindex_like(df3.iloc[137:144]), fill_value=0).add(
            df3.iloc[218:225].reindex_like(df3.iloc[137:144]), fill_value=0)
        df3_3 = df3_3.dropna(axis=1)
        colname = df3_3.columns.tolist()
        for i in range(len(colname)):
            if (i % 3 == 2):
                for j in range(7):
                    df3_3.iloc[j][colname[i]] = (df3_3.iloc[j][colname[i]] + df3_3.iloc[j][colname[i - 1]] +
                                                 df3_3.iloc[j][
                                                     colname[i - 2]]) / 3
        for i in range(len(colname)):
            if (i % 3 == 2):
                df3_3 = df3_3.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df3_3 = df3_3.drop([colname[i]], axis=1)

        # 4

        df4_1 = df4.iloc[11:18]
        df4_1 = df4_1.dropna(axis=1)
        colname = df4_1.columns.tolist()
        for i in range(len(colname)):
            if (i % 3 == 2):
                for j in range(7):
                    df4_1.iloc[j][colname[i]] = (df4_1.iloc[j][colname[i]] + df4_1.iloc[j][colname[i - 1]] +
                                                 df4_1.iloc[j][
                                                     colname[i - 2]]) / 3
        for i in range(len(colname)):
            if (i % 3 == 2):
                df4_1 = df4_1.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df4_1 = df4_1.drop([colname[i]], axis=1)

        df4_2 = df4.iloc[111:118]
        df4_2 = df4_2.dropna(axis=1)
        colname = df4_2.columns.tolist()
        for i in range(len(colname)):
            if (i % 3 == 2):
                for j in range(7):
                    df4_2.iloc[j][colname[i]] = (df4_2.iloc[j][colname[i]] + df4_2.iloc[j][colname[i - 1]] +
                                                 df4_2.iloc[j][
                                                     colname[i - 2]]) / 3
        for i in range(len(colname)):
            if (i % 3 == 2):
                df4_2 = df4_2.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df4_2 = df4_2.drop([colname[i]], axis=1)
        df4_3 = df4.iloc[151:159].add(df4.iloc[161:169].reindex_like(df4.iloc[151:159]), fill_value=0).add(
            df4.iloc[171:179].reindex_like(df4.iloc[151:159]), fill_value=0).add(
            df4.iloc[181:189].reindex_like(df4.iloc[151:159]), fill_value=0).add(
            df4.iloc[191:199].reindex_like(df4.iloc[151:159]), fill_value=0).add(
            df4.iloc[201:209].reindex_like(df4.iloc[151:159]), fill_value=0).add(
            df4.iloc[211:219].reindex_like(df4.iloc[151:159]), fill_value=0).add(
            df4.iloc[221:229].reindex_like(df4.iloc[151:159]), fill_value=0).add(
            df4.iloc[231:239].reindex_like(df4.iloc[151:159]), fill_value=0).add(
            df4.iloc[241:249].reindex_like(df4.iloc[151:159]), fill_value=0)
        df4_3 = df4_3.dropna(axis=1)
        colname = df4_3.columns.tolist()
        for i in range(len(colname)):
            if (i % 3 == 2):
                for j in range(7):
                    df4_3.iloc[j][colname[i]] = (df4_3.iloc[j][colname[i]] + df4_3.iloc[j][colname[i - 1]] +
                                                 df4_3.iloc[j][
                                                     colname[i - 2]]) / 3
        for i in range(len(colname)):
            if (i % 3 == 2):
                df4_3 = df4_3.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df4_3 = df4_3.drop([colname[i]], axis=1)

        # ------------------------------------------------------df1------------------------------------------------ the one before was to initialize all
        # ------------------------------------------------------df1------------------------------------------------ the one before was to initialize all
        # ------------------------------------------------------df1------------------------------------------------ the one before was to initialize all
        # ------------------------------------------------------df1------------------------------------------------ the one before was to initialize all

        # df initialize
        df = df.iloc[0:7]
        df = df.dropna(axis=1)
        colname = df.columns.tolist()
        for i in range(len(colname)):
            if (i % 3 == 2):
                for j in range(7):
                    df.iloc[j][colname[i]] = (df.iloc[j][colname[i]] + df.iloc[j][colname[i - 1]] + df.iloc[j][
                        colname[i - 2]]) / 3
        for i in range(len(colname)):
            if (i % 3 == 2):
                df = df.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df = df.drop([colname[i]], axis=1)
        colname = df.columns.tolist()
        for i in range(len(colname)):
            a = colname[i]
            df[a] = df[a].astype(int)
        pt_value = df.T['営業社数'].astype(int).tolist()
        eigyoshasuu = df.T['受注案件数'].astype(int).tolist()
        point_PT = df.T['平均単価'].astype(int).tolist()

        for i in range(len(colname)):
            a = colname[i]
            df_1[a] = df_1[a].astype(int)
        pt_value_1 = df_1.T['営業社数'].astype(int).tolist()
        eigyoshasuu_1 = df_1.T['受注案件数'].astype(int).tolist()
        point_PT_1 = df_1.T['平均単価'].astype(int).tolist()

        for i in range(len(colname)):
            a = colname[i]
            df_2[a] = df_2[a].astype(int)
        pt_value_2 = df_2.T['営業社数'].astype(int).tolist()
        eigyoshasuu_2 = df_2.T['受注案件数'].astype(int).tolist()
        point_PT_2 = df_2.T['平均単価'].astype(int).tolist()

        for i in range(len(colname)):
            a = colname[i]
            df_3[a] = df_3[a].astype(int)
        pt_value_3 = df_3.T['営業社数'].astype(int).tolist()
        eigyoshasuu_3 = df_3.T['受注案件数'].astype(int).tolist()
        point_PT_3 = df_3.T['平均単価'].astype(int).tolist()
        # REALEND----------------------------------------------

        # ------------------------------------------------------df2------------------------------------------------
        df2 = df2.iloc[0:7]
        df2 = df2.dropna(axis=1)
        colname = df2.columns.tolist()
        for i in range(len(colname)):
            if (i % 3 == 2):
                for j in range(7):
                    df2.iloc[j][colname[i]] = (df2.iloc[j][colname[i]] + df2.iloc[j][colname[i - 1]] + df2.iloc[j][
                        colname[i - 2]]) / 3
        for i in range(len(colname)):
            if (i % 3 == 2):
                df2 = df2.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df2 = df2.drop([colname[i]], axis=1)
        colname = df2.columns.tolist()

        for i in range(len(colname)):
            a = colname[i]
            df2[a] = df2[a].astype(int)
        pt_value2 = df2.T['営業社数'].astype(int).tolist()
        eigyoshasuu2 = df2.T['受注案件数'].astype(int).tolist()
        point_PT2 = df2.T['平均単価'].astype(int).tolist()
        for i in range(len(colname)):
            a = colname[i]
            df2_1[a] = df2_1[a].astype(int)
        pt_value2_1 = df2_1.T['営業社数'].astype(int).tolist()
        eigyoshasuu2_1 = df2_1.T['受注案件数'].astype(int).tolist()
        point_PT2_1 = df2_1.T['平均単価'].astype(int).tolist()

        for i in range(len(colname)):
            a = colname[i]
            df2_2[a] = df2_2[a].astype(int)
        pt_value2_2 = df2_2.T['営業社数'].astype(int).tolist()
        eigyoshasuu2_2 = df2_2.T['受注案件数'].astype(int).tolist()
        point_PT2_2 = df2_2.T['平均単価'].astype(int).tolist()

        for i in range(len(colname)):
            a = colname[i]
            df2_3[a] = df2_3[a].astype(int)
        pt_value2_3 = df2_3.T['営業社数'].astype(int).tolist()
        eigyoshasuu2_3 = df2_3.T['受注案件数'].astype(int).tolist()
        point_PT2_3 = df2_3.T['平均単価'].astype(int).tolist()

        # ------------------------------------------------------df3------------------------------------------------
        df3 = df3.iloc[0:7]
        df3 = df3.dropna(axis=1)
        colname = df3.columns.tolist()
        for i in range(len(colname)):
            if (i % 3 == 2):
                for j in range(7):
                    df3.iloc[j][colname[i]] = (df3.iloc[j][colname[i]] + df3.iloc[j][colname[i - 1]] + df3.iloc[j][
                        colname[i - 2]]) / 3
        for i in range(len(colname)):

            if (i % 3 == 2):
                df3 = df3.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df3 = df3.drop([colname[i]], axis=1)
        colname = df3.columns.tolist()
        for i in range(len(colname)):
            a = colname[i]
            df3[a] = df3[a].astype(int)
        pt_value3 = df3.T['営業社数'].astype(int).tolist()
        eigyoshasuu3 = df3.T['受注案件数'].astype(int).tolist()
        point_PT3 = df3.T['平均単価'].astype(int).tolist()
        for i in range(len(colname)):
            a = colname[i]
            df3_1[a] = df3_1[a].astype(int)
        pt_value3_1 = df3_1.T['営業社数'].astype(int).tolist()
        eigyoshasuu3_1 = df3_1.T['受注案件数'].astype(int).tolist()
        point_PT3_1 = df3_1.T['平均単価'].astype(int).tolist()

        for i in range(len(colname)):
            a = colname[i]
            df3_2[a] = df3_2[a].astype(int)
        pt_value3_2 = df3_2.T['営業社数'].astype(int).tolist()
        eigyoshasuu3_2 = df3_2.T['受注案件数'].astype(int).tolist()
        point_PT3_2 = df3_2.T['平均単価'].astype(int).tolist()

        for i in range(len(colname)):
            a = colname[i]
            df3_3[a] = df3_3[a].astype(int)
        pt_value3_3 = df3_3.T['営業社数'].astype(int).tolist()
        eigyoshasuu3_3 = df3_3.T['受注案件数'].astype(int).tolist()
        point_PT3_3 = df3_3.T['平均単価'].astype(int).tolist()
        # ------------------------------------------------------df4------------------------------------------------
        df4 = df4.iloc[0:7]
        df4 = df4.dropna(axis=1)
        colname = df4.columns.tolist()
        for i in range(len(colname)):
            if (i % 3 == 2):
                for j in range(7):
                    df4.iloc[j][colname[i]] = (df4.iloc[j][colname[i]] + df4.iloc[j][colname[i - 1]] + df4.iloc[j][
                        colname[i - 2]]) / 3
        for i in range(len(colname)):
            if (i % 3 == 2):
                df4 = df4.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
            else:
                df4 = df4.drop([colname[i]], axis=1)
        colname = df4.columns.tolist()
        for i in range(len(colname)):
            a = colname[i]
            df4[a] = df4[a].astype(int)
        pt_value4 = df4.T['営業社数'].astype(int).tolist()
        eigyoshasuu4 = df4.T['受注案件数'].astype(int).tolist()
        point_PT4 = df4.T['平均単価'].astype(int).tolist()
        for i in range(len(colname)):
            a = colname[i]
            df4_1[a] = df4_1[a].astype(int)
        pt_value4_1 = df4_1.T['営業社数'].astype(int).tolist()
        eigyoshasuu4_1 = df4_1.T['受注案件数'].astype(int).tolist()
        point_PT4_1 = df4_1.T['平均単価'].astype(int).tolist()

        for i in range(len(colname)):
            a = colname[i]
            df4_2[a] = df4_2[a].astype(int)
        pt_value4_2 = df4_2.T['営業社数'].astype(int).tolist()
        eigyoshasuu4_2 = df4_2.T['受注案件数'].astype(int).tolist()
        point_PT4_2 = df4_2.T['平均単価'].astype(int).tolist()

        for i in range(len(colname)):
            a = colname[i]
            df4_3[a] = df4_3[a].astype(int)
        pt_value4_3 = df4_3.T['営業社数'].astype(int).tolist()
        eigyoshasuu4_3 = df4_3.T['受注案件数'].astype(int).tolist()
        point_PT4_3 = df4_3.T['平均単価'].astype(int).tolist()
    else:
        print("no new load")

    return render_template('index.html', df=df.to_html(),df_1=df_1.to_html(),df_2=df_2.to_html(),df_3=df_3.to_html(),df2=df2.to_html(),df2_1=df2_1.to_html(),df2_2=df2_2.to_html(),df2_3=df2_3.to_html(),df3=df3.to_html(),df3_1=df3_1.to_html(),df3_2=df3_2.to_html(),df3_3=df3_3.to_html(),df4=df4.to_html(),df4_1=df4_1.to_html(),df4_2=df4_2.to_html(),df4_3=df4_3.to_html(),
                           pt_value1_0=pt_value,eigyoshasuu1_0=eigyoshasuu,point_PT1_0=point_PT,pt_value1_1=pt_value_1,eigyoshasuu1_1=eigyoshasuu_1,point_PT1_1=point_PT_1,pt_value1_2=pt_value_2,eigyoshasuu1_2=eigyoshasuu_2,point_PT1_2=point_PT_2,pt_value1_3=pt_value_3,eigyoshasuu1_3=eigyoshasuu_3,point_PT1_3=point_PT_3,
                           pt_value2_0=pt_value2,eigyoshasuu2_0=eigyoshasuu2,point_PT2_0=point_PT2,pt_value2_1=pt_value2_1,eigyoshasuu2_1=eigyoshasuu2_1,point_PT2_1=point_PT2_1,pt_value2_2=pt_value2_2,eigyoshasuu2_2=eigyoshasuu2_2,point_PT2_2=point_PT2_2,pt_value2_3=pt_value2_3,eigyoshasuu2_3=eigyoshasuu2_3,point_PT2_3=point_PT2_3,
                           pt_value3_0=pt_value3,eigyoshasuu3_0=eigyoshasuu3,point_PT3_0=point_PT3,pt_value3_1=pt_value3_1,eigyoshasuu3_1=eigyoshasuu3_1,point_PT3_1=point_PT3_1,pt_value3_2=pt_value3_2,eigyoshasuu3_2=eigyoshasuu3_2,point_PT3_2=point_PT3_2,pt_value3_3=pt_value3_3,eigyoshasuu3_3=eigyoshasuu3_3,point_PT3_3=point_PT3_3,
                           pt_value4_0=pt_value4,eigyoshasuu4_0=eigyoshasuu4,point_PT4_0=point_PT4,pt_value4_1=pt_value4_1,eigyoshasuu4_1=eigyoshasuu4_1,point_PT4_1=point_PT4_1,pt_value4_2=pt_value4_2,eigyoshasuu4_2=eigyoshasuu4_2,point_PT4_2=point_PT4_2,pt_value4_3=pt_value4_3,eigyoshasuu4_3=eigyoshasuu4_3,point_PT4_3=point_PT4_3)

if __name__ == '__main__':
     app.run(host = "0.0.0.0",debug = True,port = 5001)
#    app.run(debug = True,port = 5001)

