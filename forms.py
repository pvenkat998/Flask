# forms.py

from wtforms import Form, StringField, SelectField,TextAreaField,FieldList,FormField
from wtforms.fields.html5 import DateField
from wtforms.widgets import TextArea
from wtforms import widgets
from wtforms.validators import InputRequired,Optional,Length



class MusicSearchForm(Form):
    choices = [('松本', '松本'),
               ('井上', '井上'),
               ('李そ', '李そ'),
               ('廣瀬', '廣瀬'),
               ('ピチュカ', 'ピチュカ'),
               ('澤山', '澤山')]
    select = SelectField('Search for music:', choices=choices)
    search = StringField('')

class AlbumForm(Form):
    media_types = [('Digital', 'Digital'),
                   ('CD', 'CD'),
                   ('Cassette Tape', 'Cassette Tape')
                   ]
    artist = StringField('Artist')
    title = StringField('Title')
    release_date = StringField('Release Date')
    publisher = StringField('Publisher')
    media_type = SelectField('Media', choices=media_types)
class LogForm(Form):
             logdate = StringField('Date',render_kw={'class': 'form-control'})
             logcont = TextAreaField('aa',widget=widgets.TextInput(),render_kw={'class': 'form-control'})
             logid = StringField('ID',render_kw={'class': 'form-control'})
class Robotform(Form):
        dept = [('SK', 'SK'),
               ('顧問', '顧問'),
               ('レイサス', 'レイサス'),
               ('mode', 'mode'),
               ('SC', 'SC'),
               ('システム課', 'システム課'),
               ('業推全体', '業推全体'),
               ('PDM', 'PDM'),
               ('経理', '経理・総務'),
               ('グレコミ', 'グレコミ'),
               ('ロンザン', 'ロンザン'),
               ('レイサスプロモ', 'レイサスプロモ'),
               ('社長名鑑', '社長名鑑'),
               ('ダウンロード', 'ダウンロード'),
               ('リストアップ', 'リストアップ'),
               ('その他', 'その他'),]
        inout=[('インプット', 'インプット'),
               ('アウトプット', 'アウトプット'),]
        kan=[('未完成', '未完成'),
               ('仮完成', '仮完成'),
               ('完成', '完成'),
             ]
        shurui = [('エクセルファイル', 'エクセルファイル'),
                   ('ファイル', 'ファイル'),
                   ('PDF', 'PDF'),
                   ('スプレッドシート', 'スプレッドシート'),
                   ('グーグルドライブ（スプレッド以外', 'スプレッド以外'),
                   ('ウェブサイト', 'ウェブサイト'),
                   ('データベース', 'データベース'),
                   ('CSV', 'CSV'),
                   ('PHP', 'PHP'),
                   ('メール配信', 'メール配信'),
                   ('グーグルフォーム', 'グーグルフォーム'),
                   ('その他', 'その他'),
                  ]
        media_types = [('松本', '松本'),
               ('井上', '井上'),
               ('李そ', '李そ'),
               ('廣瀬', '廣瀬'),
               ('ピチュカ', 'ピチュカ'),
               ('澤山', '澤山'),]
        robotname = StringField(label='ロボット名',widget=widgets.TextInput(),render_kw={'class': 'form-control'}
)
        iraisha= StringField(label='依頼者',widget=widgets.TextInput(),render_kw={'class': 'form-control'})
        busho=SelectField('部署',choices=dept,widget=widgets.Select(),render_kw={'class': 'form-control'})
        developer= SelectField('作成者',choices=media_types,widget=widgets.Select(),render_kw={'class': 'form-control'})
        last_mod = DateField('最終更新日',render_kw={'class': 'form-control'})
        schedule= StringField(label='スケジュール',widget=widgets.TextInput(),render_kw={'class': 'form-control'})
   #     schedule = TextAreaField('スケジュール', render_kw={"rows": 3, "cols": 20})
        log=TextAreaField('新ログ登録',widget=widgets.TextInput(),render_kw={'class': 'form-control'})
        obje=TextAreaField('目的・背景', render_kw={"rows": 3, "cols": 50})
        gaiyo=TextAreaField('概要', render_kw={"rows": 3, "cols": 50})
        kansei= SelectField('完成',choices=kan,widget=widgets.Select(),render_kw={'class': 'form-control'})
        sakujikan=StringField("削減時間",render_kw={'class': 'form-control'})
        sakujikannote = TextAreaField("削減時間ノート",widget=widgets.TextInput(), render_kw={'class': 'form-control'})
        inout= SelectField('イン・アウト',choices=inout,widget=widgets.Select(),render_kw={'class': 'form-control'})
        sourcetype=SelectField('ソースタイプ',choices=shurui,widget=widgets.Select(),render_kw={'class': 'form-control'})
        sourceinfo=TextAreaField(label='ソース場所',widget=widgets.TextInput(),render_kw={'class': 'form-control'})
        sourceuse=TextAreaField(label='利用詳細',widget=widgets.TextInput(),render_kw={'class': 'form-control'})
        deadline=TextAreaField(label='締切',widget=widgets.TextInput(),render_kw={'class': 'form-control'})
        logout=FieldList(FormField(LogForm))




