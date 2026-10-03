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

-- Prompt colour coding: <span class="goal|source|expect|constraint">…</span> in the Markdown
-- (invisible on GitHub) becomes a Word character style with its own background shading.
local PROMPT_STYLES = {goal = "Prompt Goal", source = "Prompt Source",
                       expect = "Prompt Expectations", constraint = "Prompt Constraints"}

function Inlines(inlines)
  local out, cur, style = pandoc.List(), nil, nil
  for _, il in ipairs(inlines) do
    local cls = il.t == "RawInline" and il.format == "html" and il.text:match('^<span class="([%w-]+)">$')
    if cls and PROMPT_STYLES[cls] and not cur then
      cur, style = pandoc.List(), PROMPT_STYLES[cls]
    elseif cur and il.t == "RawInline" and il.format == "html" and il.text == "</span>" then
      out:insert(pandoc.Span(cur, pandoc.Attr("", {}, {{"custom-style", style}})))
      cur = nil
    elseif cur then
      cur:insert(il)
    else
      out:insert(il)
    end
  end
  if cur then out:extend(cur) end  -- unclosed tag: keep the text unstyled
  return out
end
