# forms.py

from wtforms import Form, StringField, SelectField,TextAreaField,FieldList,FormField,SelectMultipleField
from wtforms.fields.html5 import DateField
from wtforms.widgets import TextArea
from wtforms import widgets
from wtforms.validators import InputRequired,Optional,Length


class CustomDateInput(widgets.TextInput):
    input_type = 'date'

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
class twomonthplusform(Form):

        contact_methods = [('電話', '電話'),
               ('メール（送付）', 'メール（送付）'),
               ('メール（返信）', 'メール（返信）'),
                ]
        contact_cont1 = [('会食打診した→日程確定', '会食打診した→日程確定'),
               ('会食打診した→日程調整中', '会食打診した→日程調整中'),
               ('会食打診した→断られた', '会食打診した→断られた'),
               ('会食打診した→返事待ち', '会食打診した→返事待ち'),
               ('会食打診せず', '会食打診せず'),
                ]
        contact_cont2 = [('訪問打診した→日程確定', '訪問打診した→日程確定'),
                         ('訪問打診した→日程調整中', '訪問打診した→日程調整中'),
                         ('訪問打診した→断られた', '訪問打診した→断られた'),
                         ('訪問打診した→返事待ち', '訪問打診した→返事待ち'),
                         ('訪問打診せず', '訪問打診せず'),
                         ]
        contact_cont3 = [('紹介打診した→紹介受領', '紹介打診した→紹介受領'),
                         ('紹介打診した→断られた', '紹介打診した→断られた'),
                         ('紹介打診した→返事待ち', '紹介打診した→返事待ち'),
                         ('紹介打診せず', '紹介打診せず'),
                         ]
        questionnaire= [('とても良い', 'とても良い'),
                   ('良い', '良い'),
                   ('どちらとも言えない', 'どちらとも言えない'),
                   ('悪い', '悪い'),
                   ('とても悪い', 'とても悪い'),
                            ]
        dashinsinairiyuu= [('成約済', '成約済'),
                   ('成約はしていないが、設定は順調', '成約はしていないが、設定は順調'),
                   ('進捗は良くないが、それに対し社長納得済', '進捗は良くないが、それに対し社長納得済'),
                   ('進捗は良くないが、直近てこ入れ済', '進捗は良くないが、直近てこ入れ済'),
                            ]
        dashinsinairiyuu_comp= [('直近訪問済', '直近訪問済'),
                           ('紹介受領できる間柄かつリピートを頂戴済', '紹介受領できる間柄かつリピートを頂戴済'),
                           ('優良な紹介をみこめないかつリピートをレとイスして取りたくない', '優良な紹介をみこめないかつリピートをレイスとして取りたくない'),
                            ]
        dashinyn= [
                  #
                    ('打診する', '打診する'),
                   ('打診しない','打診しない'),
                            ]
        compname = StringField(label='企業名',widget=widgets.TextInput(),render_kw={'class': 'form-control'})
        contdate = DateField('連絡日',render_kw={'class': 'form-control'},format='%Y-%m-%d')

        contactmeth=SelectField('連絡方法',choices=contact_methods,widget=widgets.Select(),render_kw={'class': 'form-control'})
        concont1date=DateField('concont1date',render_kw={'class': 'form-control'})
        concont1name=TextAreaField('concont1name',widget=widgets.TextInput(),render_kw={'class': 'form-control'},default="")
        concont2date=TextAreaField('concont1date',render_kw={'class': 'form-control'})
        concont2name=TextAreaField('concont1name',widget=widgets.TextInput(),render_kw={'class': 'form-control'},default="")
        concont3date=TextAreaField('concont1date',render_kw={'class': 'form-control'})
        concont3name=TextAreaField('concont1name',widget=widgets.TextInput(),render_kw={'class': 'form-control'},default="")
        contactcontent1=SelectField('連絡内容①',choices=contact_cont1,widget=widgets.Select(),render_kw={'class': 'form-control'})
        contactcontent2=SelectField('連絡内容②',choices=contact_cont2,widget=widgets.Select(),render_kw={'class': 'form-control'})
        contactcontent3=SelectField('連絡内容③',choices=contact_cont3,widget=widgets.Select(),render_kw={'class': 'form-control'})
        yaritoricont=TextAreaField('やりとりした内容',widget=widgets.TextInput(),render_kw={'class': 'form-control'},default="")
        q1= SelectField('自分とのリレーションレベル                                                                                                                      (リレーションレベルの「とても良い」とは「どんな話題でも気軽に連絡できる」)',choices=questionnaire,widget=widgets.Select(),render_kw={'class': 'form-control'},default="どちらとも言えない")
        q2= SelectField('スカウトサービスへの満足度',choices=questionnaire,widget=widgets.Select(),render_kw={'class': 'form-control'},default="どちらとも言えない")
        houmondashin=SelectField('訪問打診するか',choices=dashinyn,widget=widgets.Select(),render_kw={'class': 'form-control'})
        dashinshinai=SelectField('理由',choices=dashinsinairiyuu,widget=widgets.Select(),render_kw={'class': 'form-control'})
        dashinshinai_comp=SelectField('理由',choices=dashinsinairiyuu_comp,widget=widgets.Select(),render_kw={'class': 'form-control'})


class homon_kai(Form):
    questionnaire = [('とても良い', 'とても良い'),
                     ('良い', '良い'),
                     ('どちらとも言えない', 'どちらとも言えない'),
                     ('悪い', '悪い'),
                     ('とても悪い', 'とても悪い'),
                     ]
    contact_methods = [('訪問', '訪問'),
                       ('会食', '会食'),
                       ]
    rec=[('紹介', '紹介'),
                       ('リピート／追加受注', 'リピート／追加受注'),('クロスセル', 'クロスセル'),
                       ]
    compname = StringField(label='企業名', widget=widgets.TextInput(), render_kw={'class': 'form-control'})
    contdate = DateField('連絡日', render_kw={'class': 'form-control'},format='%Y-%m-%d')

    contactmeth = SelectField('連絡方法', choices=contact_methods, widget=widgets.Select(),
                              render_kw={'class': 'form-control'})
    clients = StringField(label='クライアント参加者', widget=widgets.TextInput(), render_kw={'class': 'form-control'})
    raynos = StringField(label='自身以外のレイノス参加者', widget=widgets.TextInput(), render_kw={'class': 'form-control'})
    recieved=SelectMultipleField('頂いたもの', choices=rec, widget=widgets.Select(multiple=True),
                              render_kw={'class': 'form-control'})
    yaritoricont = TextAreaField('やりとりした内容', widget=widgets.TextInput(), render_kw={'class': 'form-control'},
                                 default="")

    q1 = SelectField('自分とのリレーションレベル                                                                                                                                                                    (リレーションレベルの「とても良い」とは「どんな話題でも気軽に連絡できる」)', choices=questionnaire, widget=widgets.Select(),
                     render_kw={'class': 'form-control'}, default="どちらとも言えない")
    q2 = SelectField('スカウトサービスへの満足度', choices=questionnaire, widget=widgets.Select(),
                     render_kw={'class': 'form-control'}, default="どちらとも言えない")