def stutterify(word):
    first_two_letters = word[:2]
    print(first_two_letters + "... " + first_two_letters + "... " + word + "?")


stutterify("incredible")
