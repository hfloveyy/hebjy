from app import db

jianqu_names = ['一监区','二监区','三监区','四监区','五监区','六监区','七监区',
'八监区','九监区','十监区','十一监区','十二监区','后勤监区','外籍监区','集训监区','出监监区','病犯监区','禁闭、严管','高戒备','改造业务科室','管理员']

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(20), index = True)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class UploadForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jianqu = db.Column(db.String(20), index=True, unique=True)
    zhibanlingdao = db.Column(db.String(20), index=True, unique=True)
    baitianzaigang = db.Column(db.String(20), index=True, unique=True)
    yejianzhiban = db.Column(db.String(20), index=True, unique=True)
    zaice = db.Column(db.String(20), index=True, unique=True)
    shiyou = db.Column(db.String(20), index=True, unique=True)
    chugong = db.Column(db.String(20), index=True, unique=True)
    beizhu = db.Column(db.String(20), index=True, unique=True)
    createtime = db.Column(db.String(20), index=True, unique=True)

class KanshouForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zhibanlingdao = db.Column(db.String(20), index=True, unique=True)
    damen = db.Column(db.String(20), index=True, unique=True)
    ermen = db.Column(db.String(20), index=True, unique=True)
    sanmen = db.Column(db.String(20), index=True, unique=True)
    beizhu = db.Column(db.String(20), index=True, unique=True)
    createtime = db.Column(db.String(20), index=True, unique=True)

class TongbaoForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    createtime = db.Column(db.String(500), index=True, unique=True)
    jianguan = db.Column(db.String(500), index=True, unique=True)
    jingwu = db.Column(db.String(500), index=True, unique=True)
    yuqing = db.Column(db.String(500), index=True, unique=True)
    shengchan = db.Column(db.String(500), index=True, unique=True)


def init_db():
    users = []
    for name in jianqu_names:
        users.append(User(nickname=name, password='1'))
    for user in users:
        db.session.add(user)
        db.session.commit()