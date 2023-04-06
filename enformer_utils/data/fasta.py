from pyfaidx import Fasta
import torch

from .base import DataFetcher


class FastaFetcher(DataFetcher):
    def __init__(self, path: str) -> None:
        self.fasta = Fasta(path)
        self.base_to_int = {
            'A': 0,
            'C': 1,
            'G': 2,
            'T': 3,
            'N': 4,
        }

    def fetch(self, chrom, start, end) -> str:
        """Fetch sequence from FASTA file."""
        chr_obj = self.fasta[chrom]
        seq = chr_obj[start:end].seq
        return seq

    def to_tensor(self, data: str) -> torch.Tensor:
        """Convert a DNA sequence(has bases ATCGN)
        to a pytorch Tensor in shape (1, n)."""
        seq = data.upper()
        tensor = torch.tensor([self.base_to_int[base] for base in seq])
        # from shape [n] to shape [1, n]
        tensor = tensor.unsqueeze(0)
        return tensor
