from flask_wtf import Form
from wtforms import PasswordField
from wtforms import SelectField
from wtforms.validators import DataRequired



jianqu_names = [('1','一监区'),('2','二监区'),('3','三监区'),('4','四监区'),('5','五监区'),('6','六监区'),('7','七监区'),('8','八监区'),
                ('9', '九监区'), ('10', '十监区'), ('11', '十一监区'), ('12', '十二监区'),('13', '后勤监区'), ('14', '外籍监区'), ('15', '集训监区'), ('16', '出监监区'),
                ('17', '病犯监区'), ('18', '禁闭、严管'), ('19', '高戒备'), ('20', '改造业务科室'), ('21', '看守大队'),('22', '管理员')]

class LoginForm(Form):
    name = SelectField('name', validators=[DataRequired()],choices= jianqu_names)
    password = PasswordField('password',validators=[DataRequired()])