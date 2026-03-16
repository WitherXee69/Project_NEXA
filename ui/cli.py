def frontend_cli(engine, renderer, prompts, context, completer, session):

    prompt_str = prompts.get_prompt(context)
    command = session.prompt(f"{prompt_str}", completer=completer, complete_while_typing=False)

    output = engine.handler(command)
    if output:
        renderer.render(output)