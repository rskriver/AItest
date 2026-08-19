<script lang="ts">
	// Modern props via $props() with default values
	let {
		initialCount = 0,
		step = 1,
		min = -Infinity,
		max = Infinity,
		label = 'Count'
	}: {
		initialCount?: number;
		step?: number;
		min?: number;
		max?: number;
		label?: string;
	} = $props();

	// Reactive state via $state()
	let count = $state(initialCount);

	// Derived values via $derived()
	const isAtMin = $derived(count <= min);
	const isAtMax = $derived(count >= max);
	const status = $derived.by(() => {
		if (count > 0) return 'positive';
		if (count < 0) return 'negative';
		return 'zero';
	});

	// Side effects via $effect() — runs when `count` changes
	$effect(() => {
		console.debug(`[Counter] ${label} is now ${count} (${status})`);
	});

	function increment() {
		count = Math.min(count + step, max);
	}

	function decrement() {
		count = Math.max(count - step, min);
	}

	function reset() {
		count = initialCount;
	}
</script>

<div class="counter">
	<h2>{label}</h2>

	<div class="display {status}">{count}</div>

	<div class="controls">
		<button onclick={decrement} disabled={isAtMin} aria-label="Decrement">−</button>
		<button onclick={reset} aria-label="Reset">Reset</button>
		<button onclick={increment} disabled={isAtMax} aria-label="Increment">+</button>
	</div>
</div>

<style>
	.counter {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 1rem;
		padding: 2rem;
		min-width: 220px;
		background: #fafafa;
		border: 1px solid #e5e7eb;
		border-radius: 12px;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
	}

	h2 {
		margin: 0;
		font-size: 1.5vw;
		color: #1f2937;
	}

	.display {
		font-size: 3vw;
		font-weight: 700;
		font-variant-numeric: tabular-nums;
		transition: color 0.2s ease;
	}

	.display.positive {
		color: #16a34a;
	}

	.display.negative {
		color: #dc2626;
	}

	.display.zero {
		color: #6b7280;
	}

	.controls {
		display: flex;
		gap: 0.75rem;
	}

	button {
		padding: 0.6rem 1.1rem;
		font-size: 1.2vw;
		border: none;
		border-radius: 6px;
		cursor: pointer;
		font-weight: 600;
		transition:
			background 0.2s ease,
			transform 0.1s ease;
	}

	button:active:not(:disabled) {
		transform: scale(0.95);
	}

	button:disabled {
		opacity: 0.4;
		cursor: not-allowed;
	}

	.controls button:first-child,
	.controls button:last-child {
		background: #2563eb;
		color: white;
	}

	.controls button:first-child:hover:not(:disabled),
	.controls button:last-child:hover:not(:disabled) {
		background: #1d4ed8;
	}

	.controls button:nth-child(2) {
		background: #6b7280;
		color: white;
	}

	.controls button:nth-child(2):hover:not(:disabled) {
		background: #4b5563;
	}
</style>
