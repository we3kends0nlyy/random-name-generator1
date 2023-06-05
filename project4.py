# project4.py
#
# ICS 33 Spring 2023
# Project 4: Still Looking for Something
import random
from pathlib import Path

def main(testing=False) -> None:
    ask_for_inputs(testing)

def ask_for_inputs(testing):
    grammar_file = Path(input())
    num_of_sentences = int(input())
    start_variable = input()
    file_1 = open(grammar_file, "r")
    grammar = Grammar()
    grammar.grammar_object = grammar
    grammar.store_rules(file_1)
    for num in range(num_of_sentences):
        x = call_duck_typed_method(["1", "[]"], grammar, start_variable, grammar)
        string_list = []
        string_to_print = ""
        for i in x:
            if i.startswith("[") is False and i.endswith("]") is False:
                string_list.append(i)
        for symbol in string_list:
            string_to_print += f" {symbol}"
        print(string_to_print[1:])
    if testing is True:
        file_1.close()

def call_duck_typed_method(current_sent_state, current_class, start_variable, grammar):
    yield from current_class.generate_sentence_fragment(current_sent_state, current_class, start_variable, grammar)

class TerminalSymbol:
    def __init__(self):
        pass
    def generate_sentence_fragment(self, current_sent_frag, current_class, starter_variable, gram_object, index):
        return current_sent_frag[index]

class VariableSymbol:
    def __init__(self):
        pass
    def generate_sentence_fragment(self, current_sent_frag, current_class, starter_variable, gram_object, index):
        searching_for = current_sent_frag[index][1:-1]
        yield from call_duck_typed_method(starter_variable, gram_object, searching_for, gram_object)

class Option:
    def __init__(self):
        pass

    def generate_sentence_fragment(self, current_sent_frag, current_class, starter_variable, gram_object):
        for index in range(len(current_sent_frag)):
            if current_sent_frag[index].startswith("[") and current_sent_frag[index].endswith("]"):
                variable = VariableSymbol()
                yield from variable.generate_sentence_fragment(current_sent_frag, current_class, starter_variable, gram_object, index)
            else:
                terminal = TerminalSymbol()
                yield terminal.generate_sentence_fragment(current_sent_frag, current_class, starter_variable, gram_object, index)

class Rule:
    def __init__(self):
        pass

    def generate_random_number(self, options_of_start_variable):
        list_of_weights = []
        for option in options_of_start_variable[1:]:
            for i in range(int(option[0])):
                list_of_weights.append(option[0])
        random_num_of_list_of_weights = random.choice(list_of_weights)
        x = True
        while x is True:
            random_num_in_ops_of_start_var = random.randint(0, len(options_of_start_variable)-1)
            if options_of_start_variable[random_num_in_ops_of_start_var][0] == random_num_of_list_of_weights:
                final_option_chosen = options_of_start_variable[random_num_in_ops_of_start_var]
                x = False
        return final_option_chosen


    def generate_sentence_fragment(self, options_of_start_variable, current_class, starter_variable, gram_object):
        option_chosen = self.generate_random_number(options_of_start_variable)
        option = Option()
        yield from call_duck_typed_method(option_chosen[1:], option, starter_variable, gram_object)


class Grammar:
    def __init__(self, original_grammar=None):
        self.original_grammar = original_grammar
        self.file = []
        self.grammar_object = None


    def store_rules(self, file_1):
        try:
            file_iterable = iter(file_1)
            while True:
                next_line = next(file_iterable)
                if next_line == "{" + "\n":
                    second_list = []
                    while next_line.strip(" ") != "}\n":
                        next_line = next(file_iterable)
                        second_list.append(next_line.strip("\n").split(" "))
                    self.file.append(second_list)
                else:
                    pass
        except StopIteration:
            self.file.append(second_list)

    def generate_sentence_fragment(self, search_for_variable, next_class, starter_variable, gram_object):
        options_of_search_variable = []
        for next_line in self.file:
            if next_line[0][0] == starter_variable:
                options_of_search_variable = next_line
        rule = Rule()
        yield from call_duck_typed_method(options_of_search_variable[0:-1], rule, starter_variable, gram_object)

if __name__ == '__main__':
    main()