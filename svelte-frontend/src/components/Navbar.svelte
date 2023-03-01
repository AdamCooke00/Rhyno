<script>
  import { Nav, NavItem, NavLink } from "sveltestrap";
  export let handlePageClick;
</script>

<Nav vertical>
  <img class="rhyno-logo" src="./images/rhyno.png" alt="Not Found" />
  <!-- <div class="nav-item">
    <NavItem>
      <NavLink class="box-link" on:click={() => handlePageClick("page2")}>
        Monitor
      </NavLink>
    </NavItem>
  </div> -->
  <div class="nav-item">
    <NavItem>
      <NavLink class="box-link" on:click={() => handlePageClick("page2")}
        >Dashboard</NavLink
      >
    </NavItem>
  </div>
</Nav>

<style>
  .nav-item {
    padding: 10px 0;
  }

  :global(.box-link),
  :global(.box-link:visited),
  :global(.box-link:link) {
    text-decoration: none;
    color: white;
  }

  :global(.box-link:hover),
  :global(.box-link:active) {
    background-color: #cbe4de;
    font-weight: 600;
  }
  .rhyno-logo {
    height: 75px;
    width: 100px;
    margin: auto;
    padding-top: 10px;
  }
</style>
