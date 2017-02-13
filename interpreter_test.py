'''Lisp interpreter test'''

import unittest

from interpreter import Grammar

class GrammarTest(unittest.TestCase):
    def test_grammar_instantiation(self):
        self.assertEqual(Grammar().__class__,Grammar)

    def test_grammar_variable_definition(self):
        gr = Grammar()
        self.assertEqual(gr.variable_definition_token,'let')
        self.assertEqual(gr.variable_definition_rule,'LEFT_HAND_ASSIGNMENT')

if __name__ == '__main__':
    unittest.main(verbosity=2)
