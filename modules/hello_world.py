#!/usr/bin/env python
import random

def helloworld(phenny, input):
    phenny.say("Hello world!")
helloworld.commands = ['hello']
helloworld.priority = 'medium'
#print "hello, world!!!"

def dance(phenny, input):
    phenny.say("O-/-<")
    phenny.say("O-|-<")
    phenny.say("O-\-<")
    phenny.say("O-|-<")
    phenny.say("O-/-<")        
dance.commands = ['doadance']
dance.priority = 'medium'

def interjection(phenny, input):
    phenny.say(input.nick + '!')
interjection.rule = r'$nickname!'
interjection.priority = 'high'
interjection.thread = False

def message_join(phenny, input):
    phenny.say("welcome, %s!" % input.nick)
message_join.event = 'JOIN'
message_join.rule = r'.*'

quotes = {}

def learn_quote(phenny,input):
    words = input.split(" ")
    user = words[1]
    quote = " ".join(words[2:])
    if not user in quotes:
        quotes[user] = [quote]
    else:
        quotes[user].append(quote)
    phenny.say("got it.")
learn_quote.commands = ['learnquote']
learn_quote.priority = 'medium'

def quote(phenny, input):
    words = input.split(" ")
    user = words[1]
    if user in quotes:
        quote = random.choice(quotes[user])
        phenny.say("%s once said: %s" % (user,quote))
    else:
        phenny.say("I don't have any intel on %s" % user)
quote.commands = ['quote']
quote.priority = 'medium'

def advisor(phenny, input):
    responses = ["Have you tried rerunning your gel?",
                 "Start writing!",
                 "Try it again",
                 "Maybe you should work more nights and weekends"]
    phenny.say(random.choice(responses))
advisor_triggers = [r"understand",
                    r"science",
                    r"difficult",
                    r"hard",
                    r"stuck"]
advisor.rule = r"|".join([r".*" + trigger + r".*" for trigger in advisor_triggers])
advisor.priority = 'medium'

with open("/home/poneill/.phenny/idioms.txt") as f:
    lines = f.readlines()
    english_idioms = [line.strip() for (i,line) in enumerate(lines) if i % 4 == 0]
    spanish_idioms = [line.strip() for (i,line) in enumerate(lines) if i % 4 == 1]
    literal_idioms = [line.strip() for (i,line) in enumerate(lines) if i % 4 == 2]

def idiom(phenny, input):
    words = input.split(" ")
    hits = [idiom for idiom in english_idioms for word in words if word in idiom]
    if hits:
        english_idiom = random.choice(hits)
        index = english_idioms.index(english_idiom)
        spanish_idiom = spanish_idioms[index]
        literal_idiom = literal_idioms[index]
        triggers = [word for word in words if word in english_idiom]
        phenny.say("it's funny that you mention: %s." % random.choice(triggers))
        phenny.say("In %s, we say:" % random.choice(["Spain","Spanish"]))
        phenny.say(spanish_idiom)
        phenny.say("it means:")
        phenny.say(literal_idiom)
idiom.rule = r'.*'
idiom.priority = 'medium'

