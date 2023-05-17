# tiny generator

do you love to generate random molecules but are you sick and tired of dependencies, black boxes and bloated weights of contemporary methods? then this is the script for you!

using a privileged set of chembl-mined reduced graphs and fragments, this script generates random molecules using string operations. the output is (highly non-canonical) rdkit parsable SMILES strings

## example usage

```python tiny_generator.py 1000 0.5```

generate 1000 molecules with a weight adjustment of 0.5 and print them out. there is no clutter printed so you can also pipe it to a smi file using

```python tiny_generator.py 1000 0.5 > random_molecules.smi```

the weight adjustment parameter should be around 1: lower means more weight to more uncommon fragments and thus more diverse molecules, higher means more weight to more common fragments, thus less diverse molecules.

you can also use it in your script by:
```python
import tiny_generator
gm=tiny_generator.gen_mols(10,0.5)
```

## example output

the output are uncanonized smiles, such as the below ones:
```
C%10C.C%10CO%11.C%111=C%12C(=O)c2ccccc2C1=O.Cl%12
C%10(=O)OCCCC.C%101CCCN1%11.c%111ccc%12c%13c1.C%12(=O)OCC.c%131cn%14cn1.C%14
```

these look funny but are totally grammatical and parsable. the equivalent canonized version of these molecules are
```
CCCCOC1=C(Cl)C(=O)c2ccccc2C1=O
CCCCOC(=O)C1CCCN1c1ccc(C(=O)OCC)c(-c2cn(C)cn2)c1
```

for quick rendering of SMILES using rdkit backend I recommend pasting into the [RDKit.js web demo](https://rdkit.org/rdkitjs/beta/demo.html)

## some stats
time to generate 1 million molecules (weight adjustment 0.5): 76.1 sec on 1 CPU core (Intel® Core™ i5-6600 CPU @ 3.30GHz × 4 ). ~99.9% of the strings were unique.

## a word of warning
currently, the merging strategy is purely random. this means some of the molecules will have unstable functionality in there like haloamine, aminals, etc
