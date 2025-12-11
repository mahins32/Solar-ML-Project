import pickle
from sklearn.metrics import mean_absolute_error, r2_score
from data_preprocessing import load_dataset, preprocess_data

def evaluate():
    df = load_dataset("data/solardataset.csv")
    (X_train, X_test, y_train, y_test), scaler = preprocess_data(df)

    # Load trained model
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("Model Evaluation:")
    print(f"MAE: {mae:.4f}")
    print(f"R² Score: {r2:.4f}")

if __name__ == "__main__":
    evaluate()
