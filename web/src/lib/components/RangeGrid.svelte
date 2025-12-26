<script lang="ts">
    import RangeCell from './RangeCell.svelte';
    import { RANKS } from '$lib/utils/range';
    import type { Range, HandAction } from '$lib/utils/range';

    export let range: Range;
</script>

<div class="grid">
    {#each RANKS as row}
        {#each RANKS as col}
            <RangeCell {row} {col} {range} />
        {/each}
    {/each}
</div>

<style>
    .grid {
        display: grid;
        grid-template-columns: repeat(13, 1fr);
        gap: 3px;
        max-width: 1000px;
        padding-top: 30px;
    }
</style>
