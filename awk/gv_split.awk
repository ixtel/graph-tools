BEGIN { FS = "\n"; RS = ""; n=0; }
      { print >> n".gv"; n++; }
