import re # Regular Expressions Module
          # Used to give access to Regular Expressions, which are tools that let you search, match & manipulate text
          # based on predefined patterns.



# Regex Patterns
# [regex, token_type]
#
# Used to define patterns of Raw Strings 'r' combined with Metacharacters & Quantifiers to give them "rules" about when to
# determine that a pattern has been matched in a search, where the patterns are searched in the order they're defined.
patterns = [
    [r"\d*\.\d+|\d+\.\d*|\d+","number"], # Ex. [\d*\.\d+]: "\d*" == Zero or more repetitions of a digit | "\." == A dot character | "\d+" == At least one repetition of a digit
    [r"\+", "+"], # A '+' character is mapped to the token_type "+".
    [r".","error"] # Any other character that isn't a newline is mapped to the token_type "error" to catch all non-numbers.
]



# Compiles each 'r' Raw String into an 're.Pattern' object for speed & convenience to turn each row into [compiled_regex, token_type].
for pattern in patterns:
    pattern[0] = re.compile(pattern[0])


# Defines the core function to tokenize an inputted character array based on the defined patterns using Reguar Expressions.
def tokenize(characters):
    tokens = [] # List of Dictionaries
    position = 0
    while position < len(characters):
        # Find the first matching token:
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break

        assert match

        if tag == "error":
            raise Exception(f"Syntax error: illegal character :{[match.group(0)]}") # "match.group(0)" returns the entire match substring found.
        
        token = {"tag":tag, "position":position} # Defines a 'token' variable as a Dictionary with the key-value pair ("tag", "position").
        value = match.group(0) # Set 'value' equal to the matched substring.
        if token["tag"] == "number":
            if "." in value:
                token["value"] = float(value) # Dynamically creates a new key named "value" to hold token value.
            else:
                token["value"] = int(value)
        tokens.append(token)
        position = match.end()

    tokens.append({"tag":None, "position":position}) # Adds a final "EOF Token" to the end of the List to mark the end.
    return tokens

# Tester Function for basic functionality of the Tokenizer.
def test_simple_tokens():
    print("Test simple tokens...")
    assert tokenize("+") == [
        {"tag":"+", "position":0},
        {"tag":None, "position":1}
    ]
    assert tokenize("3") == [
        {"tag":"number", "position":0, "value":3},
        {"tag":None, "position":1}
    ]

if __name__ == "__main__":
    print("Testing Tokenizer...")
    test_simple_tokens()
    print("Done!")
