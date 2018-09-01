local commands = {}
for i,v in ipairs(redis.call('KEYS', 'commands:*')) do
    local process_id = redis.call('HGET', v, 'process_id')
    local refreshed = redis.call('HGET', v, 'refreshed')
    local keys = redis.call('HKEYS', v)
    for j,key in ipairs(keys) do
        table.insert(commands, key)
    end
    if process_id == KEYS[1] then
        table.insert(commands, process_id)
    end
end
return commands
