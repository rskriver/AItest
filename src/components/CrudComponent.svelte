<script lang="ts">
	type Item = {
		id: number;
		name: string;
		description: string;
	};

	let items = $state<Item[]>([
		{ id: 1, name: 'Item 1', description: 'Description of item 1' },
		{ id: 2, name: 'Item 2', description: 'Description of item 2' }
	]);

	let newId = $state(3);
	let newName = $state('');
	let newDescription = $state('');

	const isValid = $derived(newName.trim().length > 0);

	function addItem() {
		if (isValid) {
			items = [
				...items,
				{
					id: newId++,
					name: newName,
					description: newDescription
				}
			];
			newName = '';
			newDescription = '';
		}
	}

	function deleteItem(id: number) {
		items = items.filter((item) => item.id !== id);
	}
</script>

<div class="crud-container">
	<form
		class="form"
		onsubmit={(e) => {
			e.preventDefault();
			addItem();
		}}
	>
		<input type="text" placeholder="Item name" bind:value={newName} aria-label="Item name" />
		<input
			type="text"
			placeholder="Item description"
			bind:value={newDescription}
			aria-label="Item description"
		/>
		<button type="submit" disabled={!isValid}>Add Item</button>
	</form>

	<div class="items">
		{#if items.length === 0}
			<p class="empty">No items yet. Add one above.</p>
		{:else}
			{#each items as item (item.id)}
				<div class="item">
					<div class="item-text">
						<h3>{item.name}</h3>
						{#if item.description}<p>{item.description}</p>{/if}
					</div>
					<button onclick={() => deleteItem(item.id)} aria-label="Delete {item.name}">Delete</button
					>
				</div>
			{/each}
		{/if}
	</div>
</div>

<style>
	.crud-container {
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
		width: 100%;
	}

	.form {
		display: flex;
		flex-wrap: wrap;
		gap: 0.6rem;
	}

	.form input {
		flex: 1 1 180px;
		padding: 0.7rem 0.9rem;
		font-size: 1rem;
		color: var(--text);
		border: 1px solid var(--border);
		border-radius: 8px;
		background: var(--surface);
		transition:
			border-color 0.2s ease,
			box-shadow 0.2s ease;
	}

	.form input:focus {
		outline: none;
		border-color: var(--accent);
		box-shadow: 0 0 0 3px rgba(231, 76, 60, 0.18);
	}

	.form button {
		padding: 0.7rem 1.25rem;
		background: #e74c3c;
		color: white;
		border: none;
		border-radius: 8px;
		cursor: pointer;
		font-weight: 600;
		font-size: 1rem;
		transition:
			background 0.2s ease,
			transform 0.1s ease;
	}

	.form button:hover:not(:disabled) {
		background: #c0392b;
	}

	.form button:active:not(:disabled) {
		transform: scale(0.97);
	}

	.form button:disabled {
		opacity: 0.4;
		cursor: not-allowed;
	}

	.items {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
		max-height: 60vh;
		overflow-y: auto;
		padding-right: 0.25rem;
	}

	.empty {
		margin: 0;
		padding: 1.5rem;
		text-align: center;
		color: var(--text-muted);
		font-size: 0.95rem;
		border: 1px dashed var(--border);
		border-radius: 10px;
	}

	.item {
		border: 1px solid var(--border);
		padding: 1rem;
		border-radius: 10px;
		background: var(--surface);
		display: flex;
		justify-content: space-between;
		align-items: center;
		gap: 1rem;
		transition:
			border-color 0.2s ease,
			box-shadow 0.2s ease;
	}

	.item:hover {
		border-color: var(--text-muted);
		box-shadow: 0 4px 12px var(--shadow);
	}

	.item-text h3 {
		margin: 0 0 0.25rem 0;
		font-size: 1.1rem;
		font-weight: 600;
		color: var(--text);
	}

	.item-text p {
		margin: 0;
		font-size: 0.95rem;
		color: var(--text-muted);
	}

	.item button {
		flex-shrink: 0;
		padding: 0.5rem 1rem;
		font-size: 0.9rem;
		background: transparent;
		color: #ef4444;
		border: 1px solid rgba(239, 68, 68, 0.4);
		border-radius: 8px;
		cursor: pointer;
		transition:
			background 0.2s ease,
			color 0.2s ease;
	}

	.item button:hover {
		background: #ef4444;
		color: white;
	}
</style>
