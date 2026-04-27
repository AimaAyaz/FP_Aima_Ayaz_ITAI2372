from sklearn.preprocessing import LabelEncoder

def preprocess(df):
    encoders = {}
    for col in ["mission_name", "destination", "mission_goal"]:
        enc = LabelEncoder()
        df[col] = enc.fit_transform(df[col])
        encoders[col] = enc

    X = df.drop("mission_type", axis=1)
    y = df["mission_type"]

    y_enc = LabelEncoder()
    y = y_enc.fit_transform(y)

    return X, y, encoders, y_enc
