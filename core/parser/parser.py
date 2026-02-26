import shlex

def parser(input_str):
    try:
        tokens = shlex.split(input_str, posix=False)
    except ValueError as e:
        return None, [], []

    if not tokens:
        return None, [], []
    else:
        command = tokens[0]
        if len(tokens) > 1:
            tail_tokens = tokens[1:]
            return command, tail_tokens
        else:
            return command, []