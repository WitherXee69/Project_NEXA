def frontend_cli(engine, renderer, prompts, context, completer, history):

    prompt_str = prompts.get_prompt(context)
    command = history.prompt(f"{prompt_str}", completer=completer)

    output = engine.handler(command)
    if output:
        renderer.render(output)