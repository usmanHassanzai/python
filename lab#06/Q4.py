alphabate = input("Enter the alphabate to check wether it is consonant or vowel : ")

if(alphabate.lower() in ['a' , 'e' , 'i' , 'o' , 'u'] or alphabate.upper in ['A' , 'E' , 'I' , 'O' , 'U']):
    print(f"The given alphabate is vowel : {alphabate}")
else:
    print(f"The given alphabate is  consonant : {alphabate}")