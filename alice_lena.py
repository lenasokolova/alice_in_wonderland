filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, but ", filename, "doesn't exist."
    print(msg)
else:
    """Counting the approximately amount of the words in the file."""
    words = contents.split()
    num_words = len(words)
    print("File ", filename, " contains", str(num_words), " words.")