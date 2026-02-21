class PromptProvider:
    def get_prompt(self, context):
        # Get the current working directory
        if str(context.home) in str(context.cwd):
            locholder = str(context.cwd).replace(str(context.home), "~")
        else:
            locholder = str(context.cwd)

        if context.verbose_mode:
            return f"\nNEXA [{locholder}] > "
        else:
            return "\n"

        # return f"NEXA [{locholder}] > "