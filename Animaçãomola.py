import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# -----------------------------
# CONFIGURAÇÕES
# -----------------------------

L0 = 4.0
compressao = 2.0
tempo_total = 8
frames = 240

# -----------------------------
# FUNÇÃO DA MOLA
# -----------------------------

def desenhar_mola(x_inicio, x_fim, y=0, voltas=18, amplitude=0.25):

    x = np.linspace(x_inicio, x_fim, 300)

    fase = np.linspace(0, voltas * 2 * np.pi, len(x))

    y_mola = y + amplitude * np.sin(fase)

    return x, y_mola


# -----------------------------
# CONFIGURAÇÃO DA FIGURA
# -----------------------------

fig, ax = plt.subplots(figsize=(10, 4))

ax.set_xlim(-1, 7)
ax.set_ylim(-1.5, 1.5)

ax.set_aspect('equal')

# Remove título e textos
ax.set_xticks([])
ax.set_yticks([])

# Parede
parede_x = 0

ax.plot(
    [parede_x, parede_x],
    [-1, 1],
    linewidth=8
)

# Bloco
bloco = plt.Rectangle(
    (4, -0.5),
    1,
    1
)

ax.add_patch(bloco)

# Mola
linha_mola, = ax.plot([], [], linewidth=3)


# -----------------------------
# ANIMAÇÃO
# -----------------------------

def atualizar(frame):

    t = frame / frames * tempo_total

    # Compressão
    if t < 2:

        progresso = t / 2

        comprimento = L0 - compressao * progresso

    # Mantém comprimida
    elif t < 3:

        comprimento = L0 - compressao

    # Solta e oscila
    else:

        tempo = t - 3

        comprimento = (
            L0
            - compressao
            * np.exp(-0.25 * tempo)
            * np.cos(4 * tempo)
        )

    # Posição do bloco
    bloco_x = parede_x + comprimento

    bloco.set_x(bloco_x)

    # Desenha a mola
    x, y = desenhar_mola(
        parede_x,
        bloco_x,
        voltas=18
    )

    linha_mola.set_data(x, y)

    return linha_mola, bloco


# -----------------------------
# CRIAÇÃO DA ANIMAÇÃO
# -----------------------------

animacao = FuncAnimation(
    fig,
    atualizar,
    frames=frames,
    interval=1000 * tempo_total / frames,
    blit=True
)

plt.close()

HTML(animacao.to_jshtml())
