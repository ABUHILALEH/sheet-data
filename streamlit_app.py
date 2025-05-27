import pandas as pd

def load_excel_file(filename):
    try:
        df = pd.read_excel(filename)
        print("\n✅ File loaded successfully!")
        return df
    except Exception as e:
        print(f"\n❌ Error loading file: {e}")
        return None

def display_columns(df):
    print("\n📋 Available Columns:")
    for i, col in enumerate(df.columns):
        print(f"{i + 1}. {col}")
    return df.columns

def filter_data(df, column_name, value):
    filtered_df = df[df[column_name].astype(str).str.contains(str(value), case=False, na=False)]
    return filtered_df

def export_data(df, output_name):
    try:
        df.to_excel(output_name, index=False)
        print(f"\n📁 Data exported successfully to '{output_name}'")
    except Exception as e:
        print(f"\n❌ Error exporting file: {e}")

def main():
    filename = input("Enter the Excel filename (e.g., data.xlsx): ")
    df = load_excel_file(filename)
    if df is None:
        return

    columns = display_columns(df)
    col_index = int(input("\nChoose a column number to filter by: ")) - 1
    if col_index < 0 or col_index >= len(columns):
        print("❌ Invalid column number.")
        return
    column_name = columns[col_index]

    value = input(f"Enter the value to search for in '{column_name}': ")
    filtered_df = filter_data(df, column_name, value)

    if filtered_df.empty:
        print("\n🔍 No results found.")
    else:
        print(f"\n🔍 Found {len(filtered_df)} matching rows.")
        print(filtered_df.head())

        export_choice = input("Do you want to export the result? (yes/no): ").lower()
        if export_choice == 'yes':
            output_name = input("Enter the output Excel filename (e.g., filtered_data.xlsx): ")
            export_data(filtered_df, output_name)

if __name__ == "__main__":
    main()
