import gzip,pickle,random,sys

[CCONN,NSSD,NSSDW,CGC] = pickle.load(gzip.open("model1000.pkl.gz"))
    
def gen_mol(adj_weights):
    """ pick random reduced graph, populate with random chembl derived frags,
    join them using string operations. result: rdkitparsable SMILES
    """
    g=random.choices(CCONN,CGC,k=1)[0]
    ds=[len(el) for el in g]
    fr=[random.choices(NSSD[d],adj_weights[d])[0] for d in ds]
    ringclosures = ["%"+str(i+10) for i in range(sum(ds)//2)]
    for i,rc in enumerate(g):
        for j in rc:
            fr[i]=fr[i].replace("(*)",ringclosures[j],1)
    fr=".".join(fr)
    return fr

def gen_mols(N=1000,adj=0.9):
    N,adj=int(N),float(adj)
    adj_weights={}
    for k in NSSDW:
        adj_weights[k]=[a**adj for a in NSSDW[k]]
    cmpds = [gen_mol(adj_weights) for i in range(N)]
    return cmpds

if __name__=="__main__":
    gm=gen_mols(*sys.argv[1:])
    for smi in gm:
        print(smi)
