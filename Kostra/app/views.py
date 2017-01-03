from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from models import *

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()

class KeyModelView(ModelView):
    datamodel = SQLAInterface(Key)
    list_columns = ['key_name', 'key_path']
    label_columns = {'key_name': 'Name', 'key_path': 'Key Path'}

appbuilder.add_view(KeyModelView, "List Keys",icon = "fa-key",category = "Keys", category_icon='fa-key')


