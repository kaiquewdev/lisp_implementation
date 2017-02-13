'''Lisp interpreter test'''

import unittest

from interpreter import Grammar

class GrammarTest(unittest.TestCase):
    def setUp(self):
        self.gr = Grammar()
    
    def test_grammar_instantiation(self):
        self.assertEqual(self.gr.__class__,Grammar)

    def test_grammar_variable_definition_token_root_scope(self):
        self.assertEqual(self.gr.variable_definition('token','root_scope'),'var')

    def test_grammar_variable_definition_token_nested_scope(self):
        self.assertEqual(self.gr.variable_definition('token','nested_scope'),'let')

    def test_grammar_variable_definition_rule(self):
        self.assertEqual(self.gr.variable_definition(),'LEFT_HAND_ASSIGNMENT')

    def test_grammar_precedence_token(self):
        self.assertEqual(self.gr.precedence('token'),['(',')'])

    def test_grammar_precedence_rule(self):
        self.assertEqual(self.gr.precedence('rule'),'HIGH_ORDER_OPERATION')

if __name__ == '__main__':
    unittest.main(verbosity=2)
