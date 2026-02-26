import shlex

def parser(input_str):
    try:
        tokens = shlex.split(input_str)
    except ValueError as e:
        return None, [], []

    command = tokens[0]
    if len(tokens) > 1:
        tail_tokens = tokens[1:]
        return command, tail_tokens
    else:
        return command, []

if __name__ == '__main__':
    inputs = input("Enter: ")
    print(parser(inputs))