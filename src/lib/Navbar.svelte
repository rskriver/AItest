<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/state';

	const links = [
		{ label: 'Home', labelDa: 'Hjem', sub: 'Start Here', path: '/' },
		{ label: 'Shop', labelDa: 'Butik', sub: 'Browse Items', path: '/shop' },
		{ label: 'About', labelDa: 'Om os', sub: 'Browse Items', path: '/about' }
	];

	function navigate(path: string) {
		goto(path);
	}
</script>

<div id="nav">
	<ul class="nav-menu">
		{#each links as link (link.path)}
			<li>
				<a
					href={link.path}
					class="three-d"
					class:active={page.url.pathname === link.path}
					onclick={(e) => {
						e.preventDefault();
						navigate(link.path);
					}}
				>
					{link.label}
					<span class="three-d-box"
						><span class="front">{link.label}</span><span class="back">{link.labelDa}</span></span
					>
				</a>
			</li>
		{/each}
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

	/* animation domination */
	.three-d {
		perspective: 200px;
		transition: all 0.07s linear;
		position: relative;
	}

	.three-d:not(.active):hover {
		cursor: pointer;
	}

	.three-d:not(.active):hover .three-d-box,
	.three-d:not(.active):focus .three-d-box {
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
	}
</style>
