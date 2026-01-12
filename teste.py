import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constante gravitacional
g = 9.8

# Valores iniciais
m0 = 1.0     # massa (kg)
h0 = 10.0    # altura inicial (m)

# Espaço de alturas
h = np.linspace(0, h0, 100)

# Função para calcular energias
def energias(m, h_max):
    Ep = m * g * h
    Ec = m * g * (h_max - h)
    Em = Ep + Ec
    return Ep, Ec, Em

Ep, Ec, Em = energias(m0, h0)

# Criando a figura
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

l1, = ax.plot(h, Ep, label="Energia Potencial")
l2, = ax.plot(h, Ec, label="Energia Cinética")
l3, = ax.plot(h, Em, '--', label="Energia Mecânica")

ax.set_xlabel("Altura (m)")
ax.set_ylabel("Energia (J)")
ax.legend()
ax.set_title("Conservação da Energia Mecânica")

# Sliders
ax_m = plt.axes([0.2, 0.15, 0.65, 0.03])
ax_h = plt.axes([0.2, 0.1, 0.65, 0.03])

slider_m = Slider(ax_m, "Massa (kg)", 0.5, 10.0, valinit=m0)
slider_h = Slider(ax_h, "Altura inicial (m)", 1.0, 20.0, valinit=h0)

# Função de atualização
def update(val):
    m = slider_m.val
    h_max = slider_h.val
    h = np.linspace(0, h_max, 100)
    Ep, Ec, Em = energias(m, h_max)

    l1.set_data(h, Ep)
    l2.set_data(h, Ec)
    l3.set_data(h, Em)

    ax.set_xlim(0, h_max)
    ax.set_ylim(0, max(Em) * 1.1)

    fig.canvas.draw_idle()

slider_m.on_changed(update)
slider_h.on_changed(update)

plt.show()
