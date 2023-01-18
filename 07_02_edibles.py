# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
food1=s[5:9]+s[11]
food2=s[7:12]
food3=s[-10:-4]
food4=s[-21:-14]
food5=s[-9]+s[-4:-1]
food6=s[26:29]
print(food1, food2, food3, food4, food5, food6)
