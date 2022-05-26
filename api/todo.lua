local uuid = require("uuid")
local json = require("cjson")
local todolist = {}

local function url_for(id)
  return ngx.var.site_url .. "/todos/" .. id
end

local function repr(todo)
  todo.url = url_for(todo.id)
  return json.encode(todo)
end

todolist.create = function(data, items)
  local id = uuid()
  local item = {title = data.title, id = id, completed = false}
  items:set(id, json.encode(item))
  return repr(item)
end

todolist.delete = function(id, items)
  items:delete(id)
end

todolist.get = function(id, items)
  local item = items:get(id)
  if item ~= nil then
    return repr(json.decode(items:get(id)))
  end
  return nil
end

todolist.list = function(items)
  local list = {}
  local ids = items:get_keys()
  for _, id in ipairs(ids) do
    table.insert(list, items:get(id))
  end
  return json.encode(list)
end

todolist.update = function(id, prev_data, new_data, items)
  local data = prev_data
  for k, _ in pairs(new_data) do
    data[k] = new_data[k]
  end
  items:replace(id, data)
  return repr(data)
end

todolist.flush = function(items)
  items:flush_all()
end

return todolist