"""4th of July Time Complexity!
A city is putting on a fireworks show for the 4th of July. There are `n` types of fireworks, and for each type, there's a specific amount of time it takes to launch that firework.

The city wants to put on a show that lasts for `m` minutes.The function `create_show` takes a list of fireworks (each represented as an integer indicating the time in minutes it takes to launch) and a total time for the show `m`.

The function will return a list of fireworks that will fill the show's time as evenly as possible.
"""

import random

def create_show(fireworks, show_time):   #time O(nlogn)  #space O(n)
    fireworks.sort()     #time O(nlogn)  #space O(0)
    show = []    #time O(1)  #space O(1)
    remaining_time = show_time    #time O(1)  #space O(1)

    while remaining_time > 0 and fireworks:   #time O(1)  #space O(0)
        # Select a random firework
        firework = random.choice(fireworks)   #time O(logn)  #space O(1)

        if firework <= remaining_time:   #time O(1)  #space O(0)
            # Add the firework to the show
            show.append(firework)     #time O(n)  #space O(1)
            remaining_time -= firework    #time O(1)  #space O(0)

        else:
            # This firework is too long, remove it from consideration
            fireworks.remove(firework)    #time O(n)  #space O(0)
    return show       #time O(1)  #space O(1)