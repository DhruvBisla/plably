import csv

def create_fake_data():
    rows = [
        ["x", "x±", "y", "y±"],
        [1, 0.5, 1, 0.5],
        [2, 0.5, 2, 0.5]
    ]
    with open('tests/data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
