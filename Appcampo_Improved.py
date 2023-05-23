# In[0]:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
    
dpi = 300
df = pd.read_excel('D:/OneDrive - Grupo EPM/10_Data_Field_App/Estaciones Hidrometereologicas_Second_read.xlsx')
columns_names_list = df.columns.tolist()
df_order = df.sort_values('Código IDEAM:')
df_order = df_order.sort_index().sort_index(axis=3)

#df_agregado = df.groupby('Código IDEAM:').sum().reset_index()

# Mostrar el nuevo DataFrame con los resultados de la agregación
#print(df_agregado)

grupo_estaciones = df.groupby('Código IDEAM:').sum()
#df1 = df['Código IDEAM:']= df.iloc[:, 1]
#df1 = grupo_estaciones.index
df1 = df_order['Código IDEAM:'] == grupo_estaciones.index[0]
#print(df[df.columns[1]])

for i in range(len(df_order)-1):
      #print(str(df_order.iloc[i]))
      print(df_order[df_order.columns[1]][i],df_order[df_order.columns[1]][i+1])
      if df_order[df_order.columns[1]][i] == df_order[df_order.columns[1]][i+1]:
          if datetime.strftime(df_order['Fecha del Mantenimiento Corregida'][i], "%Y-%m-%d")>datetime.strftime(df_order['Fecha del Mantenimiento Corregida'][i+1], "%Y-%m-%d"):
                 df.drop(i)
                 print ("if")
          else:
                 df.drop(i+1)
                 print ("Else")
                
print(datetime.strftime(df_order['Fecha del Mantenimiento Corregida'][5], "%Y-%m-%d"))      

# columnas_filtradas = ['Código IDEAM:']
# df_filtrado = df.drop_duplicates(subset=columnas_filtradas)

# Imprimir el DataFrame filtrado
#print(df_filtrado)
    
#Importar el archivo de Excel como un DataFrame
#df = pd.read_excel('ruta_del_archivo.xlsx')

# Filtrar los valores duplicados en las columnas especificadas
# 

df2 = df[df1]
deltafecha = datetime.now() - df2['Fecha del Mantenimiento Corregida']
print(deltafecha.min())



n = len(df.index)
x = np.arange(n)
width = 0.25

Valores_empty = df.isnull().sum()

comisiones = df["Comisión"].value_counts()

comisiones = ['Comisión Manuel-Andrés', 'Comisión William-Faustino', 'Comisión Hernando-Caloma', 'Comisión Norberto', 'Estaciones Sergio']
tipos_datalogger = ['.CR8', '.adc', '.CR1X', '.CR1', '.CR300', '.CR6']
Datalogger = ['CR800', 'Vaisala', 'CR1000X', 'CR1000', 'CR300 Series','CR6']

# Crear la tabla de conteo
data = {}
for comision in comisiones:
    data[comision] = {}
    for tipo in tipos_datalogger:
        tipo_datalogger = tipo.replace('.', '')  # Renombrar el tipo de datalogger
        data[comision][tipo_datalogger] = df[df['Comisión'] == comision]['Programa Estación:'].str.endswith(tipo, na=False).value_counts().get(True, 0)

# Crear el dataframe
df_logger = pd.DataFrame(data).T.reset_index()
df_logger.columns = ['Comisión'] + Datalogger

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(20, 1))

# Ocultar ejes
ax.axis('off')
ax.set_title('Datalogger instalados por comisión')

# Crear la tabla
table = ax.table(cellText=df_logger.values, colLabels=df_logger.columns, cellLoc='center', loc='upper left')

# Establecer estilo de la tabla
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

# Guardar la imagen
fig.savefig('tabla_logger.png', dpi=300, bbox_inches='tight', pad_inches=0.5)
# In[1]:
datosall = df[df["Registro"]>0]['Nombre Estación:'].value_counts()
yy = datosall.values.tolist()
xx = datosall.index.tolist()

datos = df["Funcionario(s):"].value_counts()
y = datos.values.tolist()
x = datos.index.astype(str).tolist()

datosZO = df[df["Comisión"]=='Comisión Manuel-Andrés']['Nombre Estación:'].value_counts()
yzo = datosZO.values.tolist()
xzo = datosZO.index.tolist()

datosNO = df[df["Comisión"]=='Comisión William-Faustino']['Nombre Estación:'].value_counts()
yno = datosNO.values.tolist()
xno = datosNO.index.tolist()

datosN = df[df["Comisión"]=='Comisión Hernando-Caloma']['Nombre Estación:'].value_counts()
yn = datosN.values.tolist()
xn = datosN.index.tolist()

datosNOR = df[df["Comisión"]=='Comisión Norberto']['Nombre Estación:'].value_counts()
ynor = datosNOR.values.tolist()
xnor = datosNOR.index.tolist()

datosSC= df[df["Comisión"]=='Estaciones Sergio']['Nombre Estación:'].value_counts()
ysc = datosSC.values.tolist()
xsc = datosSC.index.tolist()

fig, axall = plt.subplots(figsize=(30,5))
num_all = axall.bar(xx,yy)
for rect in num_all:
    height = rect.get_height()
    axall.text(rect.get_x() + rect.get_width()/2., height, '%d' % int(height),
            ha='center', va='bottom')
# for bar in axall.patches:
#   axall.text(bar.get_x() + bar.get_width() / 2,
#           bar.get_height() / 2 + bar.get_y(),
#           round(bar.get_height()), ha = 'center',
#           color = 'w', weight = 'bold', size = 10)  
axall.set_title('Mantenimientos totales por estación', color='black', weight='bold', size=10)
plt.xticks(rotation=90)
fig.savefig('Imagen0.png', dpi=dpi, bbox_inches='tight', overwrite=True)


