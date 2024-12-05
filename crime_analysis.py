# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load csv
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})


crimes["TIME OCC"] = crimes["TIME OCC"].str.zfill(4)  
crimes["Hour"] = crimes["TIME OCC"].str[:2].astype(int)  


peak_crime_hour = crimes["Hour"].value_counts().idxmax()



night_hours = list(range(22, 24)) + list(range(0, 4))  
night_crimes = crimes[crimes["Hour"].isin(night_hours)] 
peak_night_crime_location = night_crimes["AREA NAME"].value_counts().idxmax()




age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf] 
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]  
crimes["Age Group"] = pd.cut(crimes["Vict Age"], bins=age_bins, labels=age_labels)  
victim_ages = crimes["Age Group"].value_counts().sort_index()  



# Print results
print(f"Peak crime hour: {peak_crime_hour}")
print(f"Peak night crime location: {peak_night_crime_location}")
print("Crimes by victim age group:")
print(victim_ages)



# -------------------------------- Visualization -------------------------------

# crimes by hour
plt.figure(figsize=(10, 6))
sns.countplot(x="Hour", data=crimes, palette="viridis", order=range(24))
plt.title("Frequency of Crimes by Hour")
plt.xlabel("Hour (24-Hour Format)")
plt.ylabel("Crime Frequency")
plt.xticks(rotation=45)
plt.show()

# night crimes by area 
plt.figure(figsize=(12, 6))
sns.countplot(y="AREA NAME", data=night_crimes, palette="cool", order=night_crimes["AREA NAME"].value_counts().index)
plt.title("Frequency of Night Crimes by Area")
plt.xlabel("Crime Frequency")
plt.ylabel("Area Name")
plt.show()

# crimes by victim age group 
plt.figure(figsize=(10, 6))
sns.barplot(x=victim_ages.index, y=victim_ages.values, palette="mako")
plt.title("Crimes by Victim Age Group")
plt.xlabel("Age Group")
plt.ylabel("Crime Frequency")
plt.show()















