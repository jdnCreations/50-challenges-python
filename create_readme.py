import os
from tidy_hyperlinks import tidy_link
import requests

links = [
    "https://edabit.com/challenge/3DAkZHv2LZjgqWbvW",
    "https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt",
    "https://edabit.com/challenge/nfPNbisehCjuC8mkd",
    "https://edabit.com/challenge/AJGqpNL2yAyhbdpvB",
    "https://edabit.com/challenge/SHdu4GwBQehhDm4xT",

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
}

def add_challenges_to_readme():
    cwd = os.getcwd()
    file_name = "README.md"

    file = open(cwd + "\\" + file_name, 'a')

    for key, value in challenges.items():
        file.write(tidy_link(key, value))
        file.write('\n\n')

    print("Writing complete.")
    file.close()

add_challenges_to_readme()
