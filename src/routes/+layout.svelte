<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import Navbar from '$lib/Navbar.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="layout">
	<Navbar />

	{@render children()}
</div>

<style>
	.layout {
		min-height: 100vh;
		padding-top: 5.5rem;
	}
</style>