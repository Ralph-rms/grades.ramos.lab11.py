words = []
for i in range (10):
    word = input (f"kindly enter 10 words.  Word {i+1}/10: ")
    words.append (word)
    
    num_letters = int(input("Enter the number of letters that you want: "))
    
    matching_words = []
    for word in words:
        if len(word) == num_letters:
            matching_words.append(word)
            
    if matching_words:
        print ("these are the words with", num_letters, "letters: ")
        for word in matching_words:
            print(word)
            
        else:
            print ("there are no words with", num_letters, "letters:")
                
            