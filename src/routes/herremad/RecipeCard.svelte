<script lang="ts">
	let {
		dish
	}: {
		dish: {
			id: string;
			name: string;
			serves: number;
			ingredients: { label: string | null; items: string[] }[];
			method: { label: string | null; steps: string[] }[];
		};
	} = $props();

	let showIngredients = $state(false);
	let showMethod = $state(false);
</script>

<article class="recipe-card">
	<div class="card-header">
		<h2>{dish.name}</h2>
		<span class="serves-badge">Serveres til {dish.serves}</span>
	</div>

	<div class="card-actions">
		<button
			class="toggle-btn"
			onclick={() => (showIngredients = !showIngredients)}
			aria-expanded={showIngredients}
		>
			{showIngredients ? 'Skjul' : 'Vis'} ingredienser
		</button>
		<button
			class="toggle-btn"
			onclick={() => (showMethod = !showMethod)}
			aria-expanded={showMethod}
		>
			{showMethod ? 'Skjul' : 'Vis'} fremgangsmåde
		</button>
	</div>

	{#if showIngredients}
		<section class="recipe-section">
			<h3>Ingredienser</h3>
			{#each dish.ingredients as group, i (i)}
				<div class="ingredient-group">
					{#if group.label}
						<h4>{group.label}</h4>
					{/if}
					<ul>
						{#each group.items as item, j (item + j)}
							<li>{item}</li>
						{/each}
					</ul>
				</div>
			{/each}
		</section>
	{/if}

	{#if showMethod}
		<section class="recipe-section">
			<h3>Fremgangsmåde</h3>
			{#each dish.method as group, i (i)}
				<div class="method-group">
					{#if group.label}
						<h4>{group.label}</h4>
					{/if}
					<ol>
						{#each group.steps as step, j (step + j)}
							<li>{step}</li>
						{/each}
					</ol>
				</div>
			{/each}
		</section>
	{/if}
</article>

<style>
	.recipe-card {
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: 16px;
		padding: 1.5rem;
		box-shadow: 0 4px 12px var(--shadow);
		transition:
			transform 0.2s ease,
			box-shadow 0.2s ease;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.recipe-card:hover {
		transform: translateY(-4px);
		box-shadow: 0 10px 24px var(--shadow-strong);
	}

	.card-header {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	h2 {
		font-size: 1.5rem;
		font-weight: 700;
		color: var(--text);
		margin: 0;
	}

	h3 {
		font-size: 1.1rem;
		font-weight: 700;
		color: var(--text);
		margin: 0 0 0.75rem;
	}

	h4 {
		font-size: 0.95rem;
		font-weight: 600;
		color: var(--text-muted);
		margin: 0 0 0.5rem;
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.serves-badge {
		align-self: flex-start;
		background: var(--badge-bg);
		color: var(--badge-text);
		font-size: 0.85rem;
		font-weight: 600;
		padding: 0.25rem 0.75rem;
		border-radius: 999px;
	}

	.card-actions {
		display: flex;
		gap: 0.5rem;
		flex-wrap: wrap;
	}

	.toggle-btn {
		background: var(--surface-2);
		border: 1px solid var(--border);
		color: var(--text);
		font-size: 0.85rem;
		font-weight: 600;
		padding: 0.5rem 1rem;
		border-radius: 8px;
		cursor: pointer;
		transition:
			background 0.15s ease,
			border-color 0.15s ease;
	}

	.toggle-btn:hover {
		background: var(--border);
	}

	.toggle-btn[aria-expanded='true'] {
		background: var(--accent-2);
		border-color: var(--accent-2);
		color: #ffffff;
	}

	.recipe-section {
		border-top: 1px solid var(--border);
		padding-top: 1rem;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	ul,
	ol {
		margin: 0;
		padding-left: 1.25rem;
		color: var(--text-muted);
		font-size: 0.95rem;
		line-height: 1.6;
	}

	li {
		margin-bottom: 0.35rem;
	}
</style>
