from DNA_toolkit import *
import random
from utilities import colored

# Random_DNA = "aActgAGGTG"
Random_Num = random.randint(1, 50)
Random_DNA2 = ''.join([random.choice(Nucleotides)
               for i in range(Random_Num)])


# Nuc_Val(Random_DNA)
a = Nuc_Val(Random_DNA2) 
print(colored(a) + "\n")  
c = Nuc_Freq(a)
print(colored(f"{c}"))
d = Transcription(a)
e = RNA_Nuc_Freq(d)
print(colored(f"{e}"))
l = len(a)
r = Reverse_Complement(a)
print(colored(r))
g = gc_content(a)
g_s = gc_content_subsec(a, k = 5)

#Conversion of dictionary to string to insert in the database as .txt
a = str(a)
c = str(c)
d = str(d)
e = str(e)
l = str(l)
r = str(r)
g = str(g)
g_s = str(g_s)

#writes in a seperate text file
with open("DNA_codes.txt", "a") as f: 
    f.write(f"[1] + length of DNA : {l}" + "\n\n" + f"[2] + DNA  Sequence : {a}" + "\n" + f"[3] + Nucleutides Frequency : {c}" + "\n\n" + f"[4] + DNA/RNA Transcription : {d}" + "\n" + f"[5] + DNA/RNA Transcription Frequency : {e}"  + "\n" + f"[6] + Reverse Complement of DNA is {r} " + "\n" + f"[7] + GC Content {g}%" + "\n" + f"[8] + GC content subset : {g_s} " + "\n\n" + "-----------------------------------------------" + "\n\n")

with open("full_DNA.txt", "a") as f2:
    f2.write(f"\n DNA string + Reverse Complement :\n3' {a} 5'")
    f2.write("  ")
    f2.write(f"\n {'  '+''.join(['|' for c in range(len(a))])}")
    f2.write(f"\n5' {r} 3'\n")
     