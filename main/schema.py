from ninja import ModelSchema
from .models import History

class HistorySchemaIn(ModelSchema):
    class Meta:
        model = History
        fields = ['image', 'prompt']

class HistorySchemaOut(ModelSchema):
    class Meta:
        model = History
        fields = '__all__'