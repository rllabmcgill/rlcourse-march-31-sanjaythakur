import sys

#Defining a few constants

#Defining colors for highlighting important aspects
GREEN = lambda x: '\x1b[32m{}\x1b[0m'.format(x)
BLUE = lambda x: '\x1b[34m{}\x1b[0m'.format(x)
RED = lambda x: '\x1b[31m{}\x1b[0m'.format(x)


class Cliff_Walking_Environment():

	def __init__(self, START_STATE = '36', END_STATE = '47'):

		#The environment states
		self.all_states = [
			'00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
			'12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
			'24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35',
			'36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47'
			]

		self.cliff_states = ['37', '38', '39', '40', '41', '42', '43', '44', '45', '46']

		if ((START_STATE in self.cliff_states) or (END_STATE in self.cliff_states)):
			sys.exit('Neither the start state or the end state can be in the cliffs. Program is terminating')
		
		self.START_STATE = START_STATE
		self.END_STATE = END_STATE

		#All possible actions defined
		self.ACTION_UP = 'UP'
		self.ACTION_DOWN = 'DOWN'
		self.ACTION_LEFT = 'LEFT'
		self.ACTION_RIGHT = 'RIGHT'
		
		self.action_space = [self.ACTION_UP, self.ACTION_RIGHT, self.ACTION_DOWN, self.ACTION_LEFT]

		self.transition_dynamics = self.defineTransitionDynamics()
		self.immediate_reward_dynamics = self.defineImmediateRewardDynamics()

		
	def defineTransitionDynamics(self):
		transition_dynamics = {
		'00': {self.ACTION_UP : '00', self.ACTION_RIGHT : '01', self.ACTION_DOWN: '12', self.ACTION_LEFT: '00'},
		'01': {self.ACTION_UP : '01', self.ACTION_RIGHT : '02', self.ACTION_DOWN: '13', self.ACTION_LEFT: '00'},
		'02': {self.ACTION_UP : '02', self.ACTION_RIGHT : '03', self.ACTION_DOWN: '14', self.ACTION_LEFT: '01'},
		'03': {self.ACTION_UP : '03', self.ACTION_RIGHT : '04', self.ACTION_DOWN: '15', self.ACTION_LEFT: '02'},
		'04': {self.ACTION_UP : '04', self.ACTION_RIGHT : '05', self.ACTION_DOWN: '16', self.ACTION_LEFT: '03'},
		'05': {self.ACTION_UP : '05', self.ACTION_RIGHT : '06', self.ACTION_DOWN: '17', self.ACTION_LEFT: '04'},
		'06': {self.ACTION_UP : '06', self.ACTION_RIGHT : '07', self.ACTION_DOWN: '18', self.ACTION_LEFT: '05'},
		'07': {self.ACTION_UP : '07', self.ACTION_RIGHT : '08', self.ACTION_DOWN: '19', self.ACTION_LEFT: '06'},
		'08': {self.ACTION_UP : '08', self.ACTION_RIGHT : '09', self.ACTION_DOWN: '20', self.ACTION_LEFT: '07'},
		'09': {self.ACTION_UP : '09', self.ACTION_RIGHT : '10', self.ACTION_DOWN: '21', self.ACTION_LEFT: '08'},
		'10': {self.ACTION_UP : '10', self.ACTION_RIGHT : '11', self.ACTION_DOWN: '22', self.ACTION_LEFT: '09'},
		'11': {self.ACTION_UP : '11', self.ACTION_RIGHT : '11', self.ACTION_DOWN: '23', self.ACTION_LEFT: '10'},
		'12': {self.ACTION_UP : '00', self.ACTION_RIGHT : '13', self.ACTION_DOWN: '24', self.ACTION_LEFT: '12'},
		'13': {self.ACTION_UP : '01', self.ACTION_RIGHT : '14', self.ACTION_DOWN: '25', self.ACTION_LEFT: '12'},
		'14': {self.ACTION_UP : '02', self.ACTION_RIGHT : '15', self.ACTION_DOWN: '26', self.ACTION_LEFT: '13'},
		'15': {self.ACTION_UP : '03', self.ACTION_RIGHT : '16', self.ACTION_DOWN: '27', self.ACTION_LEFT: '14'},
		'16': {self.ACTION_UP : '04', self.ACTION_RIGHT : '17', self.ACTION_DOWN: '28', self.ACTION_LEFT: '15'},
		'17': {self.ACTION_UP : '05', self.ACTION_RIGHT : '18', self.ACTION_DOWN: '29', self.ACTION_LEFT: '16'},
		'18': {self.ACTION_UP : '06', self.ACTION_RIGHT : '19', self.ACTION_DOWN: '30', self.ACTION_LEFT: '17'},
		'19': {self.ACTION_UP : '07', self.ACTION_RIGHT : '20', self.ACTION_DOWN: '31', self.ACTION_LEFT: '18'},
		'20': {self.ACTION_UP : '08', self.ACTION_RIGHT : '21', self.ACTION_DOWN: '32', self.ACTION_LEFT: '19'},
		'21': {self.ACTION_UP : '09', self.ACTION_RIGHT : '22', self.ACTION_DOWN: '33', self.ACTION_LEFT: '20'},
		'22': {self.ACTION_UP : '10', self.ACTION_RIGHT : '23', self.ACTION_DOWN: '34', self.ACTION_LEFT: '21'},
		'23': {self.ACTION_UP : '11', self.ACTION_RIGHT : '23', self.ACTION_DOWN: '35', self.ACTION_LEFT: '22'},
		'24': {self.ACTION_UP : '12', self.ACTION_RIGHT : '25', self.ACTION_DOWN: '36', self.ACTION_LEFT: '24'},
		'25': {self.ACTION_UP : '13', self.ACTION_RIGHT : '26', self.ACTION_DOWN: self.START_STATE, self.ACTION_LEFT: '24'},
		'26': {self.ACTION_UP : '14', self.ACTION_RIGHT : '27', self.ACTION_DOWN: self.START_STATE, self.ACTION_LEFT: '25'},
		'27': {self.ACTION_UP : '15', self.ACTION_RIGHT : '28', self.ACTION_DOWN: self.START_STATE, self.ACTION_LEFT: '26'},
		'28': {self.ACTION_UP : '16', self.ACTION_RIGHT : '29', self.ACTION_DOWN: self.START_STATE, self.ACTION_LEFT: '27'},
		'29': {self.ACTION_UP : '17', self.ACTION_RIGHT : '30', self.ACTION_DOWN: self.START_STATE, self.ACTION_LEFT: '28'},
		'30': {self.ACTION_UP : '18', self.ACTION_RIGHT : '31', self.ACTION_DOWN: self.START_STATE, self.ACTION_LEFT: '29'},
		'31': {self.ACTION_UP : '19', self.ACTION_RIGHT : '32', self.ACTION_DOWN: self.START_STATE, self.ACTION_LEFT: '30'},
		'32': {self.ACTION_UP : '20', self.ACTION_RIGHT : '33', self.ACTION_DOWN: self.START_STATE, self.ACTION_LEFT: '31'},
		'33': {self.ACTION_UP : '21', self.ACTION_RIGHT : '34', self.ACTION_DOWN: self.START_STATE, self.ACTION_LEFT: '32'},
		'34': {self.ACTION_UP : '22', self.ACTION_RIGHT : '35', self.ACTION_DOWN: self.START_STATE, self.ACTION_LEFT: '33'},
		'35': {self.ACTION_UP : '23', self.ACTION_RIGHT : '35', self.ACTION_DOWN: '47', self.ACTION_LEFT: '34'},
		'36': {self.ACTION_UP : '24', self.ACTION_RIGHT : self.START_STATE, self.ACTION_DOWN: '36', self.ACTION_LEFT: '36'},
		'47': {self.ACTION_UP : '35', self.ACTION_RIGHT : '47', self.ACTION_DOWN: '47', self.ACTION_LEFT: self.START_STATE}
		}
		transition_dynamics[self.END_STATE] = {self.ACTION_UP : self.END_STATE, self.ACTION_RIGHT : self.END_STATE, self.ACTION_DOWN: self.END_STATE, self.ACTION_LEFT: self.END_STATE}
		return transition_dynamics

	def defineImmediateRewardDynamics(self):		
		immediate_reward_dynamics = {
		'00': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'01': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'02': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'03': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'04': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'05': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'06': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'07': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'08': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'09': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'10': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'11': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'12': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'13': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'14': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'15': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'16': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'17': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'18': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'19': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'20': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'21': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'22': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'23': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'24': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'25': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -100, self.ACTION_LEFT: -1},
		'26': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -100, self.ACTION_LEFT: -1},
		'27': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -100, self.ACTION_LEFT: -1},
		'28': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -100, self.ACTION_LEFT: -1},
		'29': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -100, self.ACTION_LEFT: -1},
		'30': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -100, self.ACTION_LEFT: -1},
		'31': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -100, self.ACTION_LEFT: -1},
		'32': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -100, self.ACTION_LEFT: -1},
		'33': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -100, self.ACTION_LEFT: -1},
		'34': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -100, self.ACTION_LEFT: -1},
		'35': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'36': {self.ACTION_UP : -1, self.ACTION_RIGHT : -100, self.ACTION_DOWN: -1, self.ACTION_LEFT: -1},
		'47': {self.ACTION_UP : -1, self.ACTION_RIGHT : -1, self.ACTION_DOWN: -1, self.ACTION_LEFT: -100}
		}

		for state in self.transition_dynamics.keys():
			for action in self.action_space:
				if self.transition_dynamics[state][action] == self.END_STATE:
					immediate_reward_dynamics[state][action] = 0

		immediate_reward_dynamics[self.END_STATE] = {self.ACTION_UP : 0, self.ACTION_RIGHT : 0, self.ACTION_DOWN: 0, self.ACTION_LEFT: 0}
		return immediate_reward_dynamics


	def printMDP(self):
		for state in self.all_states:
			if not state in self.cliff_states:
				print(str(state) + str(self.transition_dynamics[state]))

		print('')

		for state in self.all_states:
			if not state in self.cliff_states:
				print(str(state) + str(self.immediate_reward_dynamics[state]))