from ie.pipeline import run_pipeline

def main():
    df_structured = run_pipeline()
    print("Structured extraction completed.")
    print(df_structured.head())

if __name__ == "__main__":
    main()