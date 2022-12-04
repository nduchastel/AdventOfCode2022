BEGIN {
   total=0;
   max1=0;
   max2=0;
   max3=0;
}

{
    print $0;
    if ($0 > 0) {
        print "adding ", $0;
        total+= $0;
    } else {
        print "rebalance max(es): ", max1, max2, max3;
        print "find biggest max";
        if (max2 > max1  && max2 > max3) {
            print "max2 is largest";
            if (max1 > max3) {
                print "order is max2, max1, max3";
                temp=max1;
                max1=max2;
                max2=temp;
            } else {
                print "order is max2, max3, max1";
                temp=max1;
                max1=max2;
                max2=max3;
                max3=temp;
            }
        } else if (max3 > max1 && max3 > max2) {
            print "max3 is largest";
            if (max1 > max2) {
                print "order is max3, max1, max2";
                temp=max1;
                max1=max3;
                max3=max2;
                max2=temp
            } else {
                print "order is max3, max2, max1";
                temp=max1;
                max1=max3;
                max3=temp;
            }
        } else {
            print "max1 is largest";
            if (max2 > max3) {
                print "order is max1, max2, max3";
            } else {
                print "order is max1, max3, max2";
                temp=max2;
                max2=max3;
                max3=temp;
            }
        }
        print "new max(s) order is ", max1, max2, max3;
        print "checking max? ", total, max1, max2, max3;
        if (total > max3) {
            print "new max3 (old) : ", total, " (", max3, ")";
            max3=total;
        } else if (total > max2) {
            print "new max2 (old) : ", total, " (", max2, ")";
            max2=total;
        } else if (total > max1) {
            print "new max1 (old) : ", total, " (", max1, ")";
            max3=total;
        }
        total=0;
        print "now new max(es) are", max1, max2, max3;
    }
    print total, max1, max2, max3
    print "\n";
}

END {
    print "max(s) are ", max1, max2, max3;
    print "sum of top 3 elves are ", max1+max2+max3
}
