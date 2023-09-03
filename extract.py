import json
from types import SimpleNamespace

import pandas

INPUT_FOLDER = './files'
INPUT_FILES = [
    SimpleNamespace(
        src=f'{INPUT_FOLDER}/clientes.csv',
        name='cliente',
    ),
    SimpleNamespace(
        src=f'{INPUT_FOLDER}/compras.csv',
        name='compra',
    ),
    SimpleNamespace(
        src=f'{INPUT_FOLDER}/redes-sociais.json',
        name='redes_sociais',
    ),
]

def read_imputs():
    """
    Carrega dados csv e json em memória
    """
    inputs = []
    for source in INPUT_FILES:

        if source.src.endswith('.csv'):
            data = pandas.read_csv(source.src, quotechar="'")
            inputs.append(SimpleNamespace(
                is_df=True,
                is_main=source.name == 'cliente',
                value=data,
                name=source.name,
            ))
        else:
            # todo usar pandas para ler json
            with open(source.src) as file:
                data = json.load(file)
                inputs.append(SimpleNamespace(
                    is_df=False,
                    value=data,
                    name=source.name,
                ))

    return inputs