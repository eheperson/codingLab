# ------------------------------------------------------------------------------------------------------------
#
#
# Sampling random actions from the environment’s action space is OK. 
#       But what actually are those actions? 
# 
#   Every environment comes with an action_space and an observation_space. 
#   These attributes are of type 'Space', and they describe the format of valid actions and observations:
#
import gym
env = gym.make('CartPole-v1')
print(env.action_space)
#> Discrete(2)
print(env.observation_space)
#> Box(4,)
#
#
# ------------------------------------------------------------------------------------------------------------
#
#
#   The Discrete space allows a fixed range of non-negative numbers, 
#   so in this case valid actions are either 0 or 1. 
#   
#   The Box space represents an n-dimensional box, so valid observations will be an array of 4 numbers. 
#   We can also check the Box’s bounds:
#
print(env.observation_space.high)
#> array([ 2.4       ,         inf,  0.20943951,         inf])
print(env.observation_space.low)
#> array([-2.4       ,        -inf, -0.20943951,        -inf])
#
#
# 
#   Box and Discrete are the most common Spaces. 
#   You can sample from a Space or check that something belongs to it:
#   
from gym import spaces
space = spaces.Discrete(8) # Set with 8 elements {0, 1, 2, ..., 7}
x = space.sample()
assert space.contains(x)
assert space.n == 8
#
#
#   For CartPole-v1 one of the actions applies force to the left, and one of them applies force to the right. 
#
# ------------------------------------------------------------------------------------------------------------
