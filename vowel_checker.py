user = input("Enter a word:")
vowel = "aeiou"
for i in vowel:
    if i in user:
        print("Your word contains a vowel")
        break
    else:
        print("Your word has no vowels")
        break
