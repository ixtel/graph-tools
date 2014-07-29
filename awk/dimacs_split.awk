BEGIN { FS = "\n"; RS = ""; n=0; }
      { print >> n".dimacs"; n++; }
