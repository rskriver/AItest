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
	<div class="display {status}" aria-live="polite">{count}</div>

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
		gap: 1.25rem;
		padding: 1.75rem;
		background: linear-gradient(160deg, #f9fafb, #f3f4f6);
		border: 1px solid #e5e7eb;
		border-radius: 14px;
	}

	.display {
		font-size: 3.5rem;
		font-weight: 800;
		line-height: 1;
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
		font-size: 1rem;
		border: none;
		border-radius: 8px;
		cursor: pointer;
		font-weight: 600;
		transition:
			background 0.2s ease,
			transform 0.1s ease,
			box-shadow 0.2s ease;
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
		background: #2c3e50;
		color: white;
		box-shadow: 0 4px 12px rgba(44, 62, 80, 0.25);
	}

	.controls button:first-child:hover:not(:disabled),
	.controls button:last-child:hover:not(:disabled) {
		background: #1f2d3a;
	}

	.controls button:nth-child(2) {
		background: #e74c3c;
		color: white;
		box-shadow: 0 4px 12px rgba(231, 76, 60, 0.25);
	}

	.controls button:nth-child(2):hover:not(:disabled) {
		background: #c0392b;
	}
</style>
