from sklearn.model_selection import train_test_split

def get_data_split(df, test_size=0.3):
    settled = df[df["status"].isin(["successful", "failed"])].copy()
    settled["target"] = settled["status"] == "successful"

    y = settled["target"]
    X = settled.drop(columns=["target", "status"])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=42,
        stratify=y,
    )
    return X_train, X_test, y_train, y_test