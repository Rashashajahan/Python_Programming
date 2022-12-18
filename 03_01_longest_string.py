# Which of the following strings is the longest?
# Use the len() function to find out.
# You can run `len(my_variable)` and it will return the len of the variable (in this case it's a string)


longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"
if(len(longest_german_word)>len(longest_hungarian_word)):
    if(len(longest_german_word)>len(longest_finnish_word)):
        if(len(longest_german_word)>len(strong_password)):
            print(f"{longest_german_word} is longest.\n")
        else:
            print(f"{strong_password} is longest.\n")
    elif(len(longest_finnish_word)>len(strong_password)):
        print(f"{longest_finnish_word} is longest.\n")
    else:
        print(f"{strong_password} is longest.\n")
else:
    print(f"{longest_hungarian_word} is longest.\n")
