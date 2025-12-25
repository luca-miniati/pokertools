<script lang="ts">
  import { RANKS, getHandLabel } from "$lib/utils/hands";

  export let range: Record<string, number> = {};
  export let highlightAction = "open";

  function freq(hand: string): number {
    return range[hand] ?? 0;
  }

  function cellColor(f: number): string {
    if (f === 0) return "#1e1e1e";
    if (f < 0.25) return "#355070";
    if (f < 0.5) return "#6d597a";
    if (f < 0.75) return "#b56576";
    return "#e56b6f";
  }
</script>

<div class="grid">
  {#each RANKS as row}
    {#each RANKS as col}
      {#key row + col}
        {#let hand = getHandLabel(row, col)}
          <div
            class="cell"
            style="background-color: {cellColor(freq(hand))}"
            title="{hand}: {Math.round(freq(hand) * 100)}%"
          >
            <span class="hand">{hand}</span>
            {#if freq(hand) > 0}
              <span class="freq">{Math.round(freq(hand) * 100)}%</span>
            {/if}
          </div>
        {/let}
      {/key}
    {/each}
  {/each}
</div>

<style>
  .grid {
    display: grid;
    grid-template-columns: repeat(13, 1fr);
    gap: 2px;
    max-width: 520px;
  }

  .cell {
    position: relative;
    aspect-ratio: 1;
    font-size: 10px;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: default;
  }

  .hand {
    font-weight: bold;
  }

  .freq {
    font-size: 9px;
    opacity: 0.85;
  }
</style>
