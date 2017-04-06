import math
import numpy as np
import random

class REINFORCE_Agent():
	def __init__(self, env, GAMMA = 0.9, STEP_SIZE = 0.01, MAX_EPISODE_LENGTH = 100, DO_PLANNING = False):
		if env == None:
			sys.exit('Environment not passed in the agent. Program is terminating')

		self.env = env
		self.GAMMA = GAMMA
		self.STEP_SIZE = STEP_SIZE
		self.MAX_EPISODE_LENGTH = MAX_EPISODE_LENGTH

		self.weights = ((2 * np.random.ranf([( 4 * 4 ) + 1])) - 1)/2.0

	def generateEpisode(self):
		current_state = self.env.START_STATE
		episode = []
		while ((len(episode) < self.MAX_EPISODE_LENGTH) or not(current_state == self.env.END_STATE)):
			softmax_probabilities = self.getSoftmaxProbabilities(current_state)
			action_taken = self.pickAction(softmax_probabilities)
			
			
	def getSoftmaxProbabilities(self, current_state):
		softmax_probabilities = []
		for action in self.env.action_space:
			feature_vector = self.getFeatureVector(current_state, action)
			softmax_probabilities.append(math.exp(np.dot(feature_vector, self.weights)))

		softmax_probabilities = self.softmax(softmax_probabilities)
		return softmax_probabilities

	def softmax(self, x):
		return np.exp(x) / np.sum(np.exp(x), axis=0)

	def pickAction(self, softmax_probabilities):
		random_throw = random.uniform(0, 1)
		for iterator in range(len(softmax_probabilities)):
			if random_throw < np.sum(softmax_probabilities[0 : (iterator + 1)]:
				break
		return self.env.action_space[iterator]