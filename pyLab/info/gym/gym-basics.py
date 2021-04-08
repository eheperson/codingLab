#
#
#----------------------------------------------------------------------------------
# INSTALLATION
#   pip install gym
#   or
#   git clone https://github.com/openai/gym
#   cd gym
#   pip install -e .
#----------------------------------------------------------------------------------


#  bare minimum example of getting something running. 
#       This will run an instance of the CartPole-v1 environment for 1000 timesteps, 
#       rendering the environment at each step. 
import gym
env = gym.make('CartPole-v1')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()