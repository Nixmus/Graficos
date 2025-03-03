import matplotlib.pyplot as plt
import pandas as pd
import datetime
from matplotlib.dates import WeekdayLocator, DateFormatter

# Crear los datos
df = pd.DataFrame([
    ['Investigación y recolección de datos', '2024-02-05', '2024-02-19'],
    ['Diseño del SIG y estructura de datos', '2024-02-20', '2024-03-05'],
    ['Desarrollo de la aplicación', '2024-03-06', '2024-04-20'],
    ['Pruebas y corrección de errores', '2024-04-21', '2024-05-05'],
    ['Implementación piloto', '2024-05-06', '2024-05-20'],
    ['Socialización con la comunidad', '2024-05-21', '2024-05-30'],
    ['Ajustes finales y entrega', '2024-06-01', '2024-06-15']
], columns=['Tarea', 'Inicio', 'Fin'])

# Convertir fechas a datetime
df['Inicio'] = pd.to_datetime(df['Inicio'])
df['Fin'] = pd.to_datetime(df['Fin'])

# Calcular la duración de cada tarea
df['Duración'] = (df['Fin'] - df['Inicio']).dt.days

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_ylim(-0.5, len(df) - 0.5)
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['Tarea'])
ax.grid(True, axis='x', linestyle='--', alpha=0.7)
ax.grid(True, axis='y', linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Configurar los límites del eje x
ax.set_xlim(df['Inicio'].min() - pd.Timedelta(days=5),
            df['Fin'].max() + pd.Timedelta(days=5))

# Formato de fechas en el eje x
ax.xaxis.set_major_formatter(DateFormatter('%d-%b'))
ax.xaxis.set_major_locator(WeekdayLocator(byweekday=0))  # Mostrar lunes

# Crear las barras del Gantt
for idx, row in df.iterrows():
    start_date = row['Inicio']
    duration = row['Duración']
    ax.barh(idx, duration, left=start_date, height=0.3, 
            color='cornflowerblue', alpha=0.8)

# Rotar y alinear las etiquetas del eje x
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

# Añadir títulos y etiquetas
plt.title('Línea de Tiempo del Proyecto SIG', pad=20, fontsize=12)
plt.xlabel('Fecha', fontsize=10)

# Ajustar los márgenes
plt.tight_layout()

# Mostrar el gráfico
plt.show()
