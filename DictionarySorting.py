employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 70000},
    {"name": "Charlie", "salary": 60000}
]

# Sort by salary, highest first
sorted_staff = sorted(employees, key=lambda x: x['salary'], reverse=True)

for emp in sorted_staff:
    print(emp)
