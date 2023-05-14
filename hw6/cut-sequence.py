# >NC_000019.10:c33299900-33299801 Homo sapiens chromosome 19, GRCh38.p14 Primary Assembly
seq = "AATCTCTGGGAAAACGGCATTAATAACACGAACAATCTGTGTTGGCCGGGGGAACCCAGGAGCCCCAGGCAGGGGTGGGGCTGTGAGGGGAGGGAAGCTG"
with open('cut-sequences.fasta', 'w') as file:
    for i in range(100, 0, -1):
        file.write('>fragment_' + str(i) + '\n')
        file.write(seq[:i] + '\n')
