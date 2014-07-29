BEGIN { FS = "\n"; RS = "" }
      { print "p edge " $2 }
      { cmd="echo " $3 " | e2dimacs"; system(cmd) }
