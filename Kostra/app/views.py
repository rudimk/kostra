from flask import render_template, redirect
from flask_appbuilder.actions import action
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from models import *
import fabfile
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

class ProductionServerModelView(ModelView):
    datamodel = SQLAInterface(ProductionServer)
    list_columns = ['production_server_name', 'production_server_ip', 'key']
    label_columns = {'production_server_name': 'Server Name', 'production_server_ip': 'Host', 'key': 'SSH Key'}

    @action('update_packages', 'Update Ubuntu package repositories', 'Would you like to update package repos for this server?', 'fa-refresh')
    def update_packages(self, item):
        env = {}
        hosts = """{}@{}""".format('dartboard-admin', item.production_server_ip)
        env['key_filename'] = item.key.key_path
        fabfile.execute_update_packages(env=env, hosts=hosts)
        return redirect(self.get_redirect())

appbuilder.add_view(KeyModelView, "List Keys",icon = "fa-key",category = "Keys", category_icon='fa-key')
appbuilder.add_view(ProductionServerModelView, "Production Servers", icon="fa-cog", category="Servers", category_icon="fa-server")


