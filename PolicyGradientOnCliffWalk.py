
# coding: utf-8

# In[1]:

import Cliff_Walk_Environment
import REINFORCE


# In[2]:

#Defining the hyper-parameters
NUMBER_OF_EPISODES_TO_CONSIDER = 10000
GAMMA = 0.9


# In[3]:

env = Cliff_Walk_Environment.Cliff_Walking_Environment(START_STATE = '36', END_STATE = '47')
reinforce_agent = REINFORCE.REINFORCE_Agent(env = env)


# In[4]:

episode_lengths = []
episode_rewards = []
for episode_iterator in range(NUMBER_OF_EPISODES_TO_CONSIDER):
    episode = reinforce_agent.generateEpisode()

    episode_lengths.append(len(episode))
    episode_rewards.append(reinforce_agent.getDiscountedReturn(episode))
    #print(reinforce_agent.weights)
    #env.printEnvironment(episode)

    if (episode_iterator % 500) == 0 and not (episode_iterator == 0):
        print('Episodes done', str(episode_iterator))
        print('Successful episodes between episode number', str(episode_iterator), '-' , str(episode_iterator - 500), "is", str(reinforce_agent.goal_reached))
        print('\n')
        reinforce_agent.goal_reached = 0

    for episode_iterator in range(len(episode)):
        episode_step = episode[episode_iterator]
        discounted_return = reinforce_agent.getDiscountedReturn(episode[episode_iterator:])
        score_function = reinforce_agent.evaluateScoreFunction(episode_step[0], episode_step[1])
        reinforce_agent.doGradientAscent(score_function, discounted_return)


# In[ ]:



