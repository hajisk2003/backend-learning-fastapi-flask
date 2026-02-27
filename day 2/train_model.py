from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np
import joblib

x=np.array([[1,2,3],[4,5,6],[7,8,9],[8,6,7]])
y=np.array([10,14,18,22])
#create Pipeline
pipeline=Pipeline([
    ("scaler",StandardScaler()),
    ("model",LinearRegression())
])
#train
pipeline.fit(x,y)


model=LinearRegression()


joblib.dump(pipeline,"model.joblib")
print("Pipeline trained and saved") 

# model=LinearRegression()
# model.fit(x,y)

# joblib.dump(model,"model.joblib")
# print("Model trained and saved") 