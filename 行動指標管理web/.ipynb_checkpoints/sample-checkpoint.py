from flask import Flask, render_template, url_for, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def sample():
    df = pd.read_excel(r"C:\Users\shiozawa\Desktop\workspace\websystem\行動指標管理web\data\sie_pt.xlsx",index_col=0)
    df = df.dropna(axis = 1)
    colname = df.columns.tolist()
    pt_value = df.T["総額"].astype(int).tolist()
    for i in range(len(colname)):
        a = colname[i]
        df[a] = df[a].astype(int)
    return render_template('index.html', df=df.to_html(),pt_value=pt_value)

if __name__ == '__main__':
     app.run(host = "0.0.0.0",debug = True,port = 5001)
#    app.run(debug = True,port = 5001)

