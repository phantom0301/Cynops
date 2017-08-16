from datetime import datetime
from flask import  session
from . import main
from flask_login import login_required
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user
from ..models import User
from .forms import LoginForm,RegistrationForm,IPscannerForm
from .. import db
from flask import jsonify

from libnmap.process import NmapProcess
from libnmap.parser import NmapParser
import xml.etree.ElementTree
import networkx as nx
from networkx.readwrite import json_graph
import json

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    pass

@main.route('/contact')
def contact():
    pass

@main.route('/scan', methods=['GET', 'POST'])
@login_required
def scan():
    form = IPscannerForm()
    if form.validate_on_submit():
        ip = form.ip.data
        ip = str(ip)
        nm1 = NmapProcess(ip, options="-sn")
        nm1.run()
        parsed = NmapParser.parse(nm1.stdout)
        G = nx.Graph()
        nm2 = NmapProcess("www.baidu.com", options="--traceroute")
        nm2.run()
        collection = xml.etree.ElementTree.fromstring(nm2.stdout)
        nodes = collection.getiterator("hop")
        trace_list = []
        pre_node = ''
        for node in nodes:
            trace_list.append(node.attrib["ipaddr"])
            G.add_node(node.attrib["ipaddr"])
            if pre_node != '':
                G.add_edge(node.attrib["ipaddr"], pre_node)
            pre_node = node.attrib["ipaddr"]
        for host in parsed.hosts:
            if host.is_up():
                G.add_node(host.address)
                G.add_edge(host.address,trace_list[0])
        gra_json = json.dumps(G.adj)
        return render_template('result.html',gra_json=gra_json)
    return render_template('scan.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)




