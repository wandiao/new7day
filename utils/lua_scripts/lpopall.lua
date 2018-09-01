local result = {}
local length = tonumber(redis.call('LLEN', KEYS[1]))
for i = 1 , length do
    local val = redis.call('LPOP', KEYS[1])
    if val then
        table.insert(result, val)
    end
end
return result
