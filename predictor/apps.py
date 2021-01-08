from django.apps import AppConfig
from django.conf import settings
# import os
import pickle

class PredictorConfig(AppConfig):
    name = 'predictor'
    # path = os.path.join(settings.MODELS,'models.p')
    path = settings.MODELS/'models.p'
    # print(path)

    with open(path,'rb') as pickled:
        data = pickle.load(pickled)
        

    model = data['model']
    le_Geomorphology = data['le_Geomorphology']
    le_RockChar = data['le_RockChar']
    le_OverburdenThickness = data['le_OverburdenThickness'] 
    le_Hydrology = data['le_Hydrology']
    le_Erosion = data['le_Erosion']
    le_Rainfall = data['le_Rainfall']
    le_Anthropogenic = data['le_Anthropogenic']
    le_SlopeType = data['le_SlopeType']
    le_LandslideMaterial = data['le_LandslideMaterial']
    le_Movement = data['le_Movement']
    le_Style = data['le_Style']
    le_target = data['le_target']



