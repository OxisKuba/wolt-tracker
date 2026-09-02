# Wolt Tracker v1 - by OxisKuba
# My first Python project

earnings = 1250  # dneska vyjezděno
hours = 4.5
km = 32

per_hour = earnings / hours
per_km = earnings / km

print(f"Dneska: {earnings} Kc")
print(f"Hodiny: {hours}h")
print(f"Vydelano za hodinu: {per_hour:.0f} Kc/h")
print(f"Vydelano za km: {per_km:.0f} Kc/km")

if per_hour > 250:
    print("Super den! 🔥")
else:
    print("Priste to bude lepsi 💪")
