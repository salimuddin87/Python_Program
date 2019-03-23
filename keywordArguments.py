
def cheeseshop(kind, *arguments, **keywords):
    print "--Do you have any", kind, "?"
    print "--I am sorry, we are all out of", kind
    print "*" * 50

    for arg in arguments:
        print arg
        print "#" * 50

    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]

    print "Data type of arguments :", type(arguments)
    print "Data type of keywords :", type(keywords)

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

