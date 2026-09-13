import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import FancyBboxPatch, Circle
from IPython.display import HTML

FPS = 30
DURACAO = 5
TOTAL_FRAMES = FPS * DURACAO

fig, ax = plt.subplots(figsize=(12, 7))

fig.patch.set_facecolor("#111111")
ax.set_facecolor("#111111")

ax.set_xlim(0, 100)
ax.set_ylim(0, 70)
ax.axis("off")

# Título
ax.text(
    50, 64,
    "⚡ FORÇA & MOVIMENTO ⚡",
    color="white",
    fontsize=28,
    fontweight="bold",
    ha="center"
)

# Chão
ax.plot([5, 95], [15, 15], color="white", linewidth=5)

# Carrinho
carro = FancyBboxPatch(
    (5, 15),
    10,
    5.5,
    boxstyle="round,pad=0.1,rounding_size=1",
    facecolor="#e63946"
)
ax.add_patch(carro)

# Rodas
roda1 = Circle(
    (7, 14.2),
    1.5,
    facecolor="#222222",
    edgecolor="white",
    linewidth=2
)

roda2 = Circle(
    (13, 14.2),
    1.5,
    facecolor="#222222",
    edgecolor="white",
    linewidth=2
)

ax.add_patch(roda1)
ax.add_patch(roda2)

# Força
forca = ax.text(
    5, 32,
    "➜ F = Força",
    color="#00ff88",
    fontsize=20,
    fontweight="bold"
)

# Velocidade
velocidade = ax.text(
    5, 25,
    "➜ v = Movimento",
    color="#00aaff",
    fontsize=18,
    fontweight="bold"
)

# Texto
ax.text(
    50, 7,
    "Quanto maior a força aplicada, maior pode ser a aceleração do objeto.",
    color="white",
    fontsize=15,
    ha="center"
)

ax.text(
    50, 3,
    "F = m · a",
    color="white",
    fontsize=22,
    fontweight="bold",
    ha="center"
)

# ANIMAÇÃO
def animar(frame):

    progresso = frame / (TOTAL_FRAMES - 1)

    x = 5 + progresso * 80

    carro.set_x(x)

    roda1.center = (x + 2, 14.2)
    roda2.center = (x + 8, 14.2)

    forca.set_position((x, 32))
    velocidade.set_position((x, 25))

    return carro, roda1, roda2, forca, velocidade


animacao = FuncAnimation(
    fig,
    animar,
    frames=TOTAL_FRAMES,
    interval=1000 / FPS,
    blit=True
)

# MOSTRAR NO GOOGLE COLAB
HTML(animacao.to_jshtml())
