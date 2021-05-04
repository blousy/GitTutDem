import collections
from structures import *

Nucleotides = ["A","C","T","G"]


def Nuc_Val(DNA_seq):
    u_Nuc = DNA_seq.upper()
    for i in u_Nuc:
        if i not in Nucleotides:
            return False    
    return u_Nuc

# print(Nuc_Val("ctx"))

def Nuc_Freq(seq):
    # return dict(collections.Counter(seq))
    TmpFreqDict = {'A': 0, 'C': 0, 'T' : 0, 'G' : 0}
    for i in seq:
        TmpFreqDict[i] += 1
    return TmpFreqDict
      

def RNA_Nuc_Freq(seq):
    # return dict(collections.Counter(seq))
    TmpFreqDict_RNA = {'A': 0, 'C': 0, 'U' : 0, 'G' : 0}
    for i in seq:
        TmpFreqDict_RNA[i] += 1
    return TmpFreqDict_RNA      


def Transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine with Uracil"""
    return seq.replace("T", "U")


def Reverse_Complement(seq):
    """ Swapping Adenine with Thymine and Guanine with Cytocine. Reversing newly generated string"""
    # return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
    mapping = str.maketrans('ATCG', 'TACG')
    return seq.translate(mapping)[::-1]


def gc_content(seq):
    """GC content in DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


def gc_content_subsec(seq, k = 20):
    """ GC Content in  a DNA/RNA sub-sequence length k, k=20 by default"""
    res = []
    for i in range(0, len(seq) - k, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res

