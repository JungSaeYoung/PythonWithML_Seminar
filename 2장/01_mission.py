employees = {'Alice': 100000, 'Bob': 99817, 'Carol': 122908, 'Frank': 88123, 'Eve': 93121}

top_earners = []
for key, value in employees.items():
    if value >= 100000:
        top_earners.append((key, value))

print(top_earners)
# [('Alice', 100000), ('Carol', 122908)]