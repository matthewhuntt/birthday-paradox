# birthday-paradox
A simple script to simulate the Birthday Paradox and demonstrate the effects of changing parameters


## Background

On the first day in my introductory probability and statistics course, my professor asked the class to estimate the probability that, if we compared the birthdays of every student present, we would find at least one match. It was a class of around 60 students, so most of us guessed somewhere in the 20-50% range. The professor proceeded to ask for every single student's birthday - and we found not one match, but several. He then asked a follow-up question: "how many students would have to be in the class in order to give us a 50% chance of finding a match?" 

Many people will recognize this as the "Birthday Paradox", which preys on our inability to accurately assess the way that combinations scale. When asked the second question above, it is not uncommon to receive an answer of around 180 - after all, there are around 360 days in a year, and if we have 180, that should give us a 50% shot at a match. Of course, this reasoning disregards that we should be counting pairs, not individuals. In our group of 60 students, there were 3,540 pairs, giving us a probability of over 99% of finding at least one match. To add insult to injury, our professor told us that the magic number - the number of people needed such that the chance of finding a match is at least 50% - is only _23_. It shocked a bunch of industrial enginerring students, and it shocks most others as well.

## Methodology

For each trial:
1. Generate a list of "people" of length n, each with a randomly selected birthday
2. Compare each person's birthday to each other person's
3. Count the number of matches

## Reasoning

This program was created in order to show people this unintitive truth and to help friends and family wrap their heads around combinations, as well as basic simulation. There are certainly no shortage of closed form solutions and approximations to show the probabilities for any choice of n, but I find the simulation provides an intuitive approach that is easy for newcomers to interpret - instead of getting into combinations, just fill a room with people and see how many matches we find.

## Usage

