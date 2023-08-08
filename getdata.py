def get_csv_data(path):
    data = []

    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            elements = line.split(',')
            # Convert string elements to float
            elements = [float(e) for e in elements]
            data.append(elements)
    # print(data)
    print(f"The list has {len(data)} elements.")
    return data

# get_csv_data()