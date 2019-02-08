from flask import Flask, render_template, url_for, request
import pandas as pd
import datetime
import os
#from openpyxl import load_workbook

app = Flask(__name__)

@app.route('/')
def sample():
    path="\\\\172.16.0.232\CoffeeCrazy3\その他\受け渡し用\\20180703橋本さん受け渡し用\加工済み会議資料\\0207顧問"
    print(path)
    most_recent_file = max((os.path.join(root, f) for root, _, the_files in os.walk(path) for f in the_files if f.lower().endswith(".xlsx")), key=os.path.getctime)
    print(most_recent_file)
    xls = pd.ExcelFile(r"\\172.16.0.232\CoffeeCrazy3\その他\受け渡し用\20180703橋本さん受け渡し用\加工済み会議資料\0207顧問\【顧問】会議資料190207.xlsx")
    df = pd.read_excel(xls, '月次進捗(事業ALL',parse_cols='B:AO',skiprows = 28,index_col=0)
    df2 = pd.read_excel(xls, '月次進捗 (営業ALL (018を除く)',parse_cols='B:AO',skiprows = 30,index_col=0)
    df3 = pd.read_excel(xls, '月次進捗 (営業 018生',parse_cols='B:AO',skiprows = 27,index_col=0)
    df4 = pd.read_excel(xls, '月次進捗 (SSALL',parse_cols='B:AO',skiprows = 30,index_col=0)
  #  df = pd.read_excel(r"C:\Users\pitchuka-ramana\PycharmProjects\Flask\行動指標管理web\data\【顧問】会議資料181213.xlsx",sheet_name='月次進捗(事業ALL',parse_cols='B:AO',skiprows = 28,index_col=0)
    df=df.iloc[0:7]
    df = df.dropna(axis = 1)
    colname = df.columns.tolist()

    for i in range(len(colname)):
        1==1
        print(i)
        #looping columns nowww
        if(i%3==2):
            for j in range(7):
                df.iloc[j][colname[i]]=(df.iloc[j][colname[i]]+df.iloc[j][colname[i-1]]+df.iloc[j][colname[i-2]])/3
   # print(df.T)
    for i in range(len(colname)):

        if(i%3==2):
            df = df.rename(columns={colname[i]: str(colname[i-2])[:7]+'-'+str(colname[i])[:7]})
        else:
            df=df.drop([colname[i]], axis=1)

    colname = df.columns.tolist()

    pt_value = df.T['営業社数'].astype(int).tolist()
    for i in range(len(colname)):
        a = colname[i]
        df[a] = df[a].astype(int)
    #print(df)
    eigyoshasuu=df.T['受注案件数'].astype(int).tolist()
    for i in range(len(colname)):
        a=colname[i]
        df[a]=df[a].astype(int)
    point_PT=df.T['平均単価'].astype(int).tolist()
    for i in range(len(colname)):
        a=colname[i]
        df[a]=df[a].astype(int)

    #------------------------------------------------------df2------------------------------------------------
    df2=df2.iloc[0:7]
    df2 = df2.dropna(axis = 1)
    colname = df2.columns.tolist()

    for i in range(len(colname)):
        1 == 1
        print(i)
        # looping columns nowww
        if (i % 3 == 2):
            for j in range(7):
                df2.iloc[j][colname[i]] = (df2.iloc[j][colname[i]] + df2.iloc[j][colname[i - 1]] + df2.iloc[j][
                    colname[i - 2]]) / 3
    # print(df.T)
    for i in range(len(colname)):

        if (i % 3 == 2):
            df2 = df2.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
        else:
            df2 = df2.drop([colname[i]], axis=1)

    colname = df2.columns.tolist()

    pt_value2 = df2.T['営業社数'].astype(int).tolist()
    for i in range(len(colname)):
        a = colname[i]
        df2[a] = df2[a].astype(int)
    #print(df2)
    eigyoshasuu2=df2.T['受注案件数'].astype(int).tolist()
    for i in range(len(colname)):
        a=colname[i]
        df2[a]=df2[a].astype(int)
    point_PT2=df2.T['平均単価'].astype(int).tolist()
    for i in range(len(colname)):
        a=colname[i]
        df2[a]=df2[a].astype(int)

    #------------------------------------------------------df3------------------------------------------------

    df3=df3.iloc[0:7]
    df3 = df3.dropna(axis = 1)
    colname = df3.columns.tolist()

    for i in range(len(colname)):
        1 == 1
        print(i)
        # looping columns nowww
        if (i % 3 == 2):
            for j in range(7):
                df3.iloc[j][colname[i]] = (df3.iloc[j][colname[i]] + df3.iloc[j][colname[i - 1]] + df3.iloc[j][
                    colname[i - 2]]) / 3
    # print(df3.T)
    for i in range(len(colname)):

        if (i % 3 == 2):
            df3 = df3.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
        else:
            df3 = df3.drop([colname[i]], axis=1)

    colname = df3.columns.tolist()

    pt_value3 = df3.T['営業社数'].astype(int).tolist()
    for i in range(len(colname)):
        a = colname[i]
        df3[a] = df3[a].astype(int)
    #print(df3)
    eigyoshasuu3=df3.T['受注案件数'].astype(int).tolist()
    for i in range(len(colname)):
        a=colname[i]
        df3[a]=df3[a].astype(int)
    point_PT3=df3.T['平均単価'].astype(int).tolist()
    for i in range(len(colname)):
        a=colname[i]
        df3[a]=df3[a].astype(int)
    #------------------------------------------------------df4------------------------------------------------

    #df4
    df4=df4.iloc[0:7]
    df4 = df4.dropna(axis = 1)
    colname = df4.columns.tolist()

    for i in range(len(colname)):
        1 == 1
        print(i)
        # looping columns nowww
        if (i % 3 == 2):
            for j in range(7):
                df4.iloc[j][colname[i]] = (df4.iloc[j][colname[i]] + df4.iloc[j][colname[i - 1]] + df4.iloc[j][
                    colname[i - 2]]) / 3
    # print(df4.T)
    for i in range(len(colname)):

        if (i % 3 == 2):
            df4 = df4.rename(columns={colname[i]: str(colname[i - 2])[:7] + '-' + str(colname[i])[:7]})
        else:
            df4 = df4.drop([colname[i]], axis=1)

    colname = df4.columns.tolist()

    pt_value4 = df4.T['営業社数'].astype(int).tolist()
    for i in range(len(colname)):
        a = colname[i]
        df4[a] = df4[a].astype(int)
    #print(df4)
    eigyoshasuu4=df4.T['受注案件数'].astype(int).tolist()
    for i in range(len(colname)):
        a=colname[i]
        df4[a]=df4[a].astype(int)
    point_PT4=df4.T['平均単価'].astype(int).tolist()
    for i in range(len(colname)):
        a=colname[i]
        df4[a]=df4[a].astype(int)


    return render_template('index.html', df=df.to_html(),df2=df2.to_html(),df3=df3.to_html(),df4=df4.to_html(),pt_value=pt_value,eigyoshasuu=eigyoshasuu,point_PT=point_PT,pt_value2=pt_value2,eigyoshasuu2=eigyoshasuu2,point_PT2=point_PT2,pt_value3=pt_value3,eigyoshasuu3=eigyoshasuu3,point_PT3=point_PT3,pt_value4=pt_value4,eigyoshasuu4=eigyoshasuu4,point_PT4=point_PT4)

if __name__ == '__main__':
     app.run(host = "0.0.0.0",debug = True,port = 5001)
#    app.run(debug = True,port = 5001)

