
def count_word(filename):
    '''
    count the word number in a file
    '''
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print("sorrry, file {} not found".format(filename))
    else:
        words = contents.split()
        print("there are {} words in file {}.".format(len(words), filename))


filename = "test_count.txt"
count_word(filename)
