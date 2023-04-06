import typing as T
import pyfaidx
import fire


def gen_regions(
        fa_path: str,
        out_path: str,
        block_size=1000,
        overlap=0,
        n_ratio_threshold=0.1,
        limit_chroms: T.Optional[T.List[str]] = None,
        ) -> None:
    fa = pyfaidx.Fasta(fa_path)
    with open(out_path, 'w') as fo:
        for chrom in fa.keys():
            if (limit_chroms is not None) and (chrom not in limit_chroms):
                continue
            chrom_len = len(fa[chrom])
            for start in range(0, chrom_len, block_size - overlap):
                end = min(start + block_size, chrom_len)
                print(chrom, start, end, sep='\t')
                seq: str = fa[chrom][start:end].seq
                n_ratio = seq.count('N') / len(seq)
                if n_ratio > n_ratio_threshold:
                    print(f'N ratio {n_ratio} > {n_ratio_threshold}')
                    print('Skip this region')
                    continue
                print(chrom, start, end, sep='\t', file=fo)


if __name__ == '__main__':
    fire.Fire(gen_regions)
