-- Mark every blockquote with a custom-style Div; paragraphs inside keep their own styles
-- (so lists stay lists). A post-processing step in Python adds the callout border/shading
-- to all paragraphs between the markers. Consecutive quotes get a small gap between them.
local function marker(kind)
  return pandoc.Div({pandoc.Para({pandoc.Str(kind)})},
                    pandoc.Attr("", {}, {{"custom-style", "Callout Marker"}}))
end

function Blocks(blocks)
  local out = pandoc.List()
  local prev_quote = false
  for _, b in ipairs(blocks) do
    if b.t == "BlockQuote" then
      if prev_quote then out:insert(marker("@@GAP@@")) end
      out:insert(marker("@@CALLOUT_START@@"))
      out:extend(b.content)
      out:insert(marker("@@CALLOUT_END@@"))
      prev_quote = true
    else
      out:insert(b)
      prev_quote = false
    end
  end
  return out
end
