<h1>Day 1 - part 1</h1>

<p>URL: https://adventofcode.com/2022/day/1
</br>


<h1>Summary (by me):</h1>
<p>Giving input of numbers, grouped with empty line to split "values for each elve", count total per elve and return total from elves with maximum total.


<h1>Solution:</h1>
<p>Run awk script against input.txt:
<code>

   awk -f findMax.awk input.txt
</code>

<p>Which means:</p>
<ol>
<li>run awk programme.</li>
<li>rather than taking script as input, read script from file "findMax.awk"</li>
<li>proces input file "input.txt".</li>
</ol>

<h2>note:</h2>
<ul>
<li>Could have done</br>
<code>
     cat input.txt | awk -f findMax.awk
</code>
</li>
<li>What is Awk?
<p>AWK (awk) is a domain-specific language designed for text processing and typically used as a data extraction and reporting tool. Like sed and grep, it is a filter, and is a standard feature of most Unix-like operating systems.
<p>AWK was initially developed in 1977 by Alfred Aho (author of egrep), Peter J. Weinberger (who worked on tiny relational databases), and Brian Kernighan. AWK takes its name from their respective initials.
</li>
</ul>
</br>

<h2>findMax.awk explained:</h2>
<code>

        BEGIN {
           total=0;
           max=0;
        }

        {
            print $0;                              # debug - print each value
            if ($0 > 0) {
                print "adding ", $0;               # debug - show that we are adding
                total+= $0;
            } else {
                print "checking max? ", total, max;
                if (total > max) {
                    print "new max (old) : ", total, " (", max, ")";  # debug - found a new max
                    max=total;
                };
                total=0;                           # need to reset total to 0; will start new elf
                print "now new max is ", max;
            }
            print total, max;
            print "\n";
        }

        END {print "max is ", max; }               # solution: print out the total variable
</code>

<h2>Notes:</h2>
<ul>
<li>In awk, variable do not take $; only the "input arguments" for each line.
<p>i.e. $1, $2, $3 for 1st, 2nd or 3rd argument (separated by white space by default) of each line.
<p>  -> That's why you have
<code>
         total += $0
</code>
 <p>i.e. same as
 <code>
         total = total + $0
</code>
<p>which is add (entire line) to total variable.
</li>
<li>Awk tries to magically convert things... so entire line ($0) can be added and it will try to convert it into an integer. Since our input file has only numbers one each line, it works.
<p>If we had some text , it probably would end-up being 0.</p>
</li>
<li>The $0 argument means "the entire line".</li>
<li>Awk executes the "main script part" for each line; but has a BEGIN and END section which are run only once, before processing any lines AND after processing all lines.</li>




<h1>Detailed Description (from web site):</h1>
<h2> --- Day 1: Calorie Counting ---</h2>
<p>Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver presents on Christmas. For that, their favorite snack is a special type of star fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.
<p>To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.
<p>Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
<p>The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).
<p>The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.
<p>For example, suppose the Elves finish writing their items' Calories and end up with the following list:
</br>
<code>
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
</code>
<p> This list represents the Calories of the food carried by five Elves:

</br>
<p>The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
<p>The second Elf is carrying one food item with 4000 Calories.
<p>The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
<p>The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
<p>The fifth Elf is carrying one food item with 10000 Calories.
<p>In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

<p>Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?


