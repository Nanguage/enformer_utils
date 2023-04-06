from pathlib import Path
from enformer_utils.data.fasta import FastaFetcher
from enformer_utils.data.bigwig import BigwigFetcher
from enformer_utils.data.bed import BedIterator


test_data_dir = Path('tests/data')


def test_fasta():
    fetcher = FastaFetcher(
        (test_data_dir / 'test.fa').as_posix()
    )
    seq = fetcher.fetch('chr1', 0, 10)
    assert len(seq) == 10
    tensor = fetcher.fetch_tensor('chr1', 0, 10)
    assert tensor.shape == (1, 10)


def test_bigwig():
    fetcher = BigwigFetcher(
        [
            str(test_data_dir / 'bigwig_chr9_4000000_6000000.bw'),
            str(test_data_dir / 'bigwig_chr9_4000000_6000000.bw'),
        ],
        bins = 100
    )
    data = fetcher.fetch('chr9', 4000000, 6000000)
    assert data.shape == (2, 100)
    tensor = fetcher.fetch_tensor('chr9', 4000000, 6000000)
    assert tensor.shape == (1, 100, 2)


def test_bed_iterator():
    test_bed = "bed_chr9_4000000_6000000.bed"
    bed_iter = BedIterator(
        str(test_data_dir / test_bed)
    )
    for region in bed_iter:
        assert isinstance(region[1], int)
        assert isinstance(region[2], int)
        assert len(region) == 3
    bed_iter = BedIterator(
        str(test_data_dir / test_bed),
        only_region=False
    )
    for region in bed_iter:
        assert len(region) > 3
