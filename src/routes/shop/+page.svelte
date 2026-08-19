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
		background: linear-gradient(135deg, #1f2937, #4b5563);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}

	.intro-text {
		font-size: 1.25rem;
		color: #6b7280;
		margin-bottom: 3rem;
	}

	.placeholder-section {
		padding: 4rem 2rem;
		background: linear-gradient(135deg, #f9fafb, #f3f4f6);
		border-radius: 12px;
	}

	.placeholder-icon {
		font-size: 4rem;
		margin-bottom: 1rem;
	}

	.placeholder-section p {
		color: #9ca3af;
		font-size: 1.1rem;
	}
</style>