# Import the libraries
from matplotlib import pyplot as plt
import numpy as np

dataset.sort_values("genre", inplace=True)

# Creating values (budget amount) for the bars
iN = len(dataset)
arrCnts = dataset["budget"] / 10000000
theta = np.arange(0, 2 * np.pi, 2 * np.pi / iN)
width = (2 * np.pi) / iN * 0.9

# Plot size and proportions
fig = plt.figure(figsize=(20, 18), frameon=False, dpi=200)

# Adding radial axes
ax = fig.add_axes([0.05, 0.05, 0.9, 0.9], polar=True)
bars = ax.bar(
    theta,
    arrCnts,
    width=width,
    bottom=15,
    color=dataset["Col"],
    alpha=0.65,
    edgecolor="yellow",
)
ax.set_xticks(theta)
plt.axis("off")
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

bottom = 15
rotations = np.rad2deg(theta)
y0, y1 = ax.get_ylim()

# Adding radial tags
for x, bar, rotation, label in zip(theta, bars, rotations, dataset["name"]):
    offset = (bottom + bar.get_height()) / (y1 - y0)
    lab = ax.text(0, 0, label, transform=None, ha="center", va="center", alpha=0.5)
    renderer = ax.figure.canvas.get_renderer()
    bbox = lab.get_window_extent(renderer=renderer)
    invb = ax.transData.inverted().transform([[0, 0], [bbox.width, 0]])
    lab.set_position((x, offset + (invb[1][0] - invb[0][0]) / 2.0 * 2.7))
    lab.set_transform(ax.get_xaxis_transform())
    lab.set_rotation(rotation)

fig.tight_layout()
plt.show()
