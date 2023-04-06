from pathlib import Path


class BedIterator():
    def __init__(self, path: str, only_region: bool = True) -> None:
        self.path = Path(path)
        self.only_region = only_region

    def __iter__(self):
        with self.path.open('r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                items = line.strip().split('\t')
                items[1] = int(items[1])
                items[2] = int(items[2])
                if self.only_region:
                    yield items[:3]
                else:
                    yield items
