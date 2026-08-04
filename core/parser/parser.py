import shlex

def parser(input_str, context):
    try:
        tokens = shlex.split(input_str, posix=False)
    except ValueError as e:
        return None, []

    if not tokens:
        return None, []
    
    elif any(sep in input_str for sep in context.pipeline_separator):
        # Handle pipeline commands

        pipeline_tokens = shlex.shlex(input_str, posix=True)
        pipeline_tokens.whitespace_split = True
        pipeline_tokens.whitespace = context.pipeline_separator

        context.pipeline_commands["data"] = pipeline_tokens
        context.pipeline_commands["stages"] = len(list(pipeline_tokens))

        print(context.pipeline_commands["data"])


    else:
        command = tokens[0]
        if len(tokens) > 1:
            tail_tokens = tokens[1:]
            return command, tail_tokens
        else:
            return command, []
        