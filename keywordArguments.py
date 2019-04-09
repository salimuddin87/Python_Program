"""
--Do you have any Limburger ?
--I am sorry, we are all out of Limburger
**************************************************
It's very runny, sir.
##################################################
It's really very, VERY runny, sir.
##################################################
client : John Cleese
shopkeeper : Michael Palin
sketch : Cheese Shop Sketch
Data type of arguments : <type 'tuple'>
Data type of keywords : <type 'dict'>

"""

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

    print "*" * 50
    print "Data type of arguments :", type(arguments)
    print "Data type of keywords :", type(keywords)

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

