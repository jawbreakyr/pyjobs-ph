#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""server.py: App server, URL router, and template handler."""

import bottle as app
import rauth
from beaker.middleware import SessionMiddleware

import config
import models

app_session = SessionMiddleware(app.app(), {
    'session.data_dir': config.SESSION,
    'session.type': config.SESSION_TYPE,
    'session.auto': config.SESSION_AUTO
})

oauth2 = rauth.OAuth2Service
facebook = oauth2(
    client_id=config.FACEBOOK_CLIENT_ID,
    client_secret=config.FACEBOOK_CLIENT_SECRET,
    name='facebook',
    authorize_url='https://graph.facebook.com/oauth/authorize',
    access_token_url='https://graph.facebook.com/oauth/access_token',
    base_url='https://graph.facebook.com/'
)
redirect_uri = '{uri}:{port}/success'.format(
    uri=config.BASE_URI,
    port=config.PORT
)

def authenticate(func):
    def logged_in(*args, **kwargs):
        session = app.request.environ.get('beaker.session')

        if 'logged_in' in session:
            return func(*args, **kwargs)

        app.redirect('/login')

    return logged_in

@app.hook('before_request')
def global_session():
    app.request.session = app.request.environ.get('beaker.session')

@app.route('/')
def index():
    tpl = '{base}/index.tpl'.format(base=config.TEMPLATES)
    query = "SELECT * FROM Companies;"
    companies = models.cursor.execute(query)
    return app.template(tpl, companies=companies)

@app.route('/add<:re:/?>', method=['GET', 'POST'])
@authenticate
def add():
    tpl = '{base}/add.tpl'.format(base=config.TEMPLATES)
    name = app.request.forms.get('name')
    description = app.request.forms.get('description')
    uri = app.request.forms.get('uri')
    add = app.request.forms.get('add')

    if add:
        query = """
                INSERT INTO
                    Companies(name, description, uri, source)
                VALUES
                    (:name, :description, :uri, :source);
                """

        models.cursor.execute(query, dict(
                name=name,
                description=description,
                uri=uri,
                source=app.request.session['name']
            )
        )
        models.connect.commit()
        app.redirect('/')

    return app.template(tpl)

@app.route('/login<:re:/?>')
def login():
    params = dict(
        scope='read_stream',
        response_type='code',
        redirect_uri=redirect_uri
    )
    url = facebook.get_authorize_url(**params)

    app.redirect(url)

@app.route('/success<:re:/?>')
def login_success():
    try:
        code = app.request.params.get('code')
        session = facebook.get_auth_session(
            data=dict(
                code=code,
                redirect_uri=redirect_uri
            )
        )
        session_json = session.get('me').json()
        app.request.session['logged_in'] = True
        app.request.session['name'] = session_json['name']
    except:
        pass

    app.redirect('/add')

app.run(
    server=config.SERVER,
    host=config.HOST,
    port=config.PORT,
    app=app_session
)
