from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

# This model stores SSH key details - their names and full paths.
class Key(Model):
    key_id = Column(Integer, primary_key=True)
    key_name = Column(String(100), nullable=False)
    key_path = Column(String(50), nullable=False)

    def __repr__(self):
        return self.key_name


# This model stores details about a particular kind of server - in this case, a production server running various apps.
class ProductionServer(Model):
    production_server_id = Column(Integer, primary_key=True)
    production_server_name = Column(String(50), nullable=False)
    production_server_ip = Column(String(30), nullable=False)
    key_id = Column(Integer, ForeignKey('key.key_id'))
    key = relationship('Key')

    def __repr__(self):
        return self.production_server_name


# This model stores details about MySQL servers.
class MySQLServer(Model):
    mysql_server_id = Column(Integer, primary_key=True)
    mysql_server_name = Column(String(50), nullable=False)
    mysql_server_ip = Column(String(30), nullable=False)
    key_id = Column(Integer, ForeignKey('key.key_id'))
    key = relationship('Key')

    def __repr__(self):
        return self.mysql_server_name
