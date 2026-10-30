import pandas as pd

students = {
    "id": 7,
    "name": "kishore",
    "Department": "IT",
    "Marks": 400
}

df = pd.DataFrame([students])

df.to_csv("studentDetails.csv", mode="a", index=False, header=False)
print("Data appended successfully")