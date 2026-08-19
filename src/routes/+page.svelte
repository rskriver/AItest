<script>
	import CrudComponent from '../components/CrudComponent.svelte';
	import Counter from '../components/Counter.svelte';
</script>

<div class="header">
	<h1>Welcome to SvelteKit</h1>
	<p>
		Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation
	</p>
</div>

<div class="center-crud">
	<Counter label="Visits" initialCount={0} step={1} min={0} max={100} />
	<CrudComponent />
</div>

<style>
	.header {
		text-align: left;
	}

	h1 {
		text-align: center;
		font-size: 3vw;
	}

	p {
		text-align: left;
		font-size: 1.5vw;
	}

	p a {
		font-size: 1.5vw;
	}

	.center-crud {
		display: flex;
		justify-content: center;
		gap: 2rem;
	}
</style>