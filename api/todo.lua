local uuid = require("uuid")
local json = require("cjson")
local todolist = {}

todolist.create = function(data, items)
  local uid = uuid()
  local json_data = json.encode{title = data.title}
  items:set(uid, json_data)
  return json_data
end

return todolist