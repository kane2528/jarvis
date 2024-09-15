import random

def get_joke():
    """Returns a random joke"""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you get when you cross a snowman and a vampire? Frostbite.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta.",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What does a nosey pepper do? Gets jalapeño business.",
        "Why can't you give Elsa a balloon? Because she will let it go.",
        "What do you call cheese that isn't yours? Nacho cheese.",
        "How does a penguin build its house? Igloos it together.",
        "What do you call a factory that makes good products? A satisfactory.",
        "Why did the math book look sad? Because it had too many problems.",
        "How does a scientist freshen her breath? With experi-mints."
    ]
    return random.choice(jokes)

def get_fun_fact():
    """Returns a random cricket-related fun fact"""
    cricket_facts = [
        "The longest Test match in cricket history lasted 12 days. It was played between South Africa and England in 1939.",
        "The term 'hat-trick' in cricket originated from a tradition where a bowler who took three consecutive wickets was awarded a hat by the crowd.",
        "Cricket was originally played in England as early as the 16th century, and it is believed to have been invented by children in the country.",
        "The fastest recorded ball in cricket was bowled by Shoaib Akhtar of Pakistan at 161.3 km/h (100.23 mph) during a match against England in 2003.",
        "The first-ever One Day International (ODI) match was played between Australia and England at the Melbourne Cricket Ground in 1971.",
        "The highest individual score in a One Day International is 264 runs by Rohit Sharma of India, achieved against Sri Lanka in 2014.",
        "Cricket is the second most popular sport in the world, after soccer, with an estimated 2.5 billion fans globally.",
        "The only player to have scored 100 international centuries is Sachin Tendulkar of India.",
        "A cricket ball is traditionally made of layers of leather, cork, and rubber, with the leather being dyed red or white depending on the format of the game.",
        "In cricket, the term 'duck' refers to a batsman getting out without scoring any runs.",
        "The most runs scored by a team in a single One Day International match is 498 runs, achieved by England against the Netherlands in 2022.",
        "The Ashes, one of the most famous cricket series, is contested between England and Australia and is named after a mock obituary published in a British newspaper after Australia's victory in 1882."
    ]
    return random.choice(cricket_facts)
