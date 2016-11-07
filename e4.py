import pandas as pd
import matplotlib.pyplot as plt
import json

with open("ELECTION_ID") as f:
    year_electionid = json.load(f)

 data = []
 for x in year_electionid:
    year = x.split(" ")[0]
    header = pd.read_csv(year + ".csv", nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(year + ".csv", index_col = 0,
              thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = year
    data.append(df[["Year", "Republican", "Democratic", "Total Votes Cast"]])
def county_plot(county):
    df = pd.concat(data)
    df["Republican Share"] = df["Republican"]/ df["Total Votes Cast"]
    df.ix[county + "County", ["Year", "Republican Share"]].sort(["Year"], ascending = True).plot(x = "Year", y = "Republican Share")
    plt.savefig(county +'.png')
county_plot("Albemarle")
