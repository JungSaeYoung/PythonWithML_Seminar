employees = {'Alice': 100000, 'Bob': 99817, 'Carol': 122908, 'Frank': 88123, 'Eve': 93121}

top_earners = [(key, value) for key, value in employees.items() if value >= 100000]

print(top_earners)