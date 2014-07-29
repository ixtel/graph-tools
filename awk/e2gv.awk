BEGIN { FS = "\n"; RS = "" }
      { cmd="echo " $3 " | e2gv"; system(cmd) }
