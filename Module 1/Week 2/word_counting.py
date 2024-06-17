def word_counting(file_path):
    content = open(file_path, "r") # Read file from the path
    words = content.read().split() # Create a list of separated words
    count = dict() # Create a emply dictionary
    for word in words:
        if word.lower() not in count.keys():
            count[word.lower()] = 1
        else:
            count[word.lower()] += 1
    return count

file_path = "/Users/chaupham/Data_Science/AIO-2024/Module_1/Week_2/P1_data.txt"
print("word_count(file_path): \n", word_counting(file_path))