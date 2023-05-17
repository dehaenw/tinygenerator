# tiny generator

do you love to generate random molecules but are you sick and tired of dependencies, black boxes and bloated weights of contemporary methods? then this is the script for you!

using a privileged set of chembl-mined reduced graphs and fragments, this script generates random molecules using string operations. the output is (highly non-canonical) rdkit parsable SMILES strings

## example usage

```python tiny_generator.py 1000 0.5```

generate 1000 molecules with a weight adjustment of 0.5 and print them out. there is no clutter printed so you can also pipe it to a smi file using

```python tiny_generator.py 1000 0.5 > random_molecules.smi```

the weight adjustment parameter should be around 1: lower means more weight to more uncommon fragments and thus more diverse molecules, higher means more weight to more common fragments, thus less diverse molecules.

## some stats
time to generate 1 million molecules: 76.1 sec on 1 CPU core (Intel® Core™ i5-6600 CPU @ 3.30GHz × 4 ). ~99.9% of the strings were unique.

## a word of warning
currently, the merging strategy is purely random. this means some of the molecules will have unstable functionality in there like haloamine, aminals, etc
