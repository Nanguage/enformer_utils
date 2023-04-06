# A Demo for fine tuning the enformer-pytorch

**NOTE: This repo is still under development.**

## Requirements

The `Python>=3.8` is required. The required packages are listed in `requirements.txt`. You can install them by running the following command:

```bash
$ pip install -r requirements.txt
```

## About the demo data

The demo data is in `data` folder. But due to the size limit of GitHub,
it is not included in the repo.
You can create your own Fasta and bigwig data,
and change the path in relevant notebooks.


## Generate the target regions for fine tuning

```bash
python scripts/generate_target_region.py data/Sus_scrofa.Sscrofa11.1.dna.toplevel.chr.fa data/target_regions.bed --block_size=98304 --limit_chroms="['chr1']"
```

