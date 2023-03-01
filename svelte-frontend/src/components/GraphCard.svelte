<script>
  import { Card, CardBody, CardHeader, CardText } from "sveltestrap";
  import LineGraph from "./LineGraph.svelte";

  export let graphTitle = "";

  export let currHum;
  export let currTemp;
  
</script>

<Card class="mb-4" color="light" style="position:relative; height:72.5%">
  <CardHeader>
    <CardText class = "title">{graphTitle}</CardText>
  </CardHeader>
  <CardBody>
    <LineGraph bind:currHum={currHum} bind:currTemp={currTemp}/>
  </CardBody>
</Card>

<style>
  :global(.title){
    color: black;
    font-size: x-large;
  }

</style>
