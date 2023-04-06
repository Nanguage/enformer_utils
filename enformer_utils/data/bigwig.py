from pathlib import Path
import typing as T

import numpy as np
import bbi
import torch

from .base import DataFetcher


class BigwigFetcher(DataFetcher):
    def __init__(self, paths: T.List[str], bins: int = 100) -> None:
        self.bigwig_paths = [
            Path(path).expanduser().resolve() for path in paths
        ]
        self.bins = bins

    def fetch(self, chrom, start, end) -> np.ndarray:
        """Fetch data from bigwig files.

        Returns:
            np.ndarray: shape (n_files, n_bins)
        """
        data = []
        for path in self.bigwig_paths:
            arr = bbi.fetch(
                path.as_posix(), chrom, start, end,
                bins=self.bins)
            data.append(arr)
        return np.array(data)

    def to_tensor(self, data) -> torch.Tensor:
        """Convert data to torch.Tensor.

        Returns:
            torch.Tensor: shape (1, n_bins, n_files)
        """
        return torch.tensor(data).unsqueeze(0).permute(0, 2, 1)
