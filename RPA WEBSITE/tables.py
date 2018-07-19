from flask_table import Table, Col, LinkCol


class Results(Table):
    id = Col('ID', show=False)
    robotname = Col('ロボット名')
    iraisha = Col('依頼者')
    busho = Col('部署')
    developer = Col('作成者')
    last_mod = Col('最終更新日')
    remark = Col('備考')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))


