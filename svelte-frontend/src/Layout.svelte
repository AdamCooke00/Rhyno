<script>
  import Dashboard2 from "./pages/Dashboard2.svelte";
  import Dashboard from "./pages/Dashboard.svelte";
  import Navbar from "./components/Navbar.svelte";

  
  // Code to handle the "navigation" by loading the right column with the corresponding page svelte component
  // Essentially is a muti-page SPA
  let page1 = false;
  let page2 = true;

  function handlePageClick(pageName) {
    if(pageName == "page1"){
      page1 = true;
      page2 = false;
    }
    else if(pageName == "page2"){
      page2 = true;
      page1 = false;
    }
  }
</script>

<div class="container">
  <div class="left-column">
    <Navbar {handlePageClick} />
  </div>

  <div class="right-column">
    {#if page1}
      <Dashboard title="Rhyno Smart Home!" />
    {/if}
    {#if page2}
      <Dashboard2 />
    {/if}
  </div>
</div>

<style>
  .left-column {
    width: 11%;
    min-height: 100vh;
    background-color: rgba(93, 151, 185, 0.665); 
  }
  .right-column {
    width: 85%;
    padding: 10px 30px;
  }
  .container {
    padding-left: 0;
    padding-right: 0;
    display: flex;
    max-width: none;
    flex-wrap: wrap;
  }

  @media (max-width: 768px) {
    .left-column,
    .right-column {
      width: 100%;
      height: 100%;
      min-height: auto;
    }
  }
</style>
