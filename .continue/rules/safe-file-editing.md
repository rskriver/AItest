---
alwaysApply: true
---

When making small or targeted changes to an existing file (e.g. removing a single CSS rule, changing one line), ALWAYS use single_find_and_replace instead of edit_existing_file. Only use edit_existing_file when restructuring large portions, and in that case pass the complete intended content. Before ANY edit, call read_file to get current contents. After ANY edit, verify the result: read_file, and for critical files also confirm on disk via a terminal command (e.g. `Get-Content -Raw`) since the IDE read-back display can be truncated. Never trust a tool's success message as proof the file is intact.