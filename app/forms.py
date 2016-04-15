from flask_wtf import Form
from wtforms import PasswordField
from wtforms import SelectField
from wtforms import StringField
from wtforms.validators import DataRequired



jianqu_names = [('一监区','一监区'),('二监区','二监区'),('三监区','三监区'),('四监区','四监区'),('五监区','五监区'),('六监区','六监区'),('七监区','七监区'),('八监区','八监区'),
                ('九监区', '九监区'), ('十监区', '十监区'), ('十一监区', '十一监区'), ('十二监区', '十二监区'),('后勤监区', '后勤监区'), ('外籍监区', '外籍监区'), ('集训监区', '集训监区'), ('出监监区', '出监监区'),
                ('病犯监区', '病犯监区'), ('禁闭、严管', '禁闭、严管'), ('高戒备', '高戒备'), ('改造业务科室', '改造业务科室'), ('看守大队', '看守大队'),('管理员', '管理员')]

class LoginForm(Form):
    name = SelectField('name', validators=[DataRequired()],choices= jianqu_names)
    password = PasswordField('password',validators=[DataRequired()])

class ReportForm(Form):
    zhibanlingdao = StringField('zhibanlingdao', validators=[DataRequired()])
    baitianzaigang = StringField('baitianzaigang', validators=[DataRequired()])
    yejianzhiban = StringField('yejianzhiban', validators=[DataRequired()])
    zaice = StringField('zaice', validators=[DataRequired()])
    shiyou = StringField('shiyou', validators=[DataRequired()])
    chugong = StringField('chugong', validators=[DataRequired()])
    beizhu = StringField('beizhu', validators=[DataRequired()])

class KanshouForm(Form):
    zhibanlingdao = StringField('zhibanlingdao', validators=[DataRequired()])
    damen = StringField('damen', validators=[DataRequired()])
    ermen = StringField('ermen', validators=[DataRequired()])
    sanmen = StringField('sanmen', validators=[DataRequired()])
    beizhu = StringField('beizhu', validators=[DataRequired()])