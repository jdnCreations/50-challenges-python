import os
from tidy_hyperlinks import tidy_link

titles = [
    "# 50 Challenges/Exercise in Python",
    "## Completing 50 challenges/exercises in python for practice :)",
    "### Links to all Challenges so far"
]

challenges = {
    "Tidy Hyperlinks": "https://edabit.com/challenge/nfPNbisehCjuC8mkd",
    "Virtual DAC": "https://edabit.com/challenge/AJGqpNL2yAyhbdpvB",
    "Stuttering Function": "https://edabit.com/challenge/gt9LLufDCMHKMioh2",
    "Luke, I Am Your ...": "https://edabit.com/challenge/8pDH2SRutPoaQghgc",
    "Invert Colors": "https://edabit.com/challenge/i6hY9JSjQK4jcaB6i",
    "Calculating Damage": "https://edabit.com/challenge/HSHHkdRYXfgfZSqri",
    "Finding Adjacent Nodes": "https://edabit.com/challenge/3DAkZHv2LZjgqWbvW",
    "Length of Number": "https://edabit.com/challenge/2zKetgAJp4WRFXiDT",
    "Burglary Series (03): Is It Gone?": "https://edabit.com/challenge/2wQPKcSipXmK4idwD",
    "Calculate the Profit": "https://edabit.com/challenge/YfoKQWNeYETb9PYpw",
    "Return the Time Saved by Speeding": "https://edabit.com/challenge/QgSMSMpfcEebAyCye",
    "Sum of Resistance in Series Circuits": "https://edabit.com/challenge/gzmFeaXwFv8X6pBGq",
    "Basic Calculator": "https://edabit.com/challenge/ZdnwC3PsXPQTdTiKf",
    "Find Domain Name From DNS Pointer (PTR) Records Using IP Address": "https://edabit.com/challenge/MtktG9Dz7z9vBCFYM",
    "Flipping Bits": "https://edabit.com/challenge/z39yXccJGLAy3BDNX",
    "The Snake — Area Filling": "https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt",
    "Basic Arithmetic Operations on a String Number": "https://edabit.com/challenge/peezjw73G8BBGfHdW",
    "The Karaca's Encryption Algorithm": "https://edabit.com/challenge/JzBLDzrcGCzDjkk5n",
    "Pluralize!": "https://edabit.com/challenge/LR98GCwLGYPSv8Afb",
    "Remove The Word!": "https://edabit.com/challenge/gH3QMvF3czMDjENkk",
    "Convert to Hex": "https://edabit.com/challenge/g6yjSfTpDkX2STnSX",
    "Paint the Walls": "https://edabit.com/challenge/W8imhL66osEpK2ANs",
    "C*ns*r*d Str*ngs": "https://edabit.com/challenge/ehyZvt6AJF4rKFfXT",
    "Sales by Match": "https://edabit.com/challenge/oq2FxAx5bJZgPLk9r",
    # "The Magic Square Game": "https://edabit.com/challenge/shf4iTJTbQ7sethFA",
    "Count and Identify Data Types": "https://edabit.com/challenge/HXkpnCxJgxkFwaReT",
    "Sharing is Caring": "https://edabit.com/challenge/pqpkRBP4YT5dwBDHm",

}

def add_challenges_to_readme():
    cwd = os.getcwd()
    file_name = "README.md"

    file = open(cwd + "\\" + file_name, 'w')

    for item in titles:
        file.write(item)
        file.write('\n\n')

    file.write(tidy_link("10 Python Challenges - CodeAcademy", "https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/"))
    file.write('\n\n')

    for key, value in challenges.items():
        file.write(tidy_link(key, value))
        file.write('\n\n')

    print("Writing complete.")
    file.close()

add_challenges_to_readme()
