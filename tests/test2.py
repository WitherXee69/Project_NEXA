for index, item in enumerate(tail_flags):
    if item.startswith("-") and item in schema:
        for key, value in schema.items():
            if item == key and value == "bool":
                parsed_schema[key] = True
            elif item == key and value == "value":
                if (index + 1) < len(tail_flags):
                    if not tail_flags[index + 1].startswith("-"):
                        parsed_schema[key] = tail_flags[index + 1]
                    else:
                        parsed_schema[key] = tail_flags[index + 2]
                else:
                    print("No value found")
    elif item.startswith("-") and item not in schema:
        # For testing
        print("Unknown flag:", item)
    elif not item.startswith("-"):
        pass
# For testing
print(parsed_schema)