fig, ax = plt.subplots(figsize=(20,10))
num_zo = ax.bar(xzo, yzo)
ax.set_xlabel("Estaciones")
ax.set_ylabel("Número de mantenimientos")
ax.set_title("Comisión Manuel-Andrés",color='black', weight='bold', size=10)
plt.xticks(rotation=90)
for rect in num_zo:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., height, '%d' % int(height),
            ha='center', va='bottom')
# Mostrar plot en la pantalla y guardar como imagen
fig.savefig('Imagen1.png', dpi=dpi, bbox_inches='tight', overwrite=True)

fig, ax1 = plt.subplots(figsize=(20,10))
num_no = ax1.bar(xno, yno)
ax1.set_xlabel("Estaciones")
ax1.set_ylabel("Número de mantenimientos")
ax1.set_title("Comisión William-Faustino",color='black', weight='bold', size=10)
plt.xticks(rotation=90)
for rect in num_no:
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2., height, '%d' % int(height),
            ha='center', va='bottom')
# Mostrar plot en la pantalla y guardar como imagen
fig.savefig('Imagen2.png', dpi=dpi, bbox_inches='tight', overwrite=True)

fig, ax2 = plt.subplots(figsize=(20,10))
num_n=ax2.bar(xn, yn)
ax2.set_xlabel("Estaciones")
ax2.set_ylabel("Número de mantenimientos")
ax2.set_title("Comisión Hernando-Caloma",color='black', weight='bold', size=10)
plt.xticks(rotation=90)
for rect in num_n:
    height = rect.get_height()
    ax2.text(rect.get_x() + rect.get_width()/2., height, '%d' % int(height),
            ha='center', va='bottom')
# Mostrar plot en la pantalla y guardar como imagen
fig.savefig('Imagen3.png', dpi=dpi, bbox_inches='tight', overwrite=True)

fig, ax3 = plt.subplots(figsize=(20,10))
num_nor=ax3.bar(xnor, ynor)
ax3.set_xlabel("Estaciones")
ax3.set_ylabel("Número de mantenimientos")
ax3.set_title("Comisión Norberto",color='black', weight='bold', size=10)
plt.xticks(rotation=90)
for rect in num_nor:
    height = rect.get_height()
    ax3.text(rect.get_x() + rect.get_width()/2., height, '%d' % int(height),
            ha='center', va='bottom')
# Mostrar plot en la pantalla y guardar como imagen
fig.savefig('Imagen4.png', dpi=dpi, bbox_inches='tight', overwrite=True)

fig, ax6 = plt.subplots(figsize=(20,10))
num_sc=ax6.bar(xsc, ysc)
ax6.set_xlabel("Estaciones")
ax6.set_ylabel("Número de mantenimientos")
ax6.set_title("Estaciones Sergio",color='black', weight='bold', size=10)
plt.xticks(rotation=90)
for rect in num_sc:
    height = rect.get_height()
    ax6.text(rect.get_x() + rect.get_width()/2., height, '%d' % int(height),
            ha='center', va='bottom')
# Mostrar plot en la pantalla y guardar como imagen
fig.savefig('Imagen5.png', dpi=dpi, bbox_inches='tight', overwrite=True)


fig, ax4 = plt.subplots(figsize=(20,10))
num_names = ax4.barh(x, y)
ax4.set_xlabel("Número de ocurrencias")
ax4.set_ylabel("Funcionarios")
ax4.set_title("Variedad de nombres funcionarios",color='black', weight='bold', size=10)
plt.xticks(rotation=90)
for index, value in enumerate(y):
    ax4.text(value+0.1, index - 0.1, str(value), color='black')
# Mostrar plot en la pantalla y guardar como imagen
fig.savefig('Imagen6.png', dpi=dpi, bbox_inches='tight', overwrite=True)

fig, ax5 = plt.subplots(figsize=(20,10))
nombres = ['Comisión William-Faustino', 'Comisión Hernando-Caloma', 'Comisión Manuel-Andrés', 'Comisión Norberto', 'Estaciones Sergio']
ax5.pie(comisiones, autopct='%1.2f%%', radius=0.9, textprops={'fontsize':8})
ax5.legend(nombres, loc="upper right", prop={'size': 10}, title='Comisión')
# Mostrar plot en la pantalla y guardar como imagen
fig.savefig('Imagen7.png', dpi=dpi, bbox_inches='tight', overwrite=True)

fig, ax6 = plt.subplots(figsize=(6,30))
num_empty = Valores_empty.plot(kind='barh', 
                  stacked=False, 
                  alpha=0.4, 
                  color='purple',
                  width=0.7, 
                  ax=ax6)
ax6.set_xlabel('Número de campos no diligenciados (en blanco)')
ax6.set_ylabel('Columnas(campo)')
ax6.set_title('Número de valores no diligenciados por por campos',color='black', weight='bold', size=10)
for rect in ax6.patches:
    width = rect.get_width()
    ax6.text(width+3, rect.get_y() + rect.get_height()/2.4, f"{int(width)}",
             ha='center', va='center', fontsize=10, color='black')
# Mostrar plot en la pantalla y guardar como imagen
fig.savefig('Imagen8.png', dpi=dpi, bbox_inches='tight', overwrite=True)

plt.xticks(rotation=90)
plt.show()

plt.show()
