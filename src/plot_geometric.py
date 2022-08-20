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
norm_squarenesses = [geometric_squareness(num)/num for num in nums]

plot_xs = np.linspace(2, 50_000, 1_000)

xs, ys = nums, squarenesses
y_min, y_max = 0, 1

# Basic to 50,000
fig, ax = plt.subplots(figsize=(20, 20))
ax.scatter(xs, ys)
ax.set_xlabel("Number")
ax.set_ylabel("Squareness")
ax.set_title("Geometric Squareness")
ax.set_ylim(y_min, y_max)
percent_formatter = tck.PercentFormatter(y_max)
ax.yaxis.set_major_formatter(percent_formatter)
plt.savefig(GRAPH_PARENT_PATH / "geometric_squareness_basic_to_50000.png")

# squareness per $n$ to 50,000 to see gradient of lines in originalk plot
xs, ys = nums, norm_squarenesses
ymin, ymax = 0, 0.0025
fig, ax = plt.subplots(figsize=(20, 20))
ax.scatter(xs, ys)
ax.set_xlabel("Number")
ax.set_ylabel("Squareness per $n$")
ax.set_title("Geometric Squareness per $n$")
ax.set_ylim(ymin, ymax)
plt.savefig(GRAPH_PARENT_PATH / "geometric_squareness_normalized_to_50000.png")

# squareness per $n$ to 50,000 to see gradient of lines in originalk plot
# with value lines
xs, ys = nums, norm_squarenesses
ymin, ymax = 0, 0.0025
fig, ax = plt.subplots(figsize=(20, 20))
ax.scatter(xs, ys)
ax.set_xlabel("Number")
ax.set_ylabel("Squareness per $n$")
ax.set_title("Geometric Squareness per $n$")
ax.set_ylim(ymin, ymax)
for val in range(2,70):
    ax.axhline(1/val**2, ls='--', color='black')
plt.savefig(GRAPH_PARENT_PATH / "geometric_squareness_normalized_to_50000_lines.png")