<script lang="ts">
import { selectedRange } from '$lib/stores/rangeStore';
</script>

{#if $selectedRange}
    {$selectedRange.name()}
{:else}
    Select a range
{/if}
