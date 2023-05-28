relations = {
    "Darth Vader": "father",
    "Leia": "sister",
    "Han": "brother in law",
    "R2D2": "droid"
}


def relation_to_luke(person):
    return "Luke, I am your " + relations[person] + "."


print(relation_to_luke("Darth Vader"))
print(relation_to_luke("Leia"))
print(relation_to_luke("Han"))
print(relation_to_luke("R2D2"))
