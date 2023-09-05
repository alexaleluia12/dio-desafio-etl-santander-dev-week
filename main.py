from extract import read_imputs
from transform import clients_from, format_client

import json

if __name__ == "__main__":
    # EXTRACT
    files = read_imputs()
    clients = clients_from(files)
    group_clients = []

    # TRANSFORM
    for client in clients:
        client_json_like = format_client(clients[client])
        group_clients.append(client_json_like)

    # LOAD
    with open('saida/db.json', mode='w') as file:
        json.dump(group_clients, file)
        print('ETL feito com sucesso')
