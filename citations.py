
from scholarly import scholarly, ProxyGenerator
from scholarly.publication_parser import PublicationParser
from fp.fp import FreeProxy
import yaml
import operator

# FLAME GPU publications
flame_pubs =  ['High performance cellular level agent-based simulation with FLAME for the GPU',
              'FLAME: simulating large populations of agents on parallel hardware architectures',
              'A high performance agent based modelling framework on graphics card hardware with CUDA',
              'Template-driven agent-based modeling and simulation with CUDA',
              'Simulating heterogeneous behaviours in complex systems on GPUs',
              'FLAME GPU technical report and user guide (CS-11-03)',
              'Resolving conflicts between multiple competing agents in parallel simulations' ]

# Free proxies get blocked
#proxy_generator = ProxyGenerator()
#proxy_generator.FreeProxies()
scholarly.use_proxy(None)


# open file for dumping flame publication details
f_pubs = open("_data/publications.yml", "w")
f_cites = open("_data/citations.yml", "w")

all_pubs = []
all_cites = []
for paper_title in flame_pubs:
    results = scholarly.search_pubs(paper_title)
    pubs = [p for p in results]
    assert len(pubs) > 0 # Paper not found?
    print(f"Found '{paper_title}'.")

    # fill by querying site
    pub = scholarly.fill(pubs[0])
    all_pubs.append(pub)
    print(f"Details returned for  '{paper_title}'.")

    # get all publications that cite the current paper
    cites = [dict(c, **{'flame_paper': paper_title}) for c in scholarly.citedby(pub)]
    all_cites.extend(cites)
    print(f"Found {len(cites)} citations for '{paper_title}'\n")

    # dump to file
    #f_pubs.write(yaml.dump([pubs]))
    #f_cites.write(yaml.dump([cites]))


# remove duplicates from citations list
unique_cites = []
for p in all_cites:
    if p not in unique_cites:
        unique_cites.append(p)

# remove cross refs to pubs
#for p in all_pubs:
#    unique_cites = [x for x in unique_cites if not (p.get('title') == x.get('tile'))]

# sort by citations
sorted_pubs = sorted(all_pubs, key=lambda k: k['num_citations'], reverse=True) 
sorted_cites = sorted(unique_cites, key=lambda k: k['num_citations'], reverse=True) 

# dump to file
f_pubs.write(yaml.dump(sorted_pubs))
f_cites.write(yaml.dump(sorted_cites))

# close file for flame publication details
f_pubs.close()
f_cites.close()