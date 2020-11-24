import pandas as pd

AWS_BUCKET_PATH = "s3://wagon-public-datasets/taxi-fare-train.csv"

<<<<<<< HEAD:07-Data-Engineering/03-ML-Iteration/01-Notebook-to-package/TaxiFareModel/data.py
DIST_ARGS = dict(
    start_lat="pickup_latitude",
    start_lon="pickup_longitude",
    end_lat="dropoff_latitude",
    end_lon="dropoff_longitude",
)
=======
>>>>>>> upstream/data-engv2:07-Data-Engineering/02-ML-Iteration/03-Notebook-to-package/TaxiFareModel/data.py

def get_data(nrows=10_000):
    '''returns a DataFrame with nrows from s3 bucket'''
    df = pd.read_csv(AWS_BUCKET_PATH, nrows=nrows)
    return df


<<<<<<< HEAD:07-Data-Engineering/03-ML-Iteration/01-Notebook-to-package/TaxiFareModel/data.py
def clean_df(df, test=False):
    df = df.dropna(how="any", axis="rows")
=======
def clean_data(df, test=False):
    df = df.dropna(how='any', axis='rows')
>>>>>>> upstream/data-engv2:07-Data-Engineering/02-ML-Iteration/03-Notebook-to-package/TaxiFareModel/data.py
    df = df[(df.dropoff_latitude != 0) | (df.dropoff_longitude != 0)]
    df = df[(df.pickup_latitude != 0) | (df.pickup_longitude != 0)]
    if "fare_amount" in list(df):
        df = df[df.fare_amount.between(0, 4000)]
    df = df[df.passenger_count < 8]
    df = df[df.passenger_count >= 0]
    df = df[df["pickup_latitude"].between(left=40, right=42)]
    df = df[df["pickup_longitude"].between(left=-74.3, right=-72.9)]
    df = df[df["dropoff_latitude"].between(left=40, right=42)]
    df = df[df["dropoff_longitude"].between(left=-74, right=-72.9)]
    return df


<<<<<<< HEAD:07-Data-Engineering/03-ML-Iteration/01-Notebook-to-package/TaxiFareModel/data.py
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> upstream/data-engv2:07-Data-Engineering/02-ML-Iteration/03-Notebook-to-package/TaxiFareModel/data.py
    df = get_data()
