# Wolt Tracker v2 - by OxisKuba

print("--- WOLT TRACKER V2 ---")

earnings = int(input("Kolik Kc dneska? "))
hours = float(input("Kolik hodin? "))
km = float(input("Kolik km? "))

per_hour = earnings / hours
per_km = earnings / km

print("\n--- VYSLEDEK ---")
print(f"Dneska: {earnings} Kc")
print(f"Hodiny: {hours}h / Km: {km}km")
print(f"Za hodinu: {per_hour:.0f} Kc/h")
print(f"Za km: {per_km:.0f} Kc/km")

if per_hour >= 300:
    print("GOD MODE! 🔥🔥🔥")
elif per_hour >= 250:
    print("Super den! 🔥")
elif per_hour >= 200:
    print("Solidni 👍")
else:
    print("Priste to bude lepsi 💪")

# Uloz to pro priste
print(f"\nCil na zitra: {per_hour + 20:.0f} Kc/h")
