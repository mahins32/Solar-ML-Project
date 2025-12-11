import pickle
from sklearn.ensemble import RandomForestRegressor
from data_preprocessing import load_dataset, preprocess_data

def train_model():
    df = load_dataset("notebook/solar_generation_dataset.csv")

    (X_train, X_test, y_train, y_test), scaler = preprocess_data(df)

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Save model & scaler
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open("scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    print("Model training complete! model.pkl & scaler.pkl saved.")

if __name__ == "__main__":
    train_model()
