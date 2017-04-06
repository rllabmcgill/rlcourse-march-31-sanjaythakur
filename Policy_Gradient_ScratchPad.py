import Cliff_Walk_Environment
import REINFORCE

#Defining the hyper-parameters
NUMBER_OF_EPISODES_TO_CONSIDER = 10000
GAMMA = 0.9

env = Cliff_Walk_Environment.Cliff_Walking_Environment(START_STATE = '36', END_STATE = '47')
reinforce_agent = REINFORCE.REINFORCE_Agent(env = env)

for episode_iterator in range(NUMBER_OF_EPISODES_TO_CONSIDER):
	episode = reinforce_agent.generateEpisode()
	#print(reinforce_agent.weights)
	#env.printEnvironment(episode)

	if (episode_iterator % 1000) == 0:
		print(reinforce_agent.goal_reached)
		reinforce_agent.goal_reached = 0

	for episode_iterator in range(len(episode)):
		episode_step = episode[episode_iterator]
		discounted_return = reinforce_agent.getDiscountedReturn(episode[episode_iterator:])
		score_function = reinforce_agent.evaluateScoreFunction(episode_step[0], episode_step[1])
		reinforce_agent.doGradientAscent(score_function, discounted_return)

#print(env.transition_dynamics)

#print(env.immediate_reward_dynamics)
