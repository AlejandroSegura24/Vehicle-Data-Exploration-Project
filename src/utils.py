import matplotlib.pyplot as plt
import seaborn as sns

# Configuración global de las graficas
def configurar_graficas():
    sns.set_theme(
        style = 'whitegrid',
        palette = 'Set2',
        font_scale = 1.2
    )
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 14
plt.rcParams["axes.edgecolor"] = "gray"
plt.rcParams["axes.linewidth"] = 1
plt.rcParams["legend.facecolor"] = "white"
plt.rcParams["legend.frameon"] = True
plt.rcParams["legend.edgecolor"] = "gray"

# Función de reducción de datos
def track_data_reduction(data_before, data_after, filter_name="Filtro"):
    reduction = len(data_before) - len(data_after)
    percent = (reduction / len(data_before)) * 100 if len(data_before) > 0 else 0
    print(f"{filter_name}: {len(data_before)} -> {len(data_after)} filas ({reduction} eliminadas, {percent:.1f}% reducción)")