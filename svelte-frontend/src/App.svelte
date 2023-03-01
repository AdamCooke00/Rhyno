<script>
  import Layout from "./Layout.svelte";
  export let title;
</script>

<div>
  <Layout {title} />
</div>

<style>
  div {
    text-align: center;
    background-color: #2c3333;
    margin: 0;
    padding: 0;
  }
</style>
