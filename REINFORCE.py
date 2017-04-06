import math
import numpy as np
import random

class REINFORCE_Agent():
	def __init__(self, env, GAMMA = 0.9, STEP_SIZE = 0.001, MAX_EPISODE_LENGTH = 300, DO_PLANNING = False):
		if env == None:
			sys.exit('Environment not passed in the agent. Program is terminating')

		self.env = env
		self.GAMMA = GAMMA
		self.STEP_SIZE = STEP_SIZE
		self.MAX_EPISODE_LENGTH = MAX_EPISODE_LENGTH

		self.weights = ((2 * np.random.ranf([( 2 * 4 ) + 1])) - 1)/2.0

	def generateEpisode(self):
		current_state = self.env.START_STATE
		episode = []
		while ((len(episode) < self.MAX_EPISODE_LENGTH) and not(current_state == self.env.END_STATE)):
			softmax_probabilities = self.getSoftmaxProbabilities(current_state)
			action_taken = self.pickAction(softmax_probabilities)
			next_state = self.env.transition_dynamics[current_state][action_taken]
			reward = self.env.immediate_reward_dynamics[current_state][action_taken]
			episode_step = (current_state, action_taken, reward)
			episode.append(episode_step)
			current_state = next_state

		if not len(episode) == self.MAX_EPISODE_LENGTH:
			episode.append((self.END_STATE, self.env.action_space[0], 0))

		return episode
			
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
			if random_throw < np.sum(softmax_probabilities[0 : (iterator + 1)]):
				break
		return self.env.action_space[iterator]

	def getFeatureVector(self, state, action):
		feature_vector = [1.0]

		distance_x = int(int(state)/12) + 1
		distance_y = int(int(state)%12) + 1

		for each_action in self.env.action_space:
			if action == each_action:
				feature_vector.append(distance_x)
				feature_vector.append(distance_y)
			else:
				feature_vector.append(0.0)
				feature_vector.append(0.0)

		return feature_vector

	def getDiscountedReturn(self, episode):
		discounted_return = 0.0
		for episode_iterator in range(len(episode) - 1, -1, -1):
			discounted_return = (self.GAMMA * discounted_return) + episode[episode_iterator][2]

	def evaluateScoreFunction(self, state, action):
		state_action_feature = self.getFeatureVector(state, action)
		all_action_features = []
		for each_action in self.env.action_space:
			all_action_features.append(self.getFeatureVector(state, each_action))

		action_feature_in_expectation = np.divide([sum(x) for x in zip(all_action_features[0], all_action_features[1], all_action_features[2], all_action_features[3])], 4)
		return np.subtract(state_action_feature, action_feature_in_expectation)

	def doGradientAscent(self, score_function, discounted_return):
		self.weights = np.add(self.weights, np.multiply((np.multiply(score_function, discounted_return)), self.STEP_SIZE))