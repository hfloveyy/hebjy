from app import app
from flask import render_template,flash,redirect,url_for,abort,request,session,g
from .models import User,ReportModel,KanshouModel,TongbaoModel
from .forms import LoginForm,ReportForm,KanshouForm
from flask.ext.login import login_user, login_required, logout_user, current_user,login_url
from app import login_manager
from app import db
import time
from sqlalchemy import func


jianqu_names = ['一监区','二监区','三监区','四监区','五监区','六监区','七监区',
'八监区','九监区','十监区','十一监区','十二监区','后勤监区','外籍监区','集训监区','出监监区','病犯监区','禁闭、严管','高戒备','改造业务科室']


def get_time(timeStamp):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def index():
    content = []

    for jianqu in jianqu_names:
        res = db.session.query(func.max(ReportModel.createtime).label('max_time')).one()
        
        data = ReportModel.query.filter_by(jianqu = jianqu).last()
        if data:
            content.append(data)

    return render_template('index.html', content = content)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(nickname = form.name.data).first()
        if user is not None and user.password == form.password.data:
            login_user(user)
            flash(user.nickname)
            if '看守大队' in user.nickname:
                return redirect(url_for('addks'))
            else:
                return redirect(request.args.get('next') or url_for('index'))
        else:
            error = '登录失败,请重新登录！'
    return render_template('login.html',form = form,error = error)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.before_request
def before_request():
    g.user = current_user

@app.route("/add", methods=['GET', 'POST'])
@login_required
def add():
    username = g.user.nickname
    if '看守大队' in username:
        return redirect(url_for('addks'))
    reportform = ReportForm()
    if reportform.validate_on_submit():
        report = ReportModel(
            jianqu = username,
            zhibanlingdao = reportform.zhibanlingdao.data,
            baitianzaigang = reportform.baitianzaigang.data,
            yejianzhiban = reportform.yejianzhiban.data,
            zaice = reportform.zaice.data,
            shiyou = reportform.shiyou.data,
            chugong = reportform.chugong.data,
            beizhu = reportform.beizhu.data,
            createtime = get_time(time.time())
        )
        db.session.add(report)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html',username = username,form = reportform)

@app.route("/addks", methods=['GET', 'POST'])
@login_required
def addks():
    username = g.user.nickname
    kanshouform = KanshouForm()
    if kanshouform.validate_on_submit():
        print(kanshouform.zhibanlingdao.data)
        kanshou = KanshouModel(
            zhibanlingdao=kanshouform.zhibanlingdao.data,
            damen = kanshouform.damen.data,
            ermen = kanshouform.ermen.data,
            sanmen = kanshouform.sanmen.data,
            beizhu=kanshouform.beizhu.data,
            createtime=get_time(time.time())
        )
        db.session.add(kanshou)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addks.html', username=username, form=kanshouform)