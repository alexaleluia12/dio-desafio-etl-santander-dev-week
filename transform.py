import sys
import numpy as np

def format_client(client):
    """
    input -> client: {
        dados_pessoais: df,
        compras: df,
        sm: list
    }
    """
    new_client = {
        "id": int(client['dados_pessoais'].iloc[0, 0]),
        "nome": client['dados_pessoais'].iloc[0, 1],
        "address": client['dados_pessoais'].iloc[0, 2],
        "phone": client['dados_pessoais'].iloc[0, 3],
        "sm": client['sm'],
        "compras": [
            {"id": int(c[0]), "valor": float(c[1]), "data": c[2]}
            for c in client['compras'].iloc[:, 1:].to_numpy()
        ]
    }

    phone = new_client['phone'] # pode nao existir e o pandas lê como NaN
    new_client['phone'] = None if np.isnan(phone) else str(phone)[:-2]

    return new_client


def clients_from(inputs: list):
    clients_ids = []
    for e in inputs:
        if getattr(e, 'is_main'):
            clients_ids = e.value['id'].unique().tolist()
            break

    raw_clients = {}
    for e in inputs:
        for cid in clients_ids:
            if not cid in raw_clients:
                raw_clients[cid] = {}
            if e.name == 'cliente':
                # analisar a possibilidade de usar iloc
                # uma vez que os ids estao todos na primeira coluna
                df = e.value
                raw_clients[cid]['dados_pessoais'] = df[df['id'] == cid]
            elif e.name == 'compra':
                df = e.value
                raw_clients[cid]['compras'] = df[df['id_cliente'] == cid]
            elif e.name == 'redes_sociais':

                raw_clients[cid]['sm'] = [k['links'] for k in e.value if k['id_cliente'] == cid][0]
            else:
                print('Erro tipo nao definido', file=sys.stderr)

    return raw_clients