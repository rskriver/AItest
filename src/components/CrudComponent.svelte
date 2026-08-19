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
	<h2>Love is in the air</h2>
	<div class="form">
		<input type="text" placeholder="Item name" bind:value={newName} />
		<input type="text" placeholder="Item description" bind:value={newDescription} />
		<button onclick={addItem} disabled={!isValid}>Add Item</button>
	</div>

	<div class="items">
		{#each items as item (item.id)}
			<div class="item">
				<h3>{item.name}</h3>
				<p>{item.description}</p>
				<button onclick={() => deleteItem(item.id)}>Delete</button>
			</div>
		{/each}
	</div>
</div>

<style>
	.crud-container {
		max-width: 50vw;
		width: 100%;
		min-width: 320px;
		padding: 2rem;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
		border-radius: 8px;
		background: #fafafa;
	}

	.form {
		display: flex;
		gap: 0.5rem;
		margin-bottom: 1.5rem;
	}

	.form input {
		flex: 1;
		padding: 0.8rem;
		font-size: 1.2vw;
		border: 1px solid #ddd;
		border-radius: 4px;
	}

	.form button {
		padding: 0.8rem 1.2rem;
		background: #2563eb;
		color: white;
		border: none;
		border-radius: 4px;
		cursor: pointer;
		font-weight: 500;
		font-size: 1.2vw;
		transition: background 0.2s;
	}

	.form button:hover {
		background: #1d4ed8;
	}

	.items {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
		max-height: 60vh;
		overflow-y: auto;
	}

	.item {
		border: 1px solid #e5e7eb;
		padding: 1rem;
		border-radius: 6px;
		background: white;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.item h3 {
		margin: 0 0 0.25rem 0;
		font-size: 1.4vw;
		color: #1f2937;
	}

	.item p {
		margin: 0;
		font-size: 1.2vw;
		color: #6b7280;
	}

	.item button {
		padding: 0.6rem 1rem;
		font-size: 1.2vw;
		background: #ef4444;
		color: white;
		border: none;
		border-radius: 4px;
		cursor: pointer;
		transition: background 0.2s;
	}

	.item button:hover {
		background: #dc2626;
	}

	h2 {
		font-size: 2.5vw;
	}
</style>
