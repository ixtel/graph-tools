AWK Programs
------------

Programs in this folder are written in GNU AWK.

* `dimacs_split.awk` -- Splits a single file containing graphs in
  Dimacs format into a folder of files containing one graph per file.
* `e2dimacs.awk` -- Converts a file of graphs in edge list format into
  a file of graphs in Dimacs format. Depends on `e2dimacs` script.
* `e2gv.awk` -- Converts a file of graphs in edge-list format into a
  file of graphs in Graphviz DOT format. Depends on `e2gv` script.
* `gv_split.awk` -- Splits a single file containing graphs in Graphviz
  DOT format into a folder of files containing one graph per file.

TODO - The only difference between `dimacs_split.awk` and `gv_split.awk`
is the extension of the output files. So we really only need one program.
