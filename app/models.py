from app import db

jianqu_names = ['一监区','二监区','三监区','四监区','五监区','六监区','七监区',
'八监区','九监区','十监区','十一监区','十二监区','后勤监区','外籍监区','集训监区','出监监区','病犯监区','禁闭、严管','高戒备','看守大队','改造业务科室','管理员']

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


class ReportModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jianqu = db.Column(db.String(20), index=True)
    zhibanlingdao = db.Column(db.String(20), index=True)
    baitianzaigang = db.Column(db.String(20), index=True)
    yejianzhiban = db.Column(db.String(20), index=True)
    zaice = db.Column(db.String(20), index=True)
    shiyou = db.Column(db.String(20), index=True)
    chugong = db.Column(db.String(20), index=True)
    beizhu = db.Column(db.String(20), index=True)
    createtime = db.Column(db.String(20), index=True, unique=True)

class KanshouModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zhibanlingdao = db.Column(db.String(20), index=True)
    damen = db.Column(db.String(20), index=True)
    ermen = db.Column(db.String(20), index=True)
    sanmen = db.Column(db.String(20), index=True)
    beizhu = db.Column(db.String(20), index=True)
    createtime = db.Column(db.String(20), index=True)

class TongbaoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    createtime = db.Column(db.String(500), index=True, unique=True)
    jianguan = db.Column(db.String(500), index=True)
    jingwu = db.Column(db.String(500), index=True)
    yuqing = db.Column(db.String(500), index=True)
    shengchan = db.Column(db.String(500), index=True)


def init_db():
    from app import db
    from app.models import User
    db.create_all()
    for name in jianqu_names:
        user =User(nickname=name, password='1')
        db.session.add(user)
        db.session.commit()