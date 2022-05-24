local uuid = require("uuid")
local json = require("cjson")
local todolist = {}

todolist.create = function(data, items)
  local uid = uuid()
  local json_data = json.encode{title = data.title, uid = uid, completed = false}
  items:set(uid, json_data)
  return json_data
end

todolist.delete = function(uid, items)
  items:delete(uid)
end

todolist.get = function(uid, items)
  return items:get(uid)
end

todolist.list = function(items)
  local list = {}
  local uids = items:get_keys()
  for _, uid in ipairs(uids) do
    table.insert(list, json.decode(items:get(uid)))
  end
  return json.encode(list)
end

todolist.flush = function(items)
  items:flush_all()
end

return todolist