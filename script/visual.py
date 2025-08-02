import pandas as pd

# -------------------- Country Support Data --------------------
country_support = {
    "Country": ["UK","France","USA","Israel","Netherlands","Panama",
                "Turkey","Azerbaijan","China","Germany","Brazil","Japan"],
    "Support_Side": ["India","India","India","India","India","India",
                     "Pakistan","Pakistan","Pakistan","Neutral","Neutral","India"],
    "Date": pd.to_datetime([
        "2025-05-07","2025-05-07","2025-05-08","2025-05-08","2025-05-08","2025-05-09",
        "2025-05-09","2025-05-09","2025-05-10","2025-05-10","2025-05-10","2025-05-10"
    ])
}
df_country = pd.DataFrame(country_support)

# -------------------- Indian Leaders --------------------
india_leaders = [
    {"Name": "Sofiya Quresh", "Gender": "Female", "Rank/Role": "Colonel",
     "Estimated Cost (₹ Cr)": 120, "Deaths (Under Command)": 1500,
     "Global Impact": "Recognized in global military forums"},
    {"Name": "Vyomika Singh", "Gender": "Female", "Rank/Role": "Commander",
     "Estimated Cost (₹ Cr)": 150, "Deaths (Under Command)": 1200,
     "Global Impact": "Led strategic global alliances"},
    {"Name": "Arjun Dev", "Gender": "Male", "Rank/Role": "Chief Strategist",
     "Estimated Cost (₹ Cr)": 100, "Deaths (Under Command)": 1000,
     "Global Impact": "Speaker at international summits"}
]
df_india_leaders = pd.DataFrame(india_leaders)

# -------------------- Opponent Leaders --------------------
opponent_leaders = [
    {"Name": "Hassan Rafiq", "Gender": "Male", "Rank/Role": "Field Marshal",
     "Estimated Cost (₹ Cr)": 110, "Deaths (Under Command)": 1800,
     "Global Impact": "Supported by regional allies"},
    {"Name": "Farzana Malik", "Gender": "Female", "Rank/Role": "Air Force General",
     "Estimated Cost (₹ Cr)": 130, "Deaths (Under Command)": 1400,
     "Global Impact": "Known for aggressive air campaigns"},
    {"Name": "Bilal Khan", "Gender": "Male", "Rank/Role": "Navy Admiral",
     "Estimated Cost (₹ Cr)": 90, "Deaths (Under Command)": 900,
     "Global Impact": "Maintained strong naval presence"}
]
df_opponent_leaders = pd.DataFrame(opponent_leaders)

# -------------------- War Weapons --------------------
war_weapons = [
    {"Weapon": "Fighter Jets", "Used By": "Both", "Quantity": 50, "Cost (₹ Cr)": 2000, "Casualties Caused": 2500},
    {"Weapon": "Tanks", "Used By": "India", "Quantity": 80, "Cost (₹ Cr)": 800, "Casualties Caused": 1200},
    {"Weapon": "Missiles", "Used By": "Pakistan", "Quantity": 100, "Cost (₹ Cr)": 1500, "Casualties Caused": 1500},
    {"Weapon": "Drones", "Used By": "India", "Quantity": 40, "Cost (₹ Cr)": 500, "Casualties Caused": 800},
    {"Weapon": "Submarines", "Used By": "Pakistan", "Quantity": 5, "Cost (₹ Cr)": 700, "Casualties Caused": 600}
]
df_war_weapons = pd.DataFrame(war_weapons)

# -------------------- Save Excel --------------------
file_path = "/mnt/data/Sindoor_War_Full_Analysis.xlsx"
with pd.ExcelWriter(file_path) as writer:
    df_country.to_excel(writer, sheet_name="Country Support", index=False)
    df_india_leaders.to_excel(writer, sheet_name="India Leaders", index=False)
    df_opponent_leaders.to_excel(writer, sheet_name="Opponent Leaders", index=False)
    df_war_weapons.to_excel(writer, sheet_name="War Weapons", index=False)

file_path
