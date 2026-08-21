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
		background: #ffffff;
		border: 1px solid #e5e7eb;
		border-radius: 16px;
		padding: 1.5rem;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
		transition:
			transform 0.2s ease,
			box-shadow 0.2s ease;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.recipe-card:hover {
		transform: translateY(-4px);
		box-shadow: 0 10px 24px rgba(0, 0, 0, 0.1);
	}

	.card-header {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	h2 {
		font-size: 1.5rem;
		font-weight: 700;
		color: #1f2937;
		margin: 0;
	}

	h3 {
		font-size: 1.1rem;
		font-weight: 700;
		color: #374151;
		margin: 0 0 0.75rem;
	}

	h4 {
		font-size: 0.95rem;
		font-weight: 600;
		color: #6b7280;
		margin: 0 0 0.5rem;
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.serves-badge {
		align-self: flex-start;
		background: #dcfce7;
		color: #166534;
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
		background: #f3f4f6;
		border: 1px solid #e5e7eb;
		color: #374151;
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
		background: #e5e7eb;
	}

	.toggle-btn[aria-expanded='true'] {
		background: #16a34a;
		border-color: #16a34a;
		color: #ffffff;
	}

	.recipe-section {
		border-top: 1px solid #e5e7eb;
		padding-top: 1rem;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	ul,
	ol {
		margin: 0;
		padding-left: 1.25rem;
		color: #4b5563;
		font-size: 0.95rem;
		line-height: 1.6;
	}

	li {
		margin-bottom: 0.35rem;
	}
</style>
