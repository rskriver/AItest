<script lang="ts">
</script>

<svelte:head>
	<title>About</title>
</svelte:head>

<div class="about-container">
	<h1>About Us</h1>

	<p class="intro-text">Learn more about who we are and what we do.</p>

	<div class="about-section">
		<p>
			We are a team passionate about building fast, modern web experiences. Our focus is on
			quality, performance, and delightful user interactions.
		</p>
	</div>
</div>

<style>
	.about-container {
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

	.about-section {
		padding: 4rem 2rem;
		background: linear-gradient(135deg, #f9fafb, #f3f4f6);
		border-radius: 12px;
	}

	.about-section p {
		color: #6b7280;
		font-size: 1.1rem;
		line-height: 1.6;
	}
</style>
