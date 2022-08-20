"""Plot geometric squareness on a graph
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

from nav import GRAPH_PARENT_PATH
from squareness import geometric_squareness

plt.style.use("calibri18.mplstyle")

nums = list(range(2, 50_000))
squarenesses = [geometric_squareness(num) for num in nums]

plot_xs = np.linspace(2, 50_000, 1_000)

xs, ys = nums, squarenesses
y_min, y_max = 0, 1

# Basic to 50,000
fig, ax = plt.subplots(figsize=(20, 20))
ax.scatter(xs, ys)
ax.set_xlabel("Number")
ax.set_ylabel("Squareness")
ax.set_title("Geo Squareness")
ax.set_ylim(y_min, y_max)
percent_formatter = tck.PercentFormatter(y_max)
ax.yaxis.set_major_formatter(percent_formatter)
plt.savefig(GRAPH_PARENT_PATH / "geometric_squareness_basic_to_50000.png")

# Up to 50,000 with fitted lines
fig, ax = plt.subplots(figsize=(20, 20))
ax.scatter(xs, ys)
ax.set_xlabel("Number")
ax.set_ylabel("Squareness")
ax.set_title("Geometric Squareness")
ax.set_ylim(y_min, y_max)
ax.plot(plot_xs, 1/10_000*plot_xs, ls='--', color='black')
percent_formatter = tck.PercentFormatter(y_max)
ax.yaxis.set_major_formatter(percent_formatter)
# plt.savefig(GRAPH_PARENT_PATH / "geometric_squareness_to_50000_lines.png")
