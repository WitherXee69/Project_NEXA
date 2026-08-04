import shlex

cmd = input("enter command: ")

PIPELINE_SEPERATOR = ["|"]


pipeline_commands = {
    "data":None,
    "stages":[],
    "current_stage":0
}

if any(sep in cmd for sep in PIPELINE_SEPERATOR):
    # Handle pipeline commands

    pipeline_tokens = shlex.shlex(cmd, posix=True)
    pipeline_tokens.whitespace_split = True
    pipeline_tokens.whitespace = PIPELINE_SEPERATOR

    pipeline_commands["data"] = list(pipeline_tokens)
    pipeline_commands["stages"] = len(pipeline_commands["data"])

    print(pipeline_commands["data"])

else:
    tokens = shlex.split(cmd, posix=False)
    if not tokens:
        print("No command entered.")
    else:
        command = tokens[0]
        tail_tokens = tokens[1:] if len(tokens) > 1 else []
        print(f"Command: {command}, Tail Tokens: {tail_tokens}")
        