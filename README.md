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

# complex-analysis

To run guise calculation for simplet:

```bash
python3.10 ./complex/test/guise_error_calculation_on_random_complex.py 
```