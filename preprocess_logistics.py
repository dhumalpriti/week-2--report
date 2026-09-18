import pandas as pd
import numpy as np
from pathlib import Path
p=Path(__file__).parent
df=pd.read_csv(p/"raw_logistics_data.csv")
df["Date"]=pd.to_datetime(df["Date"],errors="coerce")
nums=["Distance_km","Weight_kg","Delivery_Days","Fuel_Litres","Cost_INR"]
for c in nums: df[c]=pd.to_numeric(df[c],errors="coerce")
df["Delivery_Days"]=df["Delivery_Days"].fillna(df["Delivery_Days"].median())
df.loc[df["Weight_kg"]<=0,"Weight_kg"]=np.nan
df["Weight_kg"]=df["Weight_kg"].fillna(df["Weight_kg"].median())
df=df.drop_duplicates("Shipment_ID")
for c in ["Distance_km","Weight_kg","Cost_INR"]:
    df[c+"_Normalized"]=(df[c]-df[c].min())/(df[c].max()-df[c].min())
df.to_csv(p/"cleaned_logistics_data.csv",index=False)
print(df.head())
