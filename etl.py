import csv

def extract_data(input_file):
    data = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        # Pula a primeira linha (cabeçalho)
        next(reader, None)
        for row in reader:
            data.append(row)
    return data

def transform_data(data):
    transformed_data = []
    for row in data:
        transformed_row = [row[0], str(int(row[1]) * 2)]
        transformed_data.append(transformed_row)
    return transformed_data

def load_data(output_file, data):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

input_file = 'dados_de_entrada.csv'
output_file = 'dados_transformados.csv'

data = extract_data(input_file)
transformed_data = transform_data(data)
load_data(output_file, transformed_data)

print("ETL concluído com sucesso!")
