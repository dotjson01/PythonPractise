years = [2027, 2026]
months = ['Jan', 'Feb']
days = range(1,29)

for y in years:
    for m in months:
        for d in days:
            print(f"Report_{y}_{m}_{d}.csv")