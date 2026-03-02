def frontend_cli(engine, renderer, prompt, context):

    prompt_str = prompt.get_prompt(context)
    command = input(prompt_str)

    output = engine.handler(command)
    if output:
        renderer.render(output)