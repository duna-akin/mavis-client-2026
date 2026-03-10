# coding: utf-8
#
# Copyright 2021 The Technical University of Denmark
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#    http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations
import sys
import itertools
import numpy as np
from utils import pos_add, pos_sub, APPROX_INFINITY
from collections import deque, defaultdict

import domains.hospital.state as h_state
import domains.hospital.goal_description as h_goal_description
import domains.hospital.level as h_level


class HospitalZeroHeuristic:
    def __init__(self):
        pass

    def preprocess(self, level: h_level.HospitalLevel):
        # This function will be called a single time prior 
        # to the search allowing us to preprocess the level such as
        # pre-computing lookup tables or other acceleration structures
        pass

    def h(self, state: h_state.HospitalState, 
                goal_description: h_goal_description.HospitalGoalDescription) -> int:
        return 0
    

class HospitalGoalCountHeuristics:

    def __init__(self):
        self.box_goal_positions = set()
        self.agent_goal_positions = set()


    def preprocess(self, level: h_level.HospitalLevel):
        # This function will be called a single time prior 
        # to the search allowing us to preprocess the level such as
        # pre-computing lookup tables or other acceleration structures
        #for goal in level.goals:
        #    if goal.goal_type == h_goal_description.HospitalGoalType.AGENT_AT:
        #        self.agent_goal_positions.add(goal.position)
        #    elif goal.goal_type == h_goal_description.HospitalGoalType.BOX_AT:
        #        self.box_goal_positions.add(goal.position)
            pass
         
    
    def h(self, state: h_state.HospitalState, 
                goal_description: h_goal_description.HospitalGoalDescription) -> int:
        
        for goal in goal_description.box_goals:
            self.box_goal_positions.add(goal[0])
        for goal in goal_description.agent_goals:
            self.agent_goal_positions.add(goal[0])
        goals = len(self.agent_goal_positions) + len(self.box_goal_positions)
        for agent_position in state.agent_positions:
            if agent_position[0] in self.agent_goal_positions:
                goals -= 1
        for box_position in state.box_positions:
            if box_position[0] in self.box_goal_positions:
                goals -= 1
        return goals
        

class HospitalAdvancedHeuristics:

    def __init__(self):
        raise NotImplementedError()

    def preprocess(self, level: h_level.HospitalLevel):
        # This function will be called a single time prior to the search allowing us to preprocess the level such as
        # pre-computing lookup tables or other acceleration structures
        raise NotImplementedError()

    def h(self, state: h_state.HospitalState, goal_description: h_goal_description.HospitalGoalDescription) -> int:
        # your heuristic goes here...      
        raise NotImplementedError()