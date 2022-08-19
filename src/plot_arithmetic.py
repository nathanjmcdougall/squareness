"""Plot arithmetic squareness on a graph
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

from nav import GRAPH_PARENT_PATH
from squareness import arithmetic_squareness

plt.style.use("calibri18.mplstyle")

nums = list(range(2, 5_000))
squarenesses = [arithmetic_squareness(num) for num in nums]

xs, ys = nums, squarenesses
y_min, y_max = 0, 1

# Basic to 5000
fig, ax = plt.subplots(figsize=(10, 20))
ax.scatter(xs, ys)
ax.set_xlabel("Number")
ax.set_ylabel("Squareness")
ax.set_title("Arithmetic Squareness")
ax.set_ylim(y_min, y_max)
percent_formatter = tck.PercentFormatter(y_max)
ax.yaxis.set_major_formatter(percent_formatter)
plt.savefig(GRAPH_PARENT_PATH / "arithmetic_squareness_basic_to_5000.png")

# To 5000 but with added asymptote lines
fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(xs, ys)
ax.set_xlabel("Number")
ax.set_ylabel("Squareness")
ax.set_title("Arithmetic Squareness")
ax.set_ylim(y_min, y_max)
for idx in range(1, 10):
    ax.axhline(idx / (idx + 1), ls="--", color="black")
percent_formatter = tck.PercentFormatter(y_max)
ax.yaxis.set_major_formatter(percent_formatter)
plt.savefig(GRAPH_PARENT_PATH / "arithmetic_squareness_to_5000_asymptotes.png")
