"""
This program is authored by Jie HAN.
It is designed for clinical practitioners to evaluate the Huntington's disease status for patients according to their DNA sequence.

"""


def get_input():
    """
    Collect user input about a patient's first name, last name and DNA sequences.
    Return the tuple of (first_name, last_name, DNA).
    """
    f_name = raw_input("Please enter first Name: ")
    l_name = raw_input("Please enter last Name: ")  
    DNA = raw_input("Please enter DNA: ")
    return  f_name,l_name,DNA


def countCAG(dna):
    """
    Count the number of occurence of the substring "CAG" in the input string "dna".
    Return the counts as an integer.
    Precondition:
    dna is a string that can not be empty.
    >>> countCAG("CADAGACCTAC")
    0
    >>> countCAG("CAGCATCAGCAGCAGCAGACGCAGGGCCACAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAACC")
    27
    >>> countCAG("ACCCAGCAGCAGCAGCACAGCAGAGCAGCAGCAGCAGACAGCAGCAGGCAGCAGCAGCAGCAGCAGTCAGTCAGCAGCAGCAGCAGCCAGCAGCAGA")
    28
    >>> countCAG("CAGACCAGCAGAGGCAGCAGCAGCACAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGACGCAGCAGCAGCAGCAGCAGCAGGACCAGCAGCAGCAGCAGCAGCAA")
    32
    >>> countCAG("ACCAGCAGCAGCAGCACAGCAGCAGGCCAGCAGCAGCAGCAGGTCAGCAGCAGCAGCAGCAGCAGACGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCCACAGCAGCAGCAGCAGCAGCACAG")
    36
    >>> countCAG("ACCAGCAGTGCAGCAGCAGCAGCAGCAGCAGCAGCCCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGGTCAGCAGCAGCAGCAGCAGCAGACCAGCAGCA")
    37
    >>> countCAG("AGCCAGCAGCAGGGCCAGCAGCAGACACAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGACGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGGGCCAGCAGCAGCAGCAGCAG")
    39
    >>> countCAG("TCAGCACAGCAGGCCAGCAGCAGCAGAGCAGCAGACCAGCAGCAGCAGCAGCAGCAGATCAGCAGCAGCAGCAGGGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAG")
    42
    >>> countCAG("ACCAGCAGCAGCACAGCAGCAGCAGTGCAGCAGCAGCAGCAGCCCAGCAGCAGCAGCAGCAGAACAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGACG")
    43
    >>> countCAG("ACGCAGCAGGCAGCAGCAGCAGCAGCAGTGCAGCAGCAGCAGCACAGCAGCAGCAGCAGCAGCAGCAGCAGCAGGCAGCAGCAGCAGACAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGACG")
    49
    """
    ind = 0
    count = 0
    while ind <= len(dna)-3:
        ch = dna[ind:(ind+3)]
        if ch == "CAG":
            count += 1
            ind += 3   
        else:
            ind += 1
    return count


def prediction(numCAG):
    """
    Return the evaluation of the classification and disease status for the patient.
    Precondition:
    numCAG: positvie integer or 0.
    >>> prediction(27)
    ('Normal', 'Unaffected')
    >>> prediction(28)
    ('Intermediate', 'Unaffected')
    >>> prediction(35)
    ('Intermediate', 'Unaffected')
    >>> prediction(36)
    ('Intermediate', 'Unaffected')
    >>> prediction(37)
    ('Reduced Penetrance', 'Somewhat Affected')
    >>> prediction(40)
    ('Reduced Penetrance', 'Somewhat Affected')
    >>> prediction(42)
    ('Reduced Penetrance', 'Somewhat Affected')
    >>> prediction(43)
    ('Full Penetrance', 'Affected')
    >>> prediction(45)
    ('Full Penetrance', 'Affected')
    """
    
    if numCAG <28:
        cla = "Normal"
        Ds = "Unaffected"
    elif numCAG <= 36:
        cla = "Intermediate"
        Ds = "Unaffected"
    elif numCAG <= 42:
        cla = "Reduced Penetrance"
        Ds = "Somewhat Affected"
    else:
        cla = "Full Penetrance"
        Ds = "Affected"
    return cla, Ds

def main():
    first_name, last_name, DNA = get_input()
    print first_name, last_name
    print "Sequence of DNA:", DNA
    repeat_count = countCAG(DNA)
    Clas, D_sta = prediction(repeat_count)
    print "Repeat Count:", repeat_count
    print "Classification:", Clas
    print "Disease Status:", D_sta


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()
