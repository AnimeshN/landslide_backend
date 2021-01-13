import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import pickle



df = pd.read_csv("landslide_suscep.csv")

delcol = ['Lat','Long','Vill','Susceptibility']
inputs = df.drop(delcol,1).set_index('Loc')
target = df['Susceptibility']


#label encoder

# le_Geomorphology = LabelEncoder()
le_RockChar = LabelEncoder()
le_OverburdenThickness = LabelEncoder()
le_Hydrology = LabelEncoder()
le_Erosion = LabelEncoder()
le_Rainfall = LabelEncoder()
le_Anthropogenic = LabelEncoder()
le_SlopeType = LabelEncoder()
le_LandslideMaterial = LabelEncoder()
le_Movement = LabelEncoder()
le_Style = LabelEncoder()


# le_Rockstate = LabelEncoder()
# le_Hydrology = LabelEncoder()
# le_Weathering = LabelEncoder()
# le_OverburdenD = LabelEncoder()

# le_RoadInfluence = LabelEncoder()
# le_JointFail = LabelEncoder()
# le_RiverBankFail = LabelEncoder()
# le_ToeFail = LabelEncoder()

le_target = LabelEncoder()


inputs_n = pd.DataFrame()
# inputs_n['Geomorphology'] = le_Geomorphology.fit_transform(inputs['Geomorphology'])
inputs_n['RockChar'] = le_RockChar.fit_transform(inputs['RockChar'])
inputs_n['OverburdenThickness'] = le_OverburdenThickness.fit_transform(inputs['OverburdenThickness'])
inputs_n['Hydrology'] = le_Hydrology.fit_transform(inputs['Hydrology'])
inputs_n['Erosion'] = le_Erosion.fit_transform(inputs['Erosion'])
inputs_n['Rainfall'] = le_Rainfall.fit_transform(inputs['Rainfall'])
inputs_n['Anthropogenic'] = le_Anthropogenic.fit_transform(inputs['Anthropogenic'])
inputs_n['SlopeType'] = le_SlopeType.fit_transform(inputs['SlopeType'])
inputs_n['LandslideMaterial'] = le_LandslideMaterial.fit_transform(inputs['LandslideMaterial'])
inputs_n['Movement'] = le_Movement.fit_transform(inputs['Movement'])
inputs_n['Style'] = le_Style.fit_transform(inputs['Style'])

print(inputs_n)
target_n = pd.DataFrame()
target_n  = le_target.fit_transform(target)

model = tree.DecisionTreeClassifier()
model.fit(inputs_n,target_n)




pickl = {
    # 'le_Geomorphology':le_Geomorphology,
    'le_RockChar': le_RockChar,
    'le_OverburdenThickness':le_OverburdenThickness, 
    'le_Hydrology': le_Hydrology,
    'le_Erosion': le_Erosion,
    'le_Rainfall': le_Rainfall,
    'le_Anthropogenic': le_Anthropogenic,
    'le_SlopeType': le_SlopeType,
    'le_LandslideMaterial': le_LandslideMaterial,
    'le_Movement': le_Movement,
    'le_Style': le_Style,
    'le_target': le_target,
    'model': model,
}
pickle.dump( pickl, open( 'models' + ".p", "wb" ) )