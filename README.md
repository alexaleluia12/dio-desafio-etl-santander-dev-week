```txt

# Projeto de ETL do Santander Dev Week 2023

## Problema
Caregar os dados dos clientes que estão em diferentes fontes sobre o cliente
    clientes.csv - (id, nome, endereco, telefone)
    compras.csv - (id_cliente, id_compra, valor_total, data)
    redes-sociais.json - { id_cliente:string, links:list(string) }

Transformar em uma estrutura JSON por cliente e Salvar em um arquivo db.json em saida/
para ser caregado por um outro processo em background.

## executar depois de clonar
pip install -r requirements.txt
python main.py

```