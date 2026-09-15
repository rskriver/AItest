<script lang="ts">
	interface IngredientGroup {
		label: string | null;
		items: string[];
	}

	interface MethodGroup {
		label: string | null;
		steps: string[];
	}

	interface Recipe {
		id: string;
		name: string;
		type: string;
		serves?: number;
		ingredients: IngredientGroup[];
		method: MethodGroup[];
	}

	let { recipe }: { recipe: Recipe } = $props();

	// Number of group rows = the longer of the two group lists, so both
	// columns always render the same number of rows and labels stay aligned.
	const groupCount = $derived(
		Math.max(recipe.ingredients?.length ?? 0, recipe.method?.length ?? 0)
	);
</script>

<article class="recipe-card" role="region" aria-label={`Opskrift: ${recipe.name}`}>
	<header class="recipe-header">
		<h2 class="recipe-name">{recipe.name}</h2>
		<div class="recipe-meta">
			{#if recipe.type}
				<span class="recipe-type">{recipe.type}</span>
			{/if}
			{#if recipe.serves}
				<span class="recipe-serves">Serveres til {recipe.serves}</span>
			{/if}
		</div>
	</header>

	<div class="recipe-body">
		<div class="recipe-row row-headers">
			<h3 class="section-title">Ingredienser</h3>
			<h3 class="section-title">Fremgangsmåde</h3>
		</div>

		{#each Array.from({ length: groupCount }) as _, i (i)}
			<div class="recipe-row">
				<div class="recipe-group">
					{#if recipe.ingredients[i]?.label}
						<h4 class="group-label">{recipe.ingredients[i].label}</h4>
					{/if}
					<ul class="item-list">
						{#each recipe.ingredients[i]?.items ?? [] as item, j (j + ':' + item)}
							<li>{item}</li>
						{/each}
					</ul>
				</div>

				<div class="recipe-group">
					{#if recipe.method[i]?.label}
						<h4 class="group-label">{recipe.method[i].label}</h4>
					{/if}
					<ol class="step-list">
						{#each recipe.method[i]?.steps ?? [] as step, j (j + ':' + step)}
							<li>{step}</li>
						{/each}
					</ol>
				</div>
			</div>
		{/each}
	</div>
</article>

<style>
	.recipe-card {
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: 16px;
		padding: 1.5rem;
		box-shadow: 0 4px 12px var(--shadow);
		width: 100%;
		box-sizing: border-box;
	}

	.recipe-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 1rem;
		flex-wrap: wrap;
		margin-bottom: 1.5rem;
		padding-bottom: 1rem;
		border-bottom: 1px solid var(--border);
	}

	.recipe-name {
		font-size: 1.6rem;
		font-weight: 800;
		margin: 0;
		background: linear-gradient(135deg, var(--heading-1), var(--heading-2));
		-webkit-background-clip: text;
		background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.recipe-meta {
		display: flex;
		align-items: center;
		gap: 0.5rem;
		flex-wrap: wrap;
	}

	.recipe-type {
		font-size: 0.75rem;
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 0.05em;
		padding: 0.25rem 0.75rem;
		border-radius: 999px;
		background: rgba(251, 146, 60, 0.15);
		color: #fb923c;
	}

	.recipe-serves {
		font-size: 0.9rem;
		color: var(--text-muted);
	}

	.recipe-body {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
		width: 100%;
		box-sizing: border-box;
	}

	.recipe-row {
		display: grid;
		grid-template-columns: 1fr 2fr;
		gap: 2rem;
		min-width: 0;
	}

	.row-headers {
		align-items: baseline;
	}

	.section-title {
		font-size: 1.1rem;
		font-weight: 700;
		color: var(--text);
		margin: 0;
	}

	.recipe-group {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
		min-width: 0;
	}

	.group-label {
		font-size: 0.95rem;
		font-weight: 700;
		color: var(--accent-2);
		margin: 0;
	}

	.item-list,
	.step-list {
		margin: 0;
		padding-left: 1.25rem;
		display: flex;
		flex-direction: column;
		gap: 0.4rem;
		color: var(--text);
		line-height: 1.5;
		overflow-wrap: break-word;
		word-break: break-word;
	}

	.item-list {
		list-style: disc;
	}

	.step-list {
		list-style: decimal;
	}

	@media (max-width: 640px) {
		.recipe-row {
			grid-template-columns: 1fr;
			gap: 1rem;
		}
	}
</style>
