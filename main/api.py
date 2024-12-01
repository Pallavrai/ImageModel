from typing import List
from ninja_extra import NinjaExtraAPI
from ninja import File
from ninja.files import UploadedFile
from ninja_extra import (
    api_controller, 
    http_get, http_post, http_put, http_delete, http_patch, http_generic
)
from .models import History
from .schema import HistorySchemaIn, HistorySchemaOut
from AIModel import run_model
from PIL import Image
from io import BytesIO

api = NinjaExtraAPI()

@api_controller("/history")
class HistoryController:
    @http_get("",response=List[HistorySchemaOut])
    def list(self, request ):
        return History.objects.all()
    
    @http_post("",response=HistorySchemaOut)
    def create(self, prompt:str, image:UploadedFile = File(...)):
        image_content = Image.open(BytesIO(image.read()))
        response = run_model(image_content, prompt, "mps")
        return History.objects.create(prompt=prompt, image=image, response=response)


api.register_controllers(HistoryController)
