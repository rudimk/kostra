from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Key(Model):
    key_id = Column(Integer, primary_key=True)
    key_name = Column(String(100), nullable=False)
    key_path = Column(String(50), nullable=False)

    def __repr__(self):
        return self.key_name
