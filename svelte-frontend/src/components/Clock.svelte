<!-- lib/Clock.svelte -->
<script lang="ts">
  import { onMount, onDestroy } from "svelte";
  let date = new Date().toLocaleTimeString();
  let interval;

  onMount(() => {
    interval = setInterval(() => {
      date = new Date().toLocaleTimeString();
    }, 1000);
  });

  onDestroy(() => {
    clearInterval(interval);
  });
</script>

<span>{date || ""}</span>

<style>
  span {
    font-family: inherit;
    font-size: inherit;
    padding: 10px 10px;
    color: #ffffff;
    background-color: rgba(71, 97, 126, 0.614);
    border-radius: 2em;
    border: 2px solid rgba(255, 62, 0, 0);
    outline: none;
    width: 50px;
    font-variant-numeric: tabular-nums;
    cursor: pointer;
  }

  span:active {
    background-color: rgba(255, 62, 0, 0.2);
  }
</style>
