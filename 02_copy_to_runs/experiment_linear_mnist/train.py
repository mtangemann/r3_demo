"""Fits a linear classifier for MNIST."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

OUTPUT_PATH = Path("output")
OUTPUT_PATH.mkdir(exist_ok=True)


mnist = np.load("data/mnist.npz")

train_images = mnist["train_images"]
train_labels = mnist["train_labels"]
test_images = mnist["test_images"]
test_labels = mnist["test_labels"]


print("Fitting classifier...")
classifier = LogisticRegression(max_iter=10)
classifier.fit(train_images, train_labels)

train_score = classifier.score(train_images, train_labels)
test_score = classifier.score(test_images, test_labels)

print(f"Train accuracy: {train_score:.2%}")
print(f"Test accuracy: {test_score:.2%}")

with open(OUTPUT_PATH / "results.yaml", "w") as results_file:
    results_file.write(f"train_accuracy: {train_score:.2%}\n")
    results_file.write(f"test_accuracy: {test_score:.2%}")


print("Plotting examples...")
fig, axes = plt.subplots(3, 3, figsize=(5, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(test_images[i].reshape(28, 28), cmap="gray")
    ax.set_title(f"Predicted: {classifier.predict([test_images[i]])[0]}")
    ax.axis("off")
plt.tight_layout()
plt.savefig(OUTPUT_PATH / "examples.png")


print("Done!")
