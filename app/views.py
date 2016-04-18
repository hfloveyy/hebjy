from app import app
from flask import render_template,flash,redirect,url_for,abort,request,session,g
from .models import User,ReportModel,KanshouModel,TongbaoModel
from .forms import LoginForm,ReportForm,KanshouForm,TongbaoForm
from flask.ext.login import login_user, login_required, logout_user, current_user,login_url
from app import login_manager
from app import db
import time
from sqlalchemy import func
from sqlalchemy.sql.expression import collate

jianqu_names = ['一监区','二监区','三监区','四监区','五监区','六监区','七监区',
'八监区','九监区','十监区','十一监区','十二监区','后勤监区','外籍监区','集训监区','出监监区','病犯监区','禁闭、严管','高戒备','改造业务科室']


def get_time(timeStamp):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def sum_all(report):
    sum = []
    btzg = 0
    yjzb = 0
    zc = 0
    sy = 0
    cg = 0
    for some in report:
        btzg += int(some.baitianzaigang)
        yjzb += int(some.yejianzhiban)
        zc += int(some.zaice)
        sy += int(some.shiyou)
        cg += int(some.chugong)
    sum.append(btzg)
    sum.append(yjzb)
    sum.append(zc)
    sum.append(sy)
    sum.append(cg)
    return sum

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def index():
    reports = []

    for jianqu in jianqu_names:
        #报表
        one = ReportModel.query.filter_by(jianqu = jianqu).order_by(ReportModel.createtime.desc()).first()
        if one:
            reports.append(one)
        #report = ReportModel.query.group_by(ReportModel.jianqu).order_by(ReportModel.jianqu).order_by(ReportModel.createtime.desc())
        #collate(ReportModel.jianqu, 'Chinese_PRC_CI_AS')
        #看守大队
    kanshou = KanshouModel.query.order_by(KanshouModel.createtime.desc()).first()
    #合计
    report = ReportModel.query.group_by(ReportModel.jianqu).order_by(ReportModel.jianqu).order_by(ReportModel.createtime.desc())
    total = sum_all(report)
    tongbao = TongbaoModel.query.order_by(TongbaoModel.createtime.desc()).first()
    return render_template('index.html', content = reports,total = total,kanshou = kanshou,tongbao = tongbao)

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
            elif '管理员' in user.nickname:
                return redirect(url_for('addtongbao'))
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
    elif '管理员' in username:
        return redirect(url_for('addtongbao'))
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

@app.route("/addtongbao", methods=['GET', 'POST'])
@login_required
def addtongbao():
    username = g.user.nickname
    tongbaoform = TongbaoForm()
    if tongbaoform.validate_on_submit():
        tongbao = TongbaoModel(
            createtime=get_time(time.time()),
            jianguan = tongbaoform.jianguan.data,
            jingwu = tongbaoform.jingwu.data,
            yuqing = tongbaoform.yuqing.data,
            shengchan = tongbaoform.shengchan.data
        )
        db.session.add(tongbao)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addtongbao.html', username=username,  form=tongbaoform)
