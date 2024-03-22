"""Downloads the MNIST dataset and saves it as a .npz file."""

import gzip
import urllib.request
from pathlib import Path

import numpy as np

MNIST_ROOT = "http://yann.lecun.com/exdb/mnist/"
MNIST_FILES = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz",
]

DATA_PATH = Path("data")
DATA_PATH.mkdir(exist_ok=True)


print("Downloading MNIST dataset...")
for filename in MNIST_FILES:
    urllib.request.urlretrieve(
        f"{MNIST_ROOT}/{filename}", DATA_PATH / filename
    )


with gzip.open(DATA_PATH / "train-images-idx3-ubyte.gz", "rb") as f:
    train_images = np.frombuffer(f.read(), np.uint8, offset=16).reshape(-1,28*28)

with gzip.open(DATA_PATH / "train-labels-idx1-ubyte.gz", "rb") as f:
    train_labels = np.frombuffer(f.read(), np.uint8, offset=8)

with gzip.open(DATA_PATH / "t10k-images-idx3-ubyte.gz", "rb") as f:
    test_images = np.frombuffer(f.read(), np.uint8, offset=16).reshape(-1, 28 * 28)

with gzip.open(DATA_PATH / "t10k-labels-idx1-ubyte.gz", "rb") as f:
    test_labels = np.frombuffer(f.read(), np.uint8, offset=8)


print(f"{train_images.shape=}")
print(f"{train_labels.shape=}")
print(f"{test_images.shape=}")
print(f"{test_labels.shape=}")


np.savez(
    DATA_PATH / "mnist.npz",
    train_images=train_images,
    train_labels=train_labels,
    test_images=test_images,
    test_labels=test_labels,
)
