<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/state';

	const links = [
		{ label: 'Home', labelDa: 'Hjem', sub: 'Start Here', path: '/' },
		{ label: 'Shop', labelDa: 'Butik', sub: 'Browse Items', path: '/shop' }
	];

	function navigate(path: string) {
		goto(path);
	}
</script>

<nav class="nav-bar">
	{#each links as link (link.path)}
		<a
			class="scene"
			class:active={page.url.pathname === link.path}
			href={link.path}
			onclick={(e) => {
				e.preventDefault();
				navigate(link.path);
			}}
		>
			<span class="cube">
				<span class="face face-front">{link.label}</span>
				<span class="face face-bottom">{link.sub}</span>
				<span class="face face-back"></span>
				<span class="face face-top">{link.labelDa}</span>
				<span class="face face-left"></span>
				<span class="face face-right"></span>
			</span>
		</a>
	{/each}
</nav>

<style>
	.nav-bar {
		position: fixed;
		top: 1.25rem;
		left: 50%;
		transform: translateX(-50%);
		display: flex;
		align-items: center;
		gap: 0.75rem;
		z-index: 100;
	}

	.scene {
		width: 54px;
		/* Height in em so top/bottom padding scales with the text size */
		font-size: 1vw;
		height: 1.88em;
		perspective: 600px;
		display: block;
	}

	.cube {
		width: 100%;
		height: 100%;
		position: relative;
		display: block;
		transform-style: preserve-3d;
		transition: transform 0.4s ease-in-out;
		/* Resting tilt so the 3D box shape is visible even without hover */
		transform: rotateX(-22deg);
	}

	.scene:hover .cube {
		transform: rotateX(-90deg);
	}

	.face {
		position: absolute;
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		color: #fff;
		font-weight: bold;
		text-decoration: none;
		text-transform: uppercase;
		font-size: 1vw;
		letter-spacing: 1px;
		border-radius: 4px;
		box-sizing: border-box;
		backface-visibility: hidden;
	}

	.face-front {
		background-color: #2c3e50;
		transform: translateZ(0.94em);
	}

	.face-bottom {
		background-color: #e74c3c;
		transform: rotateX(-90deg) translateZ(-0.94em);
	}

	.face-back {
		background-color: #2c3e50;
		transform: rotateY(180deg) translateZ(0.94em);
	}

	.face-top {
		background-color: #2c3e50;
		transform: rotateX(90deg) translateZ(0.94em);
	}

	.face-left {
		background-color: #243342;
		transform: rotateY(-90deg) translateZ(27px);
	}

	.face-right {
		background-color: #243342;
		transform: rotateY(90deg) translateZ(27px);
	}

	.scene.active .face-front,
	.scene.active .face-top {
		background-color: #e74c3c;
	}

	@media (max-width: 480px) {
		.nav-bar {
			top: 1rem;
		}

		.scene {
			width: 42px;
		}
	}
</style>
