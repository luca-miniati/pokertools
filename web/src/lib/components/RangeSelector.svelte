<script lang="ts">
    import { createEventDispatcher, onMount, onDestroy } from 'svelte';
    import { browser } from '$app/environment';

    export let items: string[] = [];
    export let selected: string | null = null;

    const dispatch = createEventDispatcher();
    let isOpen = false;

    const toggleDropdown = () => {
        isOpen = !isOpen;
    }

    const selectItem = (item: string) => {
        selected = item;
        isOpen = false;
        dispatch('select', item);
    }

    let dropdownEl: HTMLElement;

    onMount(() => {
        if (!browser) return;

        const handleClickOutside = (event: MouseEvent) => {
            if (dropdownEl && !dropdownEl.contains(event.target as Node)) {
                isOpen = false;
            }
        };

        document.addEventListener('click', handleClickOutside);
        onDestroy(() => document.removeEventListener('click', handleClickOutside));
    });
</script>


<div class="dropdown" bind:this={dropdownEl}>
    <button on:click={toggleDropdown}>
        {#if selected}<h2>{selected}</h2>{/if}
    </button>
    {#if isOpen}
        <ul>
            {#each items as item}
                <li><button on:click={() => selectItem(item)}><h2>{item}</h2></button></li>
            {/each}
        </ul>
    {/if}
</div>

<style>
    .dropdown {
        position: relative;
        display: inline-block;
        z-index: 2;
        border: 2px solid var(--border);
        background: var(--bg-muted);
        min-width: 75px;
    }

    button {
        color: var(--fg);
        background: var(--bg-muted);
        border: none;
    }

    ul {
        position: absolute;
        top: 100%;
        left: -2px;
        margin: 0;
        padding: 0;
        list-style: none;
        border: 2px solid var(--border);
        background: var(--bg-muted);
        min-width: 75px;
    }

    button {
        padding: 4px;
        width: 100%;
        border: none;
        background: none;
        text-align: center;
    }

    button h2 {
        margin: 10px;
    }

    li button:hover {
        background: var(--fg-muted);
    }
</style>

