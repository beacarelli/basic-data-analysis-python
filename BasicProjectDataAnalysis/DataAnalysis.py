# coding: utf-8

### IMPORTING MODULES AND FILES

import pandas as pd

#Reading the CSV file 'EmployeesRegister' using read_csv
funcionarios_df = pd.read_csv(r'/content/BasicProjectDataAnalysis/EmployeesRegister.csv', sep = ';', decimal = ',')

#Deleting columns that aren't relevant to the code
funcionarios_df = funcionarios_df.drop([r'Estado Civil', 'Cargo'], axis = 1)
print(funcionarios_df)  

#Reading the CSV file 'CustomerRegister' using read_csv
clientes_df = pd.read_csv(r'/content/BasicProjectDataAnalysis/CustomerRegister.csv', sep = ';', decimal = ',')
print(clientes_df)

#Reading the CSV file 'EmployeesRegister' using read_excel
base_df = pd.read_excel(r'/content/BasicProjectDataAnalysis/BaseServicesProvided.xlsx')
print(base_df)

### REVENUE

faturamentos_df = base_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente', 'Valor Contrato Mensal']])
faturamentos_df['Faturamento Total'] = clientes_df['Valor Contrato Mensal'] * base_df['Tempo Total de Contrato (Meses)']
print('O faturamento total da empresa foi de R${:,}'.format(faturamentos_df['Faturamento Total'].sum()))

### PERCENTAGE OF EMPLOYEES WHO CLOSED A CONTRACT

qtd_funcionarios_fecharam_contrato = len(base_df['ID Funcionário'].unique())
qtd_funcionarios_total = len(funcionarios_df['ID Funcionário'])
print('A porcentagem de funcionários que fecharam contrato foi de {:.2%}'.format(qtd_funcionarios_fecharam_contrato / qtd_funcionarios_total))

### NUMBER OF CONTRACTS CLOSED BY EACH DEPARTMENT

contratos_por_area = base_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on = 'ID Funcionário')
contratos_por_area_qtd = contratos_por_area['Area'].value_counts()
print(contratos_por_area_qtd)
contratos_por_area_qtd.plot(kind='bar')

### TOTAL NUMBER OF EMPLOYEES BY DEPARTMENT

funcionario_por_area = funcionarios_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on = 'ID Funcionário')
funcionario_por_area_qtd = funcionario_por_area['Area'].value_counts()
print(funcionario_por_area_qtd)
funcionario_por_area_qtd.plot(kind='bar')

### CALCULATION OF AVERAGE TICKET
ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print('O ticket médio é igual R$ {:,}'.format(ticket_medio))
