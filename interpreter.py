'''List intepreter'''

class Grammar(object):
    def __init__(self):
        self.variable_definition_token = 'let'
        self.variable_definition_rule = 'LEFT_HAND_ASSIGNMENT'
