from core.error_handler import NoSchemaError, InvalidFlagError, MissingValueError, DuplicateFlagError

class Schema_Helper:
    def get_command_schema(self, cmd_name):
        if cmd_name:
            if hasattr(cmd_name, "schema"):
                return cmd_name.schema
            else:
                return None
        else:
            return None

    def helper(self, cmd_name, tail_flags):
        schema = self.get_command_schema(cmd_name)

        parsed_schema = {}
        parsed_args = []
        parse_index = 0

        while parse_index < len(tail_flags):
            item = tail_flags[parse_index]

            try:
                if item in parsed_schema:
                    raise DuplicateFlagError(item)
                    # return None, [], f"Duplicate flag: {item}"

                elif (item.startswith("-")) and item in schema:
                    if schema[item] == "bool":
                        parsed_schema[item] = True
                        parse_index += 1
                    elif schema[item] == "value":
                        if (parse_index + 1) < len(tail_flags) and not (tail_flags[parse_index + 1].startswith("-")):
                            parsed_schema[item] = tail_flags[parse_index + 1]
                            parse_index += 2
                        else:
                            raise MissingValueError(item)
                            # return None, [], f"No value found for {item}"

                elif (item.startswith("-")) and item not in schema:
                    raise InvalidFlagError(item)
                    # return None, [], f"Unknown flag: {item}"

            except InvalidFlagError as e:
                return None, [], e.message
            except MissingValueError as e:
                return None, [], e.message
            except DuplicateFlagError as e:
                return None, [], e.message

            else:
                parsed_args.append(item)
                parse_index += 1

        return parsed_schema, parsed_args, None