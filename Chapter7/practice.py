#Hard Question

def count_vowels_consonents(userword):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in userword:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)

#User Input
userword = input("Enter Any Word")
count_vowels_consonents(userword)



#Let's Practice Again


def count_vowel_consonent(userinput):
    vowel = "aeiouAEIOU"

    vowel_count = 0
    consonent_count = 0

    for char in userinput:
        if char.isalpha():
            if char in vowel:
                vowel_count += 1
            else:
                consonent_count += 1



