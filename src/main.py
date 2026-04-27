from dataset import load_dataset
from preprocess import preprocess
from model import train_model
from utils import print_header

def main():
    print_header("NASA Space Mission Classification AI")

    df = load_dataset()
    print("Dataset Loaded:")
    print(df.head())

    X, y, encoders, y_enc = preprocess(df)
    print("\nData Preprocessed.")

    model, acc = train_model(X, y)

    if model:
        print(f"\nModel trained successfully. Accuracy: {acc:.2f}")
    else:
        print("Model training failed.")

if __name__ == "__main__":
    main()
