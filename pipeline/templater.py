import json
import random
import regex

class Token:
    def __init__(self, token_name, synonyms):
        self.token_name = token_name
        self.synonyms = synonyms

    def dict_from_json(json_file):
        loaded_dictionary = json.load(json_file)
        result = {}
        for (name, synonyms) in loaded_dictionary.items():
            result[name] = Token(name, synonyms)
        return result

    def pick(self):
        return random.choice(self.synonyms)

template_example = '''def {{ w.increment }}_{{ v.list }}({{ v.list }}, {{v.accu}}):
    return {{ o.append {{ v.list }} {{v.accu}} }}'''

class Template:
    def __init__(self, string_template, var_token_library, word_token_library, operation_token_library):
        self.string = string_template
        self.var_token_library = var_token_library
        self.word_token_library = word_token_library
        self.operation_token_library = operation_token_library

    def _resolve_variables(self, input = None):
        if not input:
            input = self.string
        matches = regex.findall('(\{\{\s*v\.([\w|_]*)\s*}})', input)
        for (group, name) in matches:
            if name not in self.resolved_tokens.keys():
                self.resolved_tokens[name] = self.var_token_library[name].pick()
            input = input.replace(group, self.resolved_tokens[name])
        return input

    def _resolve_words(self, input = None):
        if not input:
            input = self.string
        matches = regex.findall('(\{\{\s*w\.([\w|_]*)\s*}})', input)
        for (group, name) in matches:
            if name not in self.resolved_tokens.keys():
                self.resolved_tokens[name] = self.word_token_library[name].pick()
            input = input.replace(group, self.resolved_tokens[name])
        return input 

    def _resolve_operations(self, input = None):
        if not input:
            input = self.string
        matches = regex.findall('(\{\{\s*o\.([\w|_|\+|\-]*)([\w|_|\+|\-|\s]*)}})', input)
        for (group, name, variables_substring) in matches:
            if name not in self.resolved_tokens.keys():
                self.resolved_tokens[name] = self.operation_token_library[name].pick()
            operation = self.resolved_tokens[name]
            variables = variables_substring.split()
            for i, var in enumerate(variables):
                operation = operation.replace('<variable{}>'.format(i), var)
            input = input.replace(group, operation)
        return input 

    def render(self):
        self.resolved_tokens = {}
        rendered = self._resolve_variables()
        rendered = self._resolve_words(rendered)
        rendered = self._resolve_operations(rendered)
        return rendered

def main():
    variable_tokens = None
    word_tokens = None
    operation_tokens = None
    with open('pipeline/tokens/variables_tokens.json') as json_file:
        variable_tokens = Token.dict_from_json(json_file)
    with open ('pipeline/tokens/function_name_tokens.json') as json_file:
        word_tokens = Token.dict_from_json(json_file)
    with open ('pipeline/tokens/primitives_tokens.json') as json_file:
        operation_tokens = Token.dict_from_json(json_file)
    t = Template(template_example, var_token_library=variable_tokens, word_token_library=word_tokens, operation_token_library=operation_tokens)
    print(t.render())

if __name__ == "__main__":
    main()