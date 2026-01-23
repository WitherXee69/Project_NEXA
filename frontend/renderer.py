class Renderer:
    def render_tree(self, data, prefix=""):
        if isinstance(data, dict):
            items = list(data.items())
        else:
            items = list(enumerate(data))
        
        for i, (key, value) in enumerate(items):
            is_last = i == len(items) - 1
            connector = "└── " if is_last else "├── "
            print(prefix + connector + str(key))

            if isinstance(value, (dict, list)):
                extension = "    " if is_last else "│   "
                self.render_tree(value, prefix + extension)
            elif value is not None:
                extension = "    " if is_last else "│   "
                lines = str(value).split(',')
                for j, line in enumerate(lines):
                    if line.strip():  # Only print non-empty lines
                        line_connector = "└── " if j == len(lines) - 1 else "├── "
                        print(prefix + extension + line_connector + line)
            
            # Add blank line between interfaces
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
