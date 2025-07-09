T = int(input())

for _ in range(T):
    n = int(input())
    items = {}
    
    for _ in range(n):
        name, category = input().split()
        if category in items:
            items[category] += 1  # Count items per category
        else:
            items[category] = 1
    
    # Calculate total combinations
    total = 1
    for count in items.values():
        total *= (count + 1)  # +1 for choosing nothing from this category
    
    print(total - 1)  # -1 because we can't choose nothing from all categories