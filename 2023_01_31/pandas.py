#!/usr/bin/env python
# encoding: utf-8

#https://stackoverflow.com/questions/67617183/converting-excel-to-json-using-pandas-in-python-3-9

import pandas as pd
import json

rows = [
    [],
    [],
    ["Test 1", "Menu", "Setting", "Value"],
    [None, "Menu1", "Setting1", "Value1"],
    [None, "Menu2", "Setting2", "Value2"],
    [],
    [],
    ["Test 2", "A", "B", "C"],
    [None, 1, 2, 3],
    [None, 4, 5, 6],
]

df = pd.DataFrame(rows, columns=[f"Unnamed: {i}" for i in range(1, 5)])

# Remove entirely empty rows
df = df.dropna(how="all")

# Fill missing values in column 1
df["Unnamed: 1"] = df["Unnamed: 1"].fillna(method="ffill")


def process_group(g):
    # Drop first column
    g = g.drop("Unnamed: 1", axis=1)
    # Use first row as column names
    g = g.rename(columns=g.iloc[0])
    # Drop first row
    g = g.drop(g.index[0])
    # Convert to dict
    return g.to_dict(orient="records")


output = df.groupby("Unnamed: 1").apply(process_group).to_dict()

output_str = json.dumps(output)