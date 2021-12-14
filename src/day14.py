
from typing import Counter, Tuple,List
from itertools import tee

# stolen from itertools.pairwise as i couldn't import it
def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def process_polymer_rules(polymer_template:List[str], pair_insertion_rules:List[Tuple[Tuple[str,str],str]]) -> List[str]:
    count = 0
    polymer_template_copy = polymer_template[:]
    polymer_template_pairs = pairwise(polymer_template_copy)
    for i, pair in enumerate(polymer_template_pairs):
        for rule in pair_insertion_rules:
            if rule[0] == pair:
                polymer_template[(i+1)+count:i+1+count] = rule[1]
                count+=1
                break
    return polymer_template

if __name__ == "__main__":
    input = open("./src/day14_input.txt", "r").readlines()
    polymer_template = list(input[0].rstrip())
    pair_insertion_rules = [(tuple(list(x.split(" -> ")[0])),x.rstrip().split(" -> ")[1]) for x in input[2:]]
    
    for step in range(10):
        polymer_template = process_polymer_rules(polymer_template,pair_insertion_rules)
        print(f"step: {step}, polymer length: {len(polymer_template)}")
    c = Counter(polymer_template)
    print(c.most_common(1)[0][1] - c.most_common()[-1][1])