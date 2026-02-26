class Renderer:
    def render_tree(self, data, prefix=""):
        if isinstance(data, dict):
            items = list(data.items())

        elif isinstance(data, list):
            items = [(None, value) for value in data]

        else:
            items = []

        for i, (key, value) in enumerate(items):
            is_last = i == len(items) - 1
            connector = "└── " if is_last else "├── "
            extension = "    " if is_last else "│   "

            # If key is None (list item)
            if key is None:
                print(prefix + connector + str(value))
                continue

            print(prefix + connector + str(key))

            if isinstance(value, (dict, list)):
                self.render_tree(value, prefix + extension)
            elif value is not None:
                print(prefix + extension + "└── " + str(value))

            #Add a blank line after each key-value pair for better readability
            if not is_last:
                print(prefix + "│")

    def render(self, result):
        if result is not None:
            if isinstance(result, (str, int, float, bool)):
                print(result)
            elif isinstance(result, list) or isinstance(result, dict):
                self.render_tree(result)
    
    def clear(self):
        print("\033c", end="")
