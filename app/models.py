from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(20), index = True, unique = True)


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