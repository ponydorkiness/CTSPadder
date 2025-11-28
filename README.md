# Padding Cyclic Tag Systems (CTS)

Cyclic Tag Systems sometimes require **padding** to ensure they compute the same function while meeting specific constraints. 
For example, in **Rule 110 compilation**, CTS programs must have lengths that are multiples of 6.

## How it works

Given a CTS program:

```
["011011", "011011"]
```

You can pad it with 6 cells:

```
["000000011011", "000000011011"]
```

or equivalently:

```
['000000' + '011011', '000000' + '011011']
```

Both versions are **functionally equivalent**; the padding does not change the computation, it only adjusts the program length.
This technique is essential when preparing CTS programs for **Rule 110 compilation**, ensuring all rules have lengths divisible by 6.
