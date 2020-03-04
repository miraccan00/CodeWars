"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of
cells and carries the "instructions" for the development and functionin
of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)"""


def DNA_strand(dna):
    if "A" in dna or "T" in dna:
        dna = dna.replace("A", "Q").replace("T", "A").replace("Q", "T")

    if "G" in dna or "C" in dna:
        dna = dna.replace("G", "W").replace("C", "G").replace("W", "C")
    return dna


print(DNA_strand("TTTGC"))
