```txt

# Projeto de ETL do Santander Dev Week 2023

## Problema
Caregar os dados dos clientes que estão em diferentes fontes sobre o cliente
    clientes.csv - (id, nome, endereco, telefone)
    compras.csv - (id_cliente, id_compra, valor_total, data)
    redes-sociais.json - { id_cliente:string, links:list(string) }

Transformar em uma estrutura JSON por cliente e Salvar em um arquivo db.json em saida/
para ser caregado por um outro processo em background.

```

e={'is_df': True, 'value':                                id  ...         celular
1    'Marcelo Antonio Trump Fake'  ...   '11998746170'
2             'Miriam Nunes Fake'  ...   '11998746171'
3   'Milena Mendes Alves do Fake'  ...   '11998746172'
4    'Mario Jandir da Silva Fake'  ...            NULL
5   'Miguel Alves de Castro Fake'  ...            NULL

[5 rows x 4 columns]}
e={'is_df': True, 'value':     id_cliente  id_compra valor_total        data
0            1       12.0      827.90  2023-05-01
1            1       13.0      827.90  2023-05-02
2            1       14.0      827.90  2023-05-03
3            1       15.0      827.90  2023-05-05
4            1       16.0      827.90  2023-05-06
5            1       17.0      827.90  2023-05-07
6            1       18.0      827.90  2023-05-09
7            2       20.0      2180.0  2023-01-01
8            2       21.0      2180.0  2023-02-01
9            2       22.0      2180.0  2023-03-01
10           2       23.0      2180.0  2023-04-01
11           2       24.0      2180.0  2023-05-01
12           3       31.0       56.10  2023-05-11
13           5     5000.0  2023-02-10         NaN}
e={'is_df': False, 'value': [{'id_cliente': 1, 'links': ['https://www.facebook.com/marcelo_trump', 'https://www.tiktok.com/@marcelo_trump', 'https://www.instagram.com/marcelo_trump']}, {'id_cliente': 2, 'links': ['https://www.facebook.com/miriam_nunes', 'https://www.tiktok.com/@miriam_nunes', 'https://www.instagram.com/miriam_nunes']}, {'id_cliente': 3, 'links': ['https://www.instagram.com/milena_alves']}, {'id_cliente': 4, 'links': ['https://www.tiktok.com/@mario_jardim']}, {'id_cliente': 5, 'links': ['https://www.facebook.com/miguel_castro', 'https://www.instagram.com/miguel_castro']}]}
