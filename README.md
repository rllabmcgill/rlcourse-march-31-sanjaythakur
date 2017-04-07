# COMP767_Task_5

## Task

To solve the Cliff World Environment using *REINFORCE*(Monte Carlo Policy Gradient) algorithm.

## Environment

* The environment is a 4 X 12 grid. 
* Reward is −1 on all transitions except those into the region marked “The Cliff.” 
* Stepping into this region incurs a reward of −100 and sends the agent instantly back to the start.

Inline-style: 
![alt text](cliff_walking.png "Cliff Walking Environment")

Reference:: Example 6.6 - Cliff Walking, An Introduction to Reinforcement Learning, Sutton and Barton, II Edition

## Scripts

There are three different files made for accompolishing the task.
1. **Cliff\_Walk\_Environment.py**
    This defines the *Cliff World* environment defining all the necessary MDP parameters, and functions to evaluate its various aspects.
2. **REINFORCE.py**
    This defines an agent which uses REINFORCE algorithm to learn to act model-free in an environment.
3. **PolicyGradientOnCliffWalk.ipynb**
    This combines the environment and the agent so that the learning process by an agent is performed in a model-free manner in the Cliff World Environment.
    The nature of the environment made it suitable to encode the features in a tabular setting.

## Observation and results

Owing to time constraints, the agent was made to learn on 5000 episodes. It was seen that the agent's number of steps taken to the reach the goal state kept on decreasing with more training. However, 5000 episodes were not sufficient enough for it to learn how to act in the environment most optimally. 
You can see from the *PolicyGradientOnCliff.ipynb' that the number of episodes in any 500 number of consecutive episodes that were able to reach the goal with 200 number of steps kept on increasing with more and more examples. 
One possible reason behind this slow learning is *REINFORCE*'s well known problem of having a lot of variance. It uses unbiased estimate of what it observes in the environment but at a cost of a lot of variance.
