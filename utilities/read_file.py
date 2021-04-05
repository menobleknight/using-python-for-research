def read_file(file_path):
    """
    Reads a file on github.com at given file_path and return contents of a file in form of str. 
    """
    import urllib, bs4
    text = []
    
    # if there are non-ascii characters in file_path
    file_path = urllib.parse.quote(file_path, safe="/:") # don't encode '/' and ':'

    with urllib.request.urlopen(file_path) as f:
        for line in bs4.BeautifulSoup(f)('td'):
            if len(line) > 0:
                text.append(line.contents[0].strip())

    text = ' '.join(text)
    return text
