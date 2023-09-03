

def format_client(client):
    """
    client: {
        dados_pessoais: df,
        compras: df,
        sm: list
    }
    criar dict de saida no padrao
    {
        id:int, nome:str, compras:[{id:int, valor:float, data:str}], sm: list[str]
    }
    """
    pass


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
                print('Erro tipo nao definido')

    return raw_clients