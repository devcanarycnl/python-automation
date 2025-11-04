import os
import pandas as pd

def analyze_news_data():
    print("\n=== News Data Analysis ===")
    
    try:
        # Construct file path relative to the script location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, 'news.csv')
        
        # Read the data
        print("\nReading news data...")
        if not os.path.exists(csv_path):
            print(f"Error: File not found: {csv_path}")
            return
            
        df = pd.read_csv(csv_path)
        
        # Display basic information
        print(f"\nDataset Shape:")
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")
        
        print("\nFirst 5 rows of the dataset:")
        print("-" * 80)
        print(df.head())
        print("-" * 80)
        
        # Display column information
        print("\nColumns in the dataset:")
        for col in df.columns:
            print(f"- {col}")
            
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    analyze_news_data()
