from terminaltables import AsciiTable

# Input de valores da acoes
print('Informe o valor das ações separados por vigulas, (ex: 7,1,5,3,6,4)')
array_k = list(input('digite aqui: '))

array_y =  {}
headers = []
rows = []
i =1

# Setando valores no dicionario array_y
for x in array_k:
    if x != ',':
        array_y[i] = int(x)
        headers.append(str(i) + '° dia')
        rows.append('R$ ' + str(x))
        i+=1

# Montando table com valores de cada dia
table_data = [headers, rows]
table = AsciiTable(table_data)
print (table.table)

# Input dos dias de compra e venda das acoes
dia_compra = int(input('Informe dia da compra da ação(apenas numero): '))
dia_venda = int(input('Informe dia da venda da ação(apenas numero): '))

# Determinando  maior lucro 
if dia_venda < dia_compra:
    print('Está ação não está mais dispónivel para venda :(')
elif array_y.get(dia_compra) > array_y.get(dia_venda):
    print(0)
else:
    lucro = array_y.get(dia_venda) - array_y.get(dia_compra)
    print(f'Lucro: {lucro}')