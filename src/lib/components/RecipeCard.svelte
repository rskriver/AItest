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
		<section class="recipe-section">
			<h3 class="section-title">Ingredienser</h3>
			{#each recipe.ingredients as group}
				<div class="recipe-group">
					{#if group.label}
						<h4 class="group-label">{group.label}</h4>
					{/if}
					<ul class="item-list">
						{#each group.items as item}
							<li>{item}</li>
						{/each}
					</ul>
				</div>
			{/each}
		</section>

		<section class="recipe-section">
			<h3 class="section-title">Fremgangsmåde</h3>
			{#each recipe.method as group}
				<div class="recipe-group">
					{#if group.label}
						<h4 class="group-label">{group.label}</h4>
					{/if}
					<ol class="step-list">
						{#each group.steps as step}
							<li>{step}</li>
						{/each}
					</ol>
				</div>
			{/each}
		</section>
	</div>
</article>

<style>
	.recipe-card {
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: 16px;
		padding: 1.5rem;
		box-shadow: 0 4px 12px var(--shadow);
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
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 2rem;
	}

	.recipe-section {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
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
	}

	.item-list {
		list-style: disc;
	}

	.step-list {
		list-style: decimal;
	}

	@media (max-width: 640px) {
		.recipe-body {
			grid-template-columns: 1fr;
			gap: 1.5rem;
		}
	}
</style>
