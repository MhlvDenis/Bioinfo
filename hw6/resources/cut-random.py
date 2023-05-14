import random

with open('genome.fasta') as fin:
    lines = fin.read().split('\n')

genome = ""
for i in range(1, len(lines)):
    genome += lines[i]

sequences = []

for i in range(100):
    start = random.randint(0, len(genome) - 100)
    sequences.append(genome[start:(start + 100)])

with open('random-sequences.fasta', 'w') as fout:
    for i in range(len(sequences)):
        fout.write(f'>Fragment {i + 1}\n{sequences[i]}\n')
