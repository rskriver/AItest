<script lang="ts">
	import { page } from '$app/state';
	import { resolve } from '$app/paths';

	type RoutePath = '/' | '/shop' | '/herremad' | '/about';

	let {
		theme = 'light',
		onToggle = () => {}
	}: {
		theme?: 'light' | 'dark';
		onToggle?: () => void;
	} = $props();

	const links: { label: string; labelDa: string; sub: string; path: RoutePath }[] = [
		{ label: 'Home', labelDa: 'Hjem', sub: 'Start Here', path: '/' },
		{ label: 'Shop', labelDa: 'Butik', sub: 'Browse Items', path: '/shop' },
		{ label: 'Real food', labelDa: 'Herremad', sub: 'Fresh & Homemade', path: '/herremad' },
		{ label: 'About', labelDa: 'Om os', sub: 'Browse Items', path: '/about' }
	];
</script>

<div id="nav">
	<ul class="nav-menu">
		{#each links as link (link.path)}
			<li>
				<a
					href={resolve(link.path)}
					class="three-d"
					class:active={page.url.pathname === link.path}
					data-sveltekit-preload-data="hover"
				>
					{link.label}
					<span class="three-d-box"
						><span class="front">{link.label}</span><span class="back">{link.labelDa}</span></span
					>
				</a>
			</li>
		{/each}
		<li>
			<button
				class="theme-toggle"
				onclick={onToggle}
				aria-label={theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'}
				title={theme === 'dark' ? 'Light mode' : 'Dark mode'}
			>
				{#if theme === 'dark'}
					<svg
						viewBox="0 0 24 24"
						width="20"
						height="20"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
						stroke-linejoin="round"
						aria-hidden="true"
					>
						<circle cx="12" cy="12" r="4"></circle>
						<path
							d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"
						></path>
					</svg>
				{:else}
					<svg
						viewBox="0 0 24 24"
						width="20"
						height="20"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
						stroke-linejoin="round"
						aria-hidden="true"
					>
						<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
					</svg>
				{/if}
			</button>
		</li>
	</ul>
</div>

<style>
	#nav {
		position: fixed;
		top: 1.25rem;
		left: 50%;
		transform: translateX(-50%);
		z-index: 100;
	}

	.nav-menu {
		display: flex;
		gap: 4px;
		margin: 0;
		padding: 4px;
		list-style: none;
		background: #1a252f;
		border-radius: 10px;
		box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
	}

	.nav-menu li a {
		color: #fff;
		display: block;
		text-decoration: none;
		font-family: sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-font-smoothing: antialiased;
		text-transform: capitalize;
		overflow: visible;
		line-height: 20px;
		font-size: 18px;
		padding: 15px 30px 15px 31px;
	}

	.theme-toggle {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 54px;
		height: 50px;
		padding: 0;
		margin: 0;
		background: #2c3e50;
		color: #fff;
		border: 1px solid rgba(255, 255, 255, 0.35);
		border-radius: 6px;
		cursor: pointer;
		transition:
			background 0.2s ease,
			transform 0.1s ease;
	}

	.theme-toggle:hover {
		background: #e74c3c;
	}

	.theme-toggle:active {
		transform: scale(0.94);
	}

	/* animation domination */
	.three-d {
		perspective: 200px;
		transition: all 0.07s linear;
		position: relative;
	}

	.three-d:hover {
		cursor: pointer;
	}

	.three-d:hover .three-d-box,
	.three-d:focus .three-d-box {
		transform: translateZ(-25px) rotateX(90deg);
	}

	.three-d-box {
		transition: all 0.3s ease-out;
		transform: translatez(-25px);
		transform-style: preserve-3d;
		pointer-events: none;
		position: absolute;
		top: 0;
		left: 0;
		display: block;
		width: 100%;
		height: 100%;
	}

	.front {
		transform: rotatex(0deg) translatez(25px);
	}

	.back {
		transform: rotatex(-90deg) translatez(25px);
		color: #fff;
	}

	.front,
	.back {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		height: 100%;
		position: absolute;
		top: 0;
		left: 0;
		background: #2c3e50;
		padding: 15px 30px 15px 31px;
		color: white;
		pointer-events: none;
		box-sizing: border-box;
		white-space: nowrap;
		border-radius: 6px;
		border: 1px solid rgba(255, 255, 255, 0.35);
		box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
	}

	.nav-menu li .active .front,
	.nav-menu li .active .back,
	.nav-menu li a:hover .front,
	.nav-menu li a:hover .back {
		background-color: #e74c3c;
		background-size: 5px 5px;
		background-position:
			0 0,
			30px 30px;
		background-image: linear-gradient(
			45deg,
			#c0392b 25%,
			transparent 25%,
			transparent 75%,
			#c0392b 75%,
			#c0392b
		);
		border-color: rgba(0, 0, 0, 0.45);
		box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.35);
	}
</style>
