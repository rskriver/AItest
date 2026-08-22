<script lang="ts">
	import { browser } from '$app/environment';
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import Navbar from '$lib/Navbar.svelte';

	let { children } = $props();

	type Theme = 'light' | 'dark';

	const getInitialTheme = (): Theme => {
		if (!browser) return 'light';
		const stored = localStorage.getItem('theme');
		if (stored === 'light' || stored === 'dark') return stored;
		return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
	};

	let theme = $state<Theme>(getInitialTheme());

	$effect(() => {
		document.documentElement.dataset.theme = theme;
		localStorage.setItem('theme', theme);
	});

	function toggleTheme() {
		theme = theme === 'dark' ? 'light' : 'dark';
	}
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="layout">
	<Navbar {theme} onToggle={toggleTheme} />

	{@render children()}
</div>

<style>
	.layout {
		min-height: 100vh;
		padding-top: 5.5rem;
	}
</style>
