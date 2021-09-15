from ma import ma
from models.body_data import BodyDataModel
class BodyDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BodyDataModel
        load_instance = True
