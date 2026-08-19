# Svelte 5 Coding Rules & Guardrails

You are strictly developing in **Svelte 5**. Never use deprecated Svelte 3/4 syntax.

## Mandatory Svelte 5 Paradigms

1. **Runes for State**: Always use `$state()` for local reactive state instead of `let variable = value`.
2. **Derived Values**: Always use `$derived(...)` or `$derived.by(...)` instead of `$: reactive = ...`.
3. **Side Effects**: Always use `$effect(() => { ... })` instead of `$: { ... }` blocks.
4. **Props Definition**: Use `let { propName = defaultValue }: Props = $props();` instead of `export let propName`.
5. **Slots & Children**: Use Snippets (`{#snippet name()}...{/snippet}`) and `children` props instead of `<slot />`.
6. **Event Handling**: Use standard HTML attributes like `onclick={handler}` instead of `on:click={handler}`.

## Tool Usage Instructions

- Whenever you are generating Svelte components, refactoring code, or unsure about Svelte 5 API edge cases, query the **Svelte MCP server** for relevant documentation and snippets before writing the final code.

# Agent Tooling & File Edit Rules

## File Edit Constraints

- NEVER attempt to rewrite an entire file if you are only changing a single section or function.
- Prefer targeted replacement operations over full file overwrites to prevent token truncation.
- If editing large files, make changes in smaller, logical chunks instead of one single massive tool payload.

# Output Instructions for Code Edits

- When executing file writes or using edit tools, DO NOT output any `<thought>` tags, explanations, or markdown commentary.
- Return ONLY the exact replacement code or search/replace block.
