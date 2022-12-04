BEGIN {
   total=0;
   max=0;
}

{
    print $0;
    if ($0 > 0) {
        print "adding ", $0;
        total+= $0;
    } else {
        print "checking max? ", total, max;
        if (total > max) {
            print "new max (old) : ", total, " (", max, ")";
            max=total;
        };
        total=0;
        print "now new max is ", max;
    }
    print total, max;
    print "\n";
}

END {print "max is ", max; }
