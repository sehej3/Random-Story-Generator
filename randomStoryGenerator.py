import random

when = ["a few years ago", "once upon a time", "last night", "a long time ago", "yesterday"]
who = [" rabbit", "squirrel", "turtle", "dog", "cat"]
name = ["Ali", "Stan", "Tanisha", "Sehej", "Ram"]
where = ["India", "Germany", "Italy", "Romania"]
went = ["school", "seminar", "class", "laundry", "restraunt"]
happened = ["made new friends", "wrote a book", "had dinner", "did chores"]

print(random.choice(when)+ " , " + random.choice(who) + " named " + random.choice(name) + " lived in " + random.choice(where) + " went to a " +random.choice(went) + " and " + random.choice(happened) )

