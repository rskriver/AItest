<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/state';
</script>

<div class="shop-container">
	<h1>Our Shop</h1>

	<p class="intro-text">Browse our collection of premium products.</p>

	<!-- Placeholder for future product grid -->
	<div class="placeholder-section">
		<div class="placeholder-icon">📦</div>
		<p>Products will appear here...</p>
	</div>
</div>

<style>
	.shop-container {
		max-width: 800px;
		margin: 0 auto;
		padding: 3rem 1.5rem;
		text-align: center;
		min-height: calc(100vh - 120px);
	}

	h1 {
		font-size: 3rem;
		font-weight: 800;
		margin-bottom: 1rem;
		background: linear-gradient(135deg, var(--heading-1), var(--heading-2));
		background-clip: text;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		color: transparent;
	}

	.intro-text {
		font-size: 1.25rem;
		color: var(--text-muted);
		margin-bottom: 3rem;
	}

	.placeholder-section {
		padding: 4rem 2rem;
		background: var(--surface-2);
		border: 1px solid var(--border);
		border-radius: 12px;
	}

	.placeholder-icon {
		font-size: 4rem;
		margin-bottom: 1rem;
	}

	.placeholder-section p {
		color: var(--text-muted);
		font-size: 1.1rem;
	}
</style>
