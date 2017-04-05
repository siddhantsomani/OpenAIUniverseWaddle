#1: Should I turn ?
#2: Where to turn ?
import gym
import universe
import random

def main():
    #init envt
    env = gym.make('flashgames.CoasterRacer-v0')
    observation_n = env.reset()

    #init variables
    #num of game iterations
    n = 0
    j = 0
    #sum of observations
    total_sum = 0
    prev_total_sum = 0
    turn = False

    #define our turns or keyboard actions
    left = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]
    right = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
    forward = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', False)]

    #MainLogic
    while True:
        #iteration counter
        n+=1
