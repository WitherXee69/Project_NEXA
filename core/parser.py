def parser(input_str):
    parse = input_str.strip().split()

    flag_count = []

    if not parse:
        return None, [], []

    for item in parse:
        if not item:
            return None, [], []
        elif item.startswith("-"):
            flag_count.append(parse.index(item))
    if len(flag_count) > 0:
        return parse[0], parse[flag_count[0]:(len(flag_count) + 1)], parse[(len(flag_count) + 1):]
    return parse[0], None, parse[1:]