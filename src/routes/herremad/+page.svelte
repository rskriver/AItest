<script lang="ts">
	import RecipeCard from '$lib/components/RecipeCard.svelte';
	import menuData from '$lib/menues/2025/herremad_datoer_2025.json';

	interface Recipe {
		name: string;
		ID: string;
		Link: string;
		type: string;
	}

	interface MenuDate {
		date: string;
		Link: string;
		recipes: Recipe[];
	}

	interface IngredientGroup {
		label: string | null;
		items: string[];
	}

	interface MethodGroup {
		label: string | null;
		steps: string[];
	}

	interface Dish {
		id: string;
		name: string;
		type: string;
		serves?: number;
		ingredients: IngredientGroup[];
		method: MethodGroup[];
	}

	interface MenuFile {
		menu: {
			title: string;
			date: string;
			image: string;
			dishes: Dish[];
		};
	}

	const menuFiles = import.meta.glob('../../lib/menues/2025/*.json', { eager: true }) as Record<
		string,
		{ default: MenuFile }
	>;

	const menus = $derived(
		(menuData as MenuDate[]).slice().sort((a, b) => parseDate(a.date) - parseDate(b.date))
	);

	const typeLabels: Record<string, string> = {
		forret: 'Forret',
		hovedret: 'Hovedret',
		dessert: 'Dessert'
	};

	// Build a normalized-name lookup of all dishes from the per-date menu files.
	const recipeLookup = new Map<string, Dish>();
	for (const mod of Object.values(menuFiles)) {
		for (const dish of mod.default?.menu?.dishes ?? []) {
			recipeLookup.set(normalize(dish.name), dish);
		}
	}

	let selectedRecipe = $state<Dish | null>(null);
	let selectedRecipeName = $state<string | null>(null);
	let selectedDate = $state<string | null>(null);

	function parseDate(d: string): number {
		const [day, month, year] = d.split('.').map(Number);
		return new Date(year, month - 1, day).getTime();
	}

	function formatDate(d: string): string {
		const [day, month, year] = d.split('.').map(Number);
		return new Date(year, month - 1, day).toLocaleDateString('da-DK', {
			weekday: 'long',
			day: 'numeric',
			month: 'long',
			year: 'numeric'
		});
	}

	function normalize(name: string): string {
		return name
			.normalize('NFD')
			.replace(/[\u0300-\u036f]/g, '')
			.toLowerCase()
			.trim();
	}

	function openRecipe(recipe: Recipe, date: string): void {
		const dish = recipeLookup.get(normalize(recipe.name));
		selectedRecipe = dish ?? null;
		selectedRecipeName = recipe.name;
		selectedDate = date;
	}

	function closeRecipe(): void {
		selectedRecipe = null;
		selectedRecipeName = null;
		selectedDate = null;
	}
</script>

<svelte:head>
	<title>Herremad</title>
</svelte:head>

