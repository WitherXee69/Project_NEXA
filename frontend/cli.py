from frontend.renderer import Renderer

def frontend_cli(engine, context):

    renderer = Renderer()

    print("\033c", end="")
    print("""NEXA Shell [Version 0.1a]
by WitherXee. All rights reserved.\n""")

    while True:
        # Set up the location holder for the prompt
        if str(context.home) in str(context.cwd):
            locholder = str(context.cwd).replace(str(context.home), "~/")
        else:
            locholder = str(context.cwd)

        if context.verbose_mode:
            command = input("")
        else:
            command = input(f"NEXA [{locholder}] > ")

        if command == "exit":
            print("Shutting down NEXA...")
            break

        if command == "clear" or command == "cls":
            print("\033c", end="")

        output = engine.handler(command)
        if output:
            renderer.render(output)