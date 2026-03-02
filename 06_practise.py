# display a joke of the day

import random
joke = {
    "why did the chicken cross the road?" : "to get to the other side",
    "Why did the tomato turn red?" : "It was too hot",
    "Why did the cow go to the party?" : "It wanted to be milked"
}

setup = random.choice(list(joke.keys()))
print(f"Joke of the day : {setup}")
input("Press enter to see the answer")
print(f"Answer :{joke[setup]}")