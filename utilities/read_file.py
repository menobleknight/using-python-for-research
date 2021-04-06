def read_file(file_path):
    """
    Reads a file on github.com at given file_path and return contents of a file in form of str. 
    """
    import urllib.request, urllib.parse
    
    # if there are non-ascii characters in file_path
    file_path = urllib.parse.quote(file_path, safe="/:") # don't encode '/' and ':'

    with urllib.request.urlopen(file_path) as f:
        text = f.read().decode('utf-8') # read() returns data as bytes, decode data to str using 'utf-8'

    return text

# file with single line

file_path = "https://raw.githubusercontent.com/menobleknight/using-python-for-research/main/week-3-part-1/dna-translation/protein.txt"
print(read_file(file_path))

# file with multiple lines

file_path = "https://raw.githubusercontent.com/menobleknight/using-python-for-research/main/week-3-part-2/books/english/shakespeare/A-Midsummer-Night's-Dream.txt"
print(read_file(file_path))
