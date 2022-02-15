from os import system
import textwrap as tr

def genotype_entry(parent):
    while True:
        genotype = input(f"The {parent}'s genotypes: ")
        if genotype.isalpha() and len(genotype) == 2 and genotype[0].lower() == genotype[1].lower():
            if genotype[0].islower() and genotype[1].isupper():
                genotype = genotype[1] + genotype[0]
                # print("The dominant trait has been moved into the first position.")
                print(f"The {parent} is heterozygous")
            elif genotype[0].isupper() and genotype[1].islower():
                print(f"The {parent} is heterozygous")
            elif genotype[0].isupper():
                print(f"The {parent} is homozygous dominant")
            else:
                print(f"The {parent} is homozygous recessive")
            print()
            return genotype
        else:
            print("Must be only two letters long and use the same letter.")
            print()
            continue

def same_letters(a, b):
    b = list(b)
    for i in range(2):
        if b[i].lower() != a[0].lower():
            if b[i].islower():
                b[i] = a[i].lower()
            else:
                b[i] = a[i].upper()
    b = "".join(b)
    return b

def intro():
    system("clear")
    print("Welcome to the Mendelian Genetics Simulator")
    print()
    print("Copyright 2022, by Trevor McGarrah")
    print()
    print("Introduction: ")
    intro = """
    This simulator will help you learn about the genotype and phenotype of the potential offspring based on the genotype of the two parents.  Punnett Squares are useful for figuring out the chance the offspring of two parents will have a particular genotype and phenotype.
    """
    for line in tr.wrap(intro, width=60):
        print(line)

    print()
    print("Directions:")
    directions = """
    You can only test one trait at a time.  Each genotype is expressed as two characters of the same letter.  The two letters may be any combination of two lowercase, two uppercase, or one of each. (Examples: aa, AA, or Aa)  Don't mix and match different letters.  Use the same letter for both father and mother.  After entering the genotypes of the parents, you will see the Punnett Square for the pairing and the percent chance of each genotype and phenotype in the potential offspring.
    """
    for line in tr.wrap(directions, width=60):
        print(line)

    print()
    print("(Press Enter to Continue)")
    input()
    system("clear")

def core_loop():
    cont = True

    while cont:
        a = genotype_entry("father")
        b = genotype_entry("mother")

        b = same_letters(a, b)

        if b[0].isupper():
            one = b[0] + a[0]
            three = b[0] + a[1]
        else:
            one = a[0] + b[0]
            three = a[1] + b[0]

        if b[1].isupper():
            two = b[1] + a[0]
            four = b[1] + a[1]
        else:
            two = a[0] + b[1]
            four = a[1] + b[1]

        genotype_list = [one, two, three, four]
        het = a[0].upper() + a[0].lower()
        hd = a[0].upper() + a[0].upper()
        hr = a[0].lower() + a[0].lower()
        het_percent = round(genotype_list.count(het) / 4 * 100, 0)
        hd_percent = round(genotype_list.count(hd) / 4 * 100, 0)
        hr_percent = round(genotype_list.count(hr) / 4 * 100, 0)

        print("(Press Enter to Continue)")
        input()
        system("clear")

        print("Genotypes of the Parents:")
        print("Father: " + a + "\t" + "Mother: " + b)
        print()
        print("Punnett Square:")
        print("The father's genotype for the trait is on the left.")
        print("The mother's genotype for the trait is across the top.")
        print()
        print("    " + b[0] + "  | " + b[1])
        print(a[0] + " | " + one + " | " + two)
        print(a[1] + " | " + three + " | " + four)
        print()
        print("% Chance of Offspring Being:")
        print("Heterozygous: " + str(het_percent))
        print("Homozygous dominant: " + str(hd_percent))
        print("Homozygous recessive: " + str(hr_percent))
        print()
        print("% Chance of Offspring Expressing:")
        print("Dominant trait: " + str(hd_percent + het_percent))
        print("Recessive trait: " + str(hr_percent))

        while True:
            print()
            cont = input("Would you like to try again? (y/n) ")
            print()
            if cont == "y" or cont == "yes":
                cont = True
                system("clear")
                break
            elif cont == "n" or cont == "no":
                cont = False
                system("clear")
                break
            else:
                continue

def outro():
    print()
    print("""Mendelian genetics is amazing!

Thanks for playing the Mendelian Genetics Simulator!

Programmed by Trevor McGarrah""")