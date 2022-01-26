#!/usr/local/bin/python

import os
#game from openAI gym
import gym_super_mario_bros
#joypad wrapper
from nes_py.wrappers import JoypadSpace
#simplified controls
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

#import the PPO (Proximal policy oprimizer) algorythm form OpenAI
from stable_baselines3 import PPO

# import frame stacker wrapper and grayscaling
from gym.wrappers import GrayScaleObservation
#import vectorization wrappers
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv

#check CUDA availiability
from torch.cuda import is_available
if not is_available():
    raise ValueError("no CUDA!")


# deal with LFS
old_name = "./train/best_model.csv"
new_name = "./train/best_model.zip"
if os.path.isfile(old_name):
    # Renaming the file
    os.rename(old_name, new_name)

#load best model
model = PPO.load('./train/best_model')

# Renaming the file for next run
os.rename(new_name, old_name)

#1. setup game base environnement
env = gym_super_mario_bros.make('SuperMarioBros-v0')

#2. reduce action space to something managable
env = JoypadSpace(env, SIMPLE_MOVEMENT)

#3. Grayscale
env = GrayScaleObservation(env, keep_dim=True)

#4. wrap inside the dummy env
env = DummyVecEnv([lambda: env])

#5. stack up the frame
env = VecFrameStack(env, 4, channels_order="last")

#start the game
state = env.reset()

#loop trhough the game
while True:
    #get berst action for each state
    action, state = model.predict(state)
    state, reward, done, info = env.step(action)
    env.render()


