<script lang="ts">
    import { onMount } from 'svelte';
    import { Range, Ranges, Positions, Actions, StackSizes } from '$lib/utils/range';
    import RangeGrid from '$lib/components/RangeGrid.svelte';
    import RangeSelector from '$lib/components/RangeSelector.svelte';

    let selectedPosition: string = 'SB';
    let selectedAction: string = 'RFI';
    let selectedStackSize: string = '30bb';
    let range: Range | null = null;

    const positions = Positions;
    const actions = Actions;
    const stackSizes = StackSizes;

    const handleSelectPosition = async (event: CustomEvent<string>) => {
        selectedPosition = event.detail;
        await reload();
    }

    const handleSelectAction = async (event: CustomEvent<string>) => {
        selectedAction = event.detail;
        await reload();
    }

    const handleSelectStackSize = async (event: CustomEvent<string>) => {
        selectedStackSize = event.detail;
        await reload();
    }

    const getRangeString = () => {
        return selectedPosition.toLowerCase() + '_' +
               selectedAction.toLowerCase() + '_' +
               selectedStackSize.toLowerCase();
    }

    const isConfigValid = () => {
        let rangeString = getRangeString();
        return Ranges.includes(rangeString)
    }

    const reload = async () => {
        if (isConfigValid())
            range = await Range.create(getRangeString());
        else
            range = null;
    }

    onMount(async () => {
        range = await Range.create('sb_rfi_30bb');
    });
</script>

<main>
    <RangeSelector items={positions} on:select={handleSelectPosition} selected={selectedPosition} />
    <RangeSelector items={actions} on:select={handleSelectAction} selected={selectedAction} />
    <RangeSelector items={stackSizes} on:select={handleSelectStackSize} selected={selectedStackSize} />
    {#if range}
        {#key range.name()} <RangeGrid {range} /> {/key}
    {:else if !isConfigValid()}
        <p>Invalid range</p>
    {:else}
        <p>Loading range...</p>
    {/if}
</main>

<style>
    main {
        padding: 30px;
    }
</style>
