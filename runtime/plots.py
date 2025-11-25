# runtime/plots.py
# Versión sin librerías externas - ASCII plots

def _auto_scale(values):
    """Normaliza valores para graficar en texto."""
    if not values:
        return []
    mn = min(values)
    mx = max(values)
    if mx - mn == 0:
        return [5 for _ in values]  # línea plana
    return [int((v - mn) / (mx - mn) * 10) for v in values]


def plot_line(x, y, title="Grafica de Linea", xlabel="x", ylabel="y"):
    print("\n====", title, "====")
    y_norm = _auto_scale(y)
    for i in range(len(y_norm)):
        print(f"{x[i]} | " + ("#" * y_norm[i]))
    print("==============\n")


def plot_scatter(x, y, title="Grafica Scatter", xlabel="x", ylabel="y"):
    print("\n====", title, "====")
    y_norm = _auto_scale(y)
    for i in range(len(y_norm)):
        print(f"{x[i]} | " + ("*" * y_norm[i]))
    print("==============\n")


def plot_bar(labels, values, title="Grafica de Barras"):
    print("\n====", title, "====")
    v_norm = _auto_scale(values)
    for i in range(len(v_norm)):
        print(f"{labels[i]} | " + ("█" * v_norm[i]))
    print("==============\n")


def plot_hist(data, bins=10, title="Histograma"):
    print("\n====", title, "====")
    if not data:
        print("No hay datos.")
        return

    mn = min(data)
    mx = max(data)
    step = (mx - mn) / bins if bins > 0 else 1

    # Inicializar contadores
    counts = [0] * bins

    for v in data:
        idx = int((v - mn) / step)
        if idx == bins:
            idx -= 1
        counts[idx] += 1

    counts_norm = _auto_scale(counts)

    for i in range(bins):
        print(f"Bin {i} | " + ("#" * counts_norm[i]))

    print("==============\n")
