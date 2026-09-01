<script lang="ts">
	import RecipeCard from '$lib/components/RecipeCard.svelte';

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

	const dateFiles = import.meta.glob('../../lib/menues/*/herremad_datoer_*.json', {
		eager: true
	}) as Record<string, { default: MenuDate[] }>;

	const menuFiles = import.meta.glob('../../lib/menues/*/*.json', {
		eager: true
	}) as Record<string, { default: MenuFile }>;

	const years = [2025, 2024, 2023, 2022, 2021, 2020];
	const typeLabels: Record<string, string> = {
		forret: 'Forret',
		hovedret: 'Hovedret',
		dessert: 'Dessert'
	};

	let selectedYear = $state<number>(2025);
	let activeSelection = $state<{ date: string; name: string } | null>(null);

	// Helpers
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

	// Derived values
	const currentYearNum = $derived(Number(selectedYear));

	const menus = $derived.by(() => {
		const key = Object.keys(dateFiles).find((k) =>
			k.endsWith(`herremad_datoer_${currentYearNum}.json`)
		);
		const data = key ? (dateFiles[key].default ?? []) : [];
		return [...data].sort((a, b) => parseDate(a.date) - parseDate(b.date));
	});

	const recipeLookup = $derived.by(() => {
		const map = new Map<string, Dish>();
		for (const [path, mod] of Object.entries(menuFiles)) {
			if (path.includes('herremad_datoer_')) continue;
			if (!path.includes(`/${currentYearNum}/`)) continue;

			for (const dish of mod.default?.menu?.dishes ?? []) {
				if (dish?.name) {
					map.set(normalize(dish.name), dish);
				}
			}
		}
		return map;
	});

	const selectedRecipe = $derived(
		activeSelection ? (recipeLookup.get(normalize(activeSelection.name)) ?? null) : null
	);

	// Reset active selection when switching years
	$effect(() => {
		void selectedYear;
		activeSelection = null;
	});

	function toggleRecipe(recipeName: string, date: string): void {
		if (activeSelection?.date === date && activeSelection?.name === recipeName) {
			activeSelection = null;
		} else {
			activeSelection = { date, name: recipeName };
		}
	}
</script>

<svelte:head>
	<title>Herremad</title>
</svelte:head>

<div class="herremad-container">
	<header class="page-header">
		<div class="title-row">
			<h1>Herremad</h1>
			<label class="year-selector">
				<span class="year-label">År</span>
				<select class="year-select" bind:value={selectedYear} aria-label="Vælg år">
					{#each years as year (year)}
						<option value={year}>{year}</option>
					{/each}
				</select>
			</label>
		</div>
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
					{#each menu.recipes as recipe (recipe.name + recipe.type)}
						<li class="dish-item">
							<span class="dish-type type-{recipe.type}">
								{typeLabels[recipe.type] ?? recipe.type}
							</span>
							<button
								class="dish-name"
								type="button"
								aria-expanded={activeSelection?.date === menu.date &&
									activeSelection?.name === recipe.name}
								onclick={() => toggleRecipe(recipe.name, menu.date)}
							>
								{recipe.name}
							</button>
						</li>
					{/each}
				</ul>

				{#if activeSelection?.date === menu.date}
					<div class="recipe-card-wrapper" aria-live="polite">
						<div class="recipe-card-header">
							<button
								class="recipe-close"
								type="button"
								aria-label="Luk opskrift"
								onclick={() => (activeSelection = null)}
							>
								Luk <span aria-hidden="true">✕</span>
							</button>
						</div>

						{#if selectedRecipe}
							<RecipeCard recipe={selectedRecipe} />
						{:else}
							<div class="recipe-fallback">
								<h2 class="fallback-title">{activeSelection.name}</h2>
								<p>Desværre er der ingen opskrift tilgængelig for denne ret endnu.</p>
							</div>
						{/if}
					</div>
				{/if}
			</article>
		{/each}
	</div>
</div>

<style>
	.herremad-container {
		max-width: 800px;
		margin: 0 auto;
		padding: 2rem 1rem;
		display: flex;
		flex-direction: column;
		gap: 2rem;
	}

	.page-header {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	.title-row {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 1rem;
	}

	h1 {
		font-size: 2rem;
		font-weight: 800;
		color: var(--text);
		margin: 0;
	}

	.year-selector {
		display: flex;
		align-items: center;
		gap: 0.5rem;
	}

	.year-label {
		font-size: 0.9rem;
		font-weight: 600;
		color: var(--text-muted);
	}

	.year-select {
		background: var(--surface);
		border: 1px solid var(--border);
		color: var(--text);
		padding: 0.4rem 0.8rem;
		border-radius: 8px;
		font-size: 0.95rem;
		font-weight: 600;
		cursor: pointer;
	}

	.intro-text {
		color: var(--text-muted);
		margin: 0;
		font-size: 0.95rem;
	}

	.menu-list {
		display: flex;
		flex-direction: column;
		gap: 1.5rem;
	}

	.menu-card {
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: 12px;
		padding: 1.25rem;
		box-shadow: 0 2px 8px var(--shadow);
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.menu-date {
		font-weight: 700;
		font-size: 1.1rem;
		color: var(--text);
		text-transform: capitalize;
	}

	.dish-list {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}

	.dish-item {
		display: flex;
		align-items: center;
		gap: 0.75rem;
	}

	.dish-type {
		font-size: 0.75rem;
		font-weight: 700;
		text-transform: uppercase;
		padding: 0.2rem 0.5rem;
		border-radius: 4px;
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
		background: none;
		border: none;
		padding: 0;
		font-size: 1rem;
		font-weight: 600;
		color: var(--text);
		cursor: pointer;
		text-align: left;
	}

	.dish-name:hover {
		color: var(--accent-2);
	}

	.recipe-card-wrapper {
		margin-top: 1rem;
		padding-top: 1rem;
		border-top: 1px solid var(--border);
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
		width: 100%;
		box-sizing: border-box;
	}

	.recipe-card-header {
		display: flex;
		justify-content: flex-end;
	}

	.recipe-close {
		background: var(--surface-2, #f3f4f6);
		border: 1px solid var(--border);
		color: var(--text);
		font-size: 0.85rem;
		font-weight: 600;
		padding: 0.3rem 0.75rem;
		border-radius: 999px;
		cursor: pointer;
	}

	.recipe-fallback {
		padding: 1.5rem;
		background: var(--surface-2, #f9fafb);
		border-radius: 12px;
		text-align: center;
	}

	.fallback-title {
		font-size: 1.2rem;
		margin: 0 0 0.5rem;
	}
</style>
