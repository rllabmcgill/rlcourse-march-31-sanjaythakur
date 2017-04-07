import Cliff_Walk_Environment
import REINFORCE
import matplotlib.pyplot as plt

#Defining the hyper-parameters
NUMBER_OF_EPISODES_TO_CONSIDER = 10000
GAMMA = 0.9

env = Cliff_Walk_Environment.Cliff_Walking_Environment(START_STATE = '36', END_STATE = '47')
reinforce_agent = REINFORCE.REINFORCE_Agent(env = env)

episode_lengths = []
for episode_iterator in range(NUMBER_OF_EPISODES_TO_CONSIDER):
	episode = reinforce_agent.generateEpisode()

	episode_lengths.append(len(episode))

	#print(reinforce_agent.weights)
	#env.printEnvironment(episode)

	if (episode_iterator % 100) == 0:
		print(reinforce_agent.goal_reached)
		reinforce_agent.goal_reached = 0

	for episode_iterator in range(len(episode)):
		episode_step = episode[episode_iterator]
		discounted_return = reinforce_agent.getDiscountedReturn(episode[episode_iterator:])
		score_function = reinforce_agent.evaluateScoreFunction(episode_step[0], episode_step[1])
		reinforce_agent.doGradientAscent(score_function, discounted_return)

episode_number = [x for x in range(len(episode_lengths))]

print(episode_lengths)
plt.plot(episode_lengths)
plt.ylabel('Length of Episodes')
plt.show()

'''
plot(episode_number, episode_lengths, linewidth=2)
grid(1)
ylabel('Steps per episode')
xlabel('Episodes -> ')
legend(['REINFORCE'])
'''
#print(env.transition_dynamics)

#print(env.immediate_reward_dynamics)
