# graphlet-analysis
Graph analysis using graphlets.
Graphlets are small structures in the graph.

The "network-repository" folder contains real graph, to run guise calculation on them run following command:

```bash
python3.10 ./graph/test/guise_error_on_input_graph.py < ./network-repository/chesapeake.mtx 
```
and for the random graph guise calculation run:

```bash
python3.10 ./graph/test/guise_error_calculation.py
```
the first input for above command is n (number of nodes) and the second one is p (floating poing number of probability of apearance of each vertex) 

# complex-analysis

We extend a variant of the Erdos-Reyni model to generate random simplicial complexes. Our random complexes have up to three dimensional simplices. Our model has four parameters: n is the number of vertices in the complex, and $p,q,r$ are the probability values.

To run guise calculation for simplet:

```bash
python3.10 ./complex/test/guise_error_calculation_on_random_complex.py 
```
the first input for above command is n and the second one is p and third one is q and fourth one is r.

For all $n,p,q,r$, consider a random simplicial complex $\mathcal{K}(n,p,q,r)$ defined over $n$ vertices, where each edge is inclusively present in the complex with an independent probability $p$. Additionally, for every complete subgraph of three vertices, a corresponding triangle is independently present in the complex with a probability $q$. Furthermore, a corresponding tetrahedron is independently present in the complex with a probability $r$ for each complete subgraph with four vertices and four associated triangles.
