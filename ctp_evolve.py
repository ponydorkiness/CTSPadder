import itertools
from collections import deque
import time

def string_chunks(string, x):
    new = ''
    cnt = 0
    for ch in string:
        if cnt%x==0 and cnt!=0:
            new += ''
        cnt += 1
        new += ch
    return new

def compare_strings(a, b):
    return a.startswith(b) or b.startswith(a)

def run(rules, gens):
    tape = deque("1")
    state = 0
    output = []
    num_rules = len(rules)
    count = 0
    
    while count < gens and tape:
        while tape and tape[0] == "0":
            tape.popleft()
            state = (state + 1) % num_rules

        if not tape:
            break
        
        tape.popleft()
        
        output.append(str(state))
        output.append("*")
        
        tape.extend(rules[state])
        
        state = (state + 1) % num_rules
        count += 1
    
    return "".join(output)

def compare_rules(rules1,rules2,gens=10,debug=False):
    if debug == True:
        print(run(rules1,gens))
        print(run(rules2,gens))
    return compare_strings(run(rules1,gens),run(rules2,gens))

def pad(padding, array):
    new_array = array.copy()
    for x in range(len(padding)):
        new_array[x] = (padding[x]*"0") + new_array[x]
    return new_array

def main():
    rules = ["1010","1010"]
    min_padding = 1
    max_padding = 20
    length = len(rules)

    for row in itertools.product(range(min_padding,max_padding+1), repeat=length):
        padded_rules = pad(row, rules)
        lengths = [len(s) for s in padded_rules]
        if all(l % 6 == 0 for l in lengths): # This checks for divisblity of six, you can change it or remove it if you don't care about divisbility.
            if compare_rules(padded_rules, rules, 2): 
                #print(padded_rules)
                print(lengths, row)  # row shows the integer padding us

main()
#print(run(["1","00000000000000000000000000000000000000101"],10))
