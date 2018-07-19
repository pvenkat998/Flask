from wtforms import Form, StringField, SelectField,TextAreaField,FieldList,FormField
from wtforms.fields.html5 import DateField
from wtforms.widgets import TextArea
from wtforms import widgets
from wtforms.validators import InputRequired,Optional,Length,DataRequired,ValidationError

from datetime import date
class pointform(Form):
    startdate = DateField('StartDate', render_kw={'class': 'form-control'}, validators=[DataRequired(message="日付は正しく入力されていません")],)
    enddate = DateField('EndDate', render_kw={'class': 'form-control'}, default=date.today() ,validators=[DataRequired(message="日付は正しく入力されていません")],)
class yoteipoints(Form):
    denwasuu = TextAreaField('電話数', widget=widgets.TextInput(), render_kw={'class': 'form-control'})
    tsunasuu = TextAreaField('つな数', widget=widgets.TextInput(), render_kw={'class': 'form-control'})
    apo = TextAreaField('アポ', widget=widgets.TextInput(), render_kw={'class': 'form-control'})
