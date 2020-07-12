from csv import DictReader, DictWriter


with open('pessoas.csv', 'w', newline='') as file:
    cabecalho = ['Nome', 'Idade', 'Altura']
    csv_writer = DictWriter(file, fieldnames=cabecalho)
    csv_writer.writeheader()
    csv_writer.writerow({
        'Nome': 'Bruno',
        'Idade': '35',
        'Altura': '175'
    })
    csv_writer.writerow({
        'Nome': 'Maria',
        'Idade': '19',
        'Altura': '180'
    })
    csv_writer.writerow({
        'Nome': 'Davi',
        'Idade': '39',
        'Altura': '175'
    })

with open('pessoas.csv', 'r') as arquivo_original:
    csv_reader = DictReader(arquivo_original)
    computadores = list(csv_reader)
    with open('pessoasV2.csv', 'w', newline='') as novo_arquivo:
        cabecalho = ['Nome', 'Idade', 'Altura']
        csv_writer = DictWriter(novo_arquivo, fieldnames=cabecalho)
        csv_writer.writeheader()
        for linha in computadores:
            csv_writer.writerow({
                'Nome': linha['Nome'],
                'Idade': linha['Idade'],
                'Altura': linha['Altura'] + 'cm'
            })
