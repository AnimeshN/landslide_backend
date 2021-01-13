from django.shortcuts import render

# Create your views here.
from .apps import PredictorConfig

from django.http import JsonResponse
from rest_framework.views import APIView

class descisionTree(APIView):
    def get(self,*args,**kwargs):
            #reading values form url
            # val1 = self.kwargs.get('Geomorphology', None)
            val2 = self.kwargs.get('RockChar', None)
            val3 = self.kwargs.get('OverburdenThickness', None)
            val4 = self.kwargs.get('Hydrology', None)
            val5 = self.kwargs.get('Erosion', None)
            val6 = self.kwargs.get('Rainfall', None)
            val7 = self.kwargs.get('Anthropogenic', None)
            val8 = self.kwargs.get('SlopeType', None)
            val9 = self.kwargs.get('LandslideMaterial', None)
            val10 = self.kwargs.get('Movement', None)
            val11 = self.kwargs.get('Style', None)

    
            #converting labels to integers


            # Geomorphology = int(PredictorConfig.le_Geomorphology.transform([val1])[0])
            RockChar = int(PredictorConfig.le_RockChar.transform([val2])[0])
            OverburdenThickness = int(PredictorConfig.le_OverburdenThickness.transform([val3])[0])
            Hydrology = int(PredictorConfig.le_Hydrology.transform([val4])[0])
            Erosion = int(PredictorConfig.le_Erosion.transform([val5])[0])
            Rainfall = int(PredictorConfig.le_Rainfall.transform([val6])[0])
            Anthropogenic = int(PredictorConfig.le_Anthropogenic.transform([val7])[0])
            SlopeType = int(PredictorConfig.le_SlopeType.transform([val8])[0])
            LandslideMaterial = int(PredictorConfig.le_LandslideMaterial.transform([val9])[0])
            Movement = int(PredictorConfig.le_Movement.transform([val10])[0])
            Style = int(PredictorConfig.le_Style.transform([val11])[0])
            
            #predicting value
            result = PredictorConfig.model.predict([[RockChar,OverburdenThickness,Hydrology,Erosion,Rainfall,Anthropogenic,SlopeType,LandslideMaterial,Movement,Style]])
            
            #inversing the integer to value
            susceptibility = PredictorConfig.le_target.inverse_transform(result)[0]
            response = {'Susceptibility': susceptibility}
            return JsonResponse(response)