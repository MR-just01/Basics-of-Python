def inverted_bib(data):
    inverted  = {}
    for author, books  in data.items():
        for book in books:
            inverted[book] = author
    return inverted

authors = {
    "orwell " : ["1984" , "Animal Farm"],
    "Huxley " : ["Brave New World "]
}


print(inverted_bib(authors))