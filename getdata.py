def get_csv_data():
    data = []

    with open('data/15mDOTUSDT.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            elements = line.split(',')
            # Convert string elements to float
            elements = [float(e) for e in elements[:6]]
            data.append(elements)
    # print(data)
    print(f"The list has {len(data)} elements.")
    return data

get_csv_data()