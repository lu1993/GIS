# -*- coding: utf-8 -*-
# here you will register all blueprint apps
from .home import home
from .gis import gis_caller


def register_blueprint(app):
    # app.register_blueprint(home)
    app.register_blueprint(gis_caller, url_prefix='/gis/b12c645e186f93509b1c0c36552ec334')
