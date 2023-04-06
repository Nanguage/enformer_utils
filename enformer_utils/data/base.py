import typing as T
import torch


class DataFetcher():

    def fetch(self, chrom, start, end) -> T.Any:
        pass

    def to_tensor(self, data) -> torch.Tensor:
        return torch.tensor(data)

    def fetch_tensor(self, chrom, start, end, *args, **kwargs) -> torch.Tensor:
        data = self.fetch(chrom, start, end, *args, **kwargs)
        tensor = self.to_tensor(data)
        return tensor

