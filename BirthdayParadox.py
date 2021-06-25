
import random

def trialRunner(n, k):
	"""
	Runs k trials with n people each
	Returns 
	"""

	#initialize counter variables
	trials_with_match_counter = 0
	master_match_counter = 0

	#run k trials
	for i in range(k):

		#create n 'people'
		people = []
		for j in range(n):
			people.append(birthdayGenerator())

		#compare all members of people to find matches
		match_counter = matchFinder(people)

		#if a match is found, increment trials_with_match and add total matches to master_match
		if match_counter > 0:
			trials_with_match_counter += 1
			master_match_counter += match_counter

	#caclulate results
	success_rate = trials_with_match_counter / k
	expected_matches = master_match_counter / k

	return (success_rate, expected_matches, trials_with_match_counter)

def birthdayGenerator():
	"""
	Returns a random birthday as an integer day number
	"""

	return random.randint(1, 365)


def matchFinder(people):
	"""
	Takes in a list of birthdays as integer day numbers
	Returns the number of matches
	"""

	#initialize counter variable
	counter = 0

	#compare all pairs and increment counter if a pair is found
	for i in range(len(people)):
		for j in range(len(people)):
			if (people[i] == people[j]) & (i != j):
				counter += 1

	return counter

def simpleOutputer(results, n, k):
	print("\nResults: ")
	print(str(results[2]) + " trials with matches in " + str(k) + " trials.")
	print(str(results[0]) + "% probability of at least one match with " + str(n) + " people.")
	print("Expected number of matches per trial: " + str(results[1]) + ".")


def chartBuilder(n_lower, n_upper, k, step):
	

	expected_matches_list = []
	probability_list = []
	n_list = []

	for n in range(n_lower, n_upper, step):
		results = trialRunner(n, k)
		expected_matches_list.append(results[1])
		probability_list.append(results[0])
		n_list.append(n)

	#scale lists and zip with original lists
	expected_matches_scaled = [i / max(expected_matches_list)  for i in expected_matches_list]
	probability_scaled = [i / max(probability_list)  for i in probability_list]
	
	expected_matches_zipped = zip(n_list, expected_matches_list, expected_matches_scaled)
	probability_zipped = zip(n_list, probability_list, probability_scaled)

	#build first chart
	print("\nExpected Number of Matches:\n")
	for (n, unscaled, scaled) in expected_matches_zipped:
		print("{:>3}|".format(n) + ('X' * int(scaled * 100)) + " " + str(unscaled))

	#build second char
	print("\nProbability of Getting as Least One Match:\n")
	for (n, unscaled, scaled) in probability_zipped:
		print("{:>3}|".format(n) + ('X' * int(scaled * 100)) + " " + str(unscaled))


		



def main(args):
	k = int(args[1])
	n = int(args[2])


	if len(args) == 3:
		results = trialRunner (n, k)
		simpleOutputer(results, n, k)

	if len(args) >= 4:
		n_lower = n
		n_upper = int(args[3])
		if len(args) == 5:
			step = int(args[4])
		else:
			step = 1	
		chartBuilder(n_lower, n_upper, k, step)

		




if __name__ == '__main__':
    import sys
    main(sys.argv)