<script lang="ts">
	import CrudComponent from '../components/CrudComponent.svelte';
	import Counter from '../components/Counter.svelte';
</script>

<main class="page">
	<section class="hero">
		<span class="eyebrow">Svelte 5 · SvelteKit</span>
		<h1>Welcome to SvelteKit</h1>
		<p class="lede">
			A fast, modern starter built with Svelte 5 runes. Explore the components below, or read the
			full documentation at
			<a href="https://svelte.dev/docs/kit" target="_blank" rel="noreferrer">svelte.dev/docs/kit</a
			>.
		</p>
	</section>

	<section class="grid">
		<article class="card">
			<header class="card-head">
				<h2>Counter</h2>
				<p>Track a value with increment, decrement and reset.</p>
			</header>
			<Counter label="Visits" initialCount={0} step={1} min={0} max={100} />
		</article>

		<article class="card card--wide">
			<header class="card-head">
				<h2>Items</h2>
				<p>Add and remove items from a live list.</p>
			</header>
			<CrudComponent />
		</article>
	</section>
</main>

<style>
	.page {
		max-width: 1100px;
		margin: 0 auto;
		padding: 2rem 1.5rem 4rem;
	}

	.hero {
		text-align: center;
		margin-bottom: 3rem;
	}

	.eyebrow {
		display: inline-block;
		padding: 0.35rem 0.9rem;
		font-size: 0.8rem;
		font-weight: 600;
		letter-spacing: 0.08em;
		text-transform: uppercase;
		color: var(--accent);
		background: rgba(231, 76, 60, 0.1);
		border: 1px solid rgba(231, 76, 60, 0.25);
		border-radius: 999px;
		margin-bottom: 1.25rem;
	}

	.hero h1 {
		font-size: clamp(2.25rem, 5vw, 3.5rem);
		font-weight: 800;
		letter-spacing: -0.02em;
		margin: 0 0 1rem;
		background: linear-gradient(135deg, var(--heading-1), var(--heading-2));
		-webkit-background-clip: text;
		background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.lede {
		max-width: 620px;
		margin: 0 auto;
		font-size: 1.1rem;
		line-height: 1.6;
		color: var(--text-muted);
	}

	.lede a {
		color: var(--text);
		font-weight: 600;
		text-decoration: none;
		border-bottom: 2px solid rgba(231, 76, 60, 0.5);
		transition: border-color 0.2s ease;
	}

	.lede a:hover {
		border-color: var(--accent);
	}

	.grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
		gap: 1.5rem;
	}

	.card {
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
		padding: 1.75rem;
		background: var(--surface);
		border: 1px solid var(--border);
		border-radius: 16px;
		box-shadow: 0 10px 30px var(--shadow);
		transition:
			box-shadow 0.25s ease,
			transform 0.25s ease;
	}

	.card:hover {
		box-shadow: 0 16px 40px var(--shadow-strong);
		transform: translateY(-2px);
	}

	.card-head h2 {
		margin: 0 0 0.35rem;
		font-size: 1.4rem;
		font-weight: 700;
		color: var(--text);
	}

	.card-head p {
		margin: 0;
		font-size: 0.95rem;
		color: var(--text-muted);
	}
</style>
