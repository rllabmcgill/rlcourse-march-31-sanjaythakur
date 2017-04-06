import Cliff_Walk_Environment
import REINFORCE

#Defining the hyper-parameters
NUMBER_OF_EPISODES_TO_CONSIDER = 10
GAMMA = 0.9

def getDiscountedReturn(episode):
    discounted_return = 0.0
    for episode_iterator in range(len(episode) - 1, -1, -1):
        discounted_return = (GAMMA * discounted_return) + episode[2]

env = Cliff_Walk_Environment.Cliff_Walking_Environment(START_STATE = '36', END_STATE = '47')
reinforce_agent = REINFORCE.REINFORCE_Agent(env = env)

for episode_iterator in range(NUMBER_OF_EPISODES_TO_CONSIDER):
	episode = reinforce_agent.generateEpisode()
    for episode_iterator in range(len(episode)):
        discounted_return = getDiscountedReturn(episode[episode_iterator:])
        score_function =        

#print(env.transition_dynamics)

#print(env.immediate_reward_dynamics)
