import joblib
def load_model():
    try:
        model=joblib.load("model.joblib")
        return model
    except Exception as e:
        print("Error loading Model",e)
        return None