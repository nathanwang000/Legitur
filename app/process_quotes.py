f = open("quotes.txt")
quotes = []
def process_quotes(f):
    quote = ""
    author = None
    for l in f:
        if l == "\n":
            quotes.append((quote.replace("\n", " "), 
                           author or "Anonymous"))
            quote = ""
            author = None
        elif l.find("--") != -1:
            author = l.split("--")[-1].strip()
        else:
            quote += l

process_quotes(f)


