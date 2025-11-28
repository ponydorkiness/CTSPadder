This is used to find paddings of Cylic tag systems such that the cylic tag system still computes the same thing.

Example
["011011","011011"]
if you pad it with 6 cells
['000000'+'011011', '000000'+'011011']
or just ['000000011011', '000000011011']
it will be an equalivant CTS program.
This is used for rule 110 compilation because it requires programs to be lengths, multiples of 6.
