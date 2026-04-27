name="femi"
age= 35
print(name)
#lists
items=["bags", 34,age, 45]
print(items[2])
items.append("address")
print(items[4])
#dictionary
customer={
    "address":"akoka estate",
    "marital status": "single",
    "purchases": ["bags", "shoes"]
    }
customer["location"]="Ëlepe"
print(customer["purchases"])
print(customer["location"])
#function
def add(a,b):
    return a + b
print(add(500,1050))
def discount(pay):
    return pay * 0.5
print(round(discount(1000)))
#pandas
import pandas as pd
femi={
    "items":["bags", "shoes", "clothes","caps"],
    "size":[20,30,10,40],
    "amount":[5000,2000,2000, 1000]
    }
df=pd.DataFrame(femi)
print(df["items"])
print(round(df.describe()))
print(round(df["amount"].mean()))
print(df.head())
print(df.info())