<div class="herremad-container">
	<header class="page-header">
		<h1>Herremad</h1>
		<p class="intro-text">
			Vores hjemmelavede retter, lavet med omsorg og kvalitet. Vælg en dato for at se ugens menu.
		</p>
	</header>

	<div class="menu-list">
		{#each menus as menu (menu.date)}
			<article class="menu-card">
				<header class="menu-card-header">
					<time class="menu-date" datetime={menu.date}>{formatDate(menu.date)}</time>
				</header>

				<ul class="dish-list">
					{#each menu.recipes as recipe (recipe.Link)}
						<li class="dish-item">
							<span class="dish-type type-{recipe.type}">
								{typeLabels[recipe.type] ?? recipe.type}
							</span>
							<button
								class="dish-name"
								type="button"
								aria-expanded={selectedDate === menu.date && selectedRecipeName === recipe.name
									? 'true'
									: 'false'}
								onclick={() => openRecipe(recipe, menu.date)}
							>
								{recipe.name}
							</button>
						</li>
					{/each}
				</ul>

				{#if selectedDate === menu.date && selectedRecipe}
					<div class="recipe-card-wrapper" aria-live="polite">
						<div class="recipe-card-header">
							<button
								class="recipe-close"
								type="button"
								aria-label="Luk opskrift"
								onclick={closeRecipe}
							>
								Luk <span aria-hidden="true">✕</span>
							</button>
						</div>
						<RecipeCard recipe={selectedRecipe} />
					</div>
				{:else if selectedDate === menu.date && selectedRecipeName}
					<div class="recipe-card-wrapper" aria-live="polite">
						<div class="recipe-card-header">
							<button
								class="recipe-close"
								type="button"
								aria-label="Luk opskrift"
								onclick={closeRecipe}
							>
								Luk <span aria-hidden="true">✕</span>
							</button>
						</div>
						<div class="recipe-fallback">
							<h2 class="fallback-title">{selectedRecipeName}</h2>
							<p>Desværre er der ingen opskrift tilgængelig for denne ret endnu.</p>
						</div>
					</div>
				{/if}
			</article>
		{/each}
	</div>
</div>

<style>
	.herremad-container {
		max-width: 900px;
		margin: 0 auto;
		padding: 3rem 1.5rem;
		min-height: calc(100vh - 120px);
	}

	.page-header {
		text-align: center;
		margin-bottom: 3rem;
	}

	h1 {
		font-size: 3rem;
		font-weight: 800;
		margin-bottom: 1rem;
		background: linear-gradient(135deg, var(--heading-1), var(--heading-2));
		-webkit-background-clip: text;
		background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.intro-text {
		font-size: 1.25rem;
		color: var(--text-muted);
		max-width: 600px;
		margin: 0 auto;
	}

	.menu-list {
		display: flex;
		flex-direction: column;
		gap: 1.5rem;
	}

	.menu-card {
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: 16px;
		padding: 1.5rem;
		box-shadow: 0 4px 12px var(--shadow);
		transition:
			transform 0.2s ease,
			box-shadow 0.2s ease;
	}

	.menu-card:hover {
		transform: translateY(-4px);
		box-shadow: 0 10px 24px var(--shadow-strong);
	}

	.menu-card-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 1rem;
		flex-wrap: wrap;
		margin-bottom: 1rem;
		padding-bottom: 1rem;
		border-bottom: 1px solid var(--border);
	}

	.menu-date {
		font-size: 1.2rem;
		font-weight: 700;
		color: var(--text);
		text-transform: capitalize;
	}

	.dish-list {
		list-style: none;
		margin: 0;
		padding: 0;
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
	}

	.dish-item {
		display: flex;
		align-items: center;
		gap: 0.75rem;
	}

	.dish-type {
		flex-shrink: 0;
		font-size: 0.75rem;
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 0.05em;
		padding: 0.25rem 0.75rem;
		border-radius: 999px;
		min-width: 90px;
		text-align: center;
	}

	.type-forret {
		background: rgba(96, 165, 250, 0.15);
		color: #60a5fa;
	}

	.type-hovedret {
		background: rgba(251, 146, 60, 0.15);
		color: #fb923c;
	}

	.type-dessert {
		background: rgba(244, 114, 182, 0.15);
		color: #f472b6;
	}

	.dish-name {
		font-size: 1rem;
		font-weight: 600;
		color: var(--text);
		background: none;
		border: none;
		padding: 0;
		margin: 0;
		cursor: pointer;
		text-align: left;
		font-family: inherit;
	}

	.dish-name:hover {
		color: var(--accent-2);
		text-decoration: underline;
	}

	.dish-name:focus-visible {
		outline: 2px solid var(--accent-2);
		outline-offset: 2px;
		border-radius: 4px;
	}

	.recipe-card-wrapper {
		margin-top: 1.25rem;
		padding-top: 1.25rem;
		border-top: 1px solid var(--border);
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
		animation: fade-in 0.25s ease;
	}

	.recipe-card-header {
		display: flex;
		justify-content: flex-end;
	}

	.recipe-close {
		font-size: 0.9rem;
		font-weight: 600;
		color: var(--text-muted);
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: 999px;
		padding: 0.4rem 1rem;
		cursor: pointer;
		transition:
			color 0.2s ease,
			border-color 0.2s ease;
	}

	.recipe-close:hover {
		color: var(--accent-2);
		border-color: var(--accent-2);
	}

	.recipe-fallback {
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: 16px;
		padding: 1.5rem;
		box-shadow: 0 4px 12px var(--shadow);
	}

	.fallback-title {
		font-size: 1.4rem;
		font-weight: 800;
		margin: 0 0 0.5rem;
		color: var(--text);
	}

	.recipe-fallback p {
		margin: 0;
		color: var(--text-muted);
	}

	@keyframes fade-in {
		from {
			opacity: 0;
			transform: translateY(-8px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}

	@media (max-width: 480px) {
		.dish-item {
			flex-direction: column;
			align-items: flex-start;
			gap: 0.4rem;
		}

		.dish-type {
			min-width: auto;
		}
	}
</style>
