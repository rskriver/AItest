<script lang="ts">
	import recipes from '$lib/recipes.json';
	import RecipeCard from './RecipeCard.svelte';

	const menu = $derived(recipes.menu);
	const menuDate = $derived(
		new Date(menu.date).toLocaleDateString('da-DK', {
			day: 'numeric',
			month: 'long',
			year: 'numeric'
		})
	);
</script>

<svelte:head>
	<title>Herremad</title>
</svelte:head>

<div class="herremad-container">
	<header class="page-header">
		<h1>{menu.title}</h1>
		<p class="intro-text">
			Our homemade dishes, made with care and quality.
			<span class="menu-date">Menu: {menuDate}</span>
		</p>
	</header>

	<div class="recipe-grid">
		{#each menu.dishes as dish (dish.id)}
			<RecipeCard {dish} />
		{/each}
	</div>
</div>

<style>
	.herremad-container {
		max-width: 1200px;
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
	}

	.menu-date {
		display: block;
		margin-top: 0.5rem;
		font-size: 0.95rem;
		font-weight: 600;
		color: var(--accent-2);
	}

	.recipe-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
		gap: 2rem;
	}
</style>
