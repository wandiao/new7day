def lpopall(conn, key):
    with open('utils/lua_scripts/lpopall.lua', 'r') as lua_file:
        script = lua_file.read().replace('\n', ' ')
        lpopall_script = conn.register_script(script)
        return lpopall_script(keys=[key, ])


def get_commands(conn, identifier):
    with open('utils/lua_scripts/pull_commands.lua', 'r') as lua_file:
        script = lua_file.read().replace('\n', ' ')
        get_commands_script = conn.register_script(script)
        return get_commands_script(keys=[identifier, ])
