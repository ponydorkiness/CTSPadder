# Padding Cyclic Tag Systems (CTS)

Cyclic Tag Systems sometimes require **padding** to ensure they compute the same function while meeting specific constraints. 
For example, in **Rule 110 compilation**, CTS programs must have lengths that are multiples of 6.

## Padding


Given a CTS program:

```
["011011", "011011"]
```

You can pad it with 6 cells:

```
['000000' + '011011', '000000' + '011011']
```

or equivalently:

```
["000000011011", "000000011011"]
```

Both versions are **functionally equivalent**; the padding does not change the computation, it only adjusts the program length.
However not all paddings are created equally, because certain paddings messes up timings, so we have to create a program *this program* to find paddings that don't mess up the state history.
This technique is essential when preparing CTS programs for **Rule 110 compilation**, ensuring all rules have lengths divisible by 6.

## Retrieving the state history.

Two check if two programs with padding are **functionally equvalent** a history of their states must be made.
Given the ruleset [1,101] an example run of getting it's state history looks like this.

```
1
> 0  # This means we will append 0, because we see a 1 has been hit in the tape and we are in rule 0.
1
> 1
101
> 0
011
11   # As you can see nothing is being appened at this step because the zero doesn't affect the state history.
> 0

# So the state history of this program for the first 4 appendings is
0*1*0*0
```

You can not just add padding and expect the CTS to still work because adding zeros progresses the rules of the cylic tag, we need to pad it while keeping the timing the same.
So you generate multiple different amount of paddings of zeros, and check if the state history matches up, if you do then it's a match and it's good to go!
However, do not be mislead. It is possible that two unreleated machines create the same state history, that is why we are only checking padded programs because they append the same things.
Do not try to check two unrelated machines and then say they are fuctionally equalivant, we can only say these are fuctionally equal because it is adding the same things onto the programs.

## Small proof it works
Given the ruleset
```plaintext
  ["1010", "1010"]
````
 It is possible to pad it with a padding of length 8.
<pre>
['<b>00000000</b>1010', '<b>00000000</b>1010']
</pre>

If we run it and check every single time the programs encounters a zero we can see the real program act as expected
<pre>
1010
0101010
010101010
</pre>
Now looking at the padded program we can see it is identical however it has paddings with length 8 in it's running, however they are fuctionally equalivant.
<pre>
<b>00000000</b>1010
010<b>00000000</b>1010
<b>00000000</b>01010<b>00000000</b>1010
</pre>



