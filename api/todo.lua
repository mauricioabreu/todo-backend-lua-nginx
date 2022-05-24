local uuid = require("uuid")
local json = require("cjson")
local todolist = {}

todolist.create = function(data, items)
  local uid = uuid()
  local json_data = json.encode{title = data.title, uid = uid}
  items:set(uid, json_data)
  return json_data
end

todolist.delete = function(uid, items)
  items:delete(uid)
end

todolist.get = function(uid, items)
  return items:get(uid)
end

return todolist