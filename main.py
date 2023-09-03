from extract import read_imputs
from transform import clients_from
import pandas as pd

if __name__ == "__main__":
    # agrupamento feitos
    files = read_imputs()
    clients = clients_from(files)
    print(clients)
    """
    df = pd.read_csv('./files/clientes.csv', quotechar="'")
    # print(df.head(10))
    print(df['id'].unique().tolist())
    print()
    print(df['endereco'])
    """
