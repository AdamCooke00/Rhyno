<script>
  import "fluent-svelte/theme.css";
  import { Col, Container, Row, Breadcrumb, BreadcrumbItem } from "sveltestrap";

  
  import Clock from "../components/Clock.svelte";

  import Light from "../components/Light.svelte";
  import {setLight1,setLight2,sendPostOff,sendPostOn} from './dashboard.js'
  export let title;

</script>

<main>
  <Clock />
  <Row><h1>{title}!</h1></Row>

  <button on:click={sendPostOn}>Smart Plug ON</button>
  <button on:click={sendPostOff}>Smart Plug OFF</button>
  <section>class = "video"</section>
  <Row>
    <Col><Light lightName="Smart Light 1" setLight={setLight1} /></Col>
    <Col><Light lightName="Smart Light 2" setLight={setLight2} /></Col>
    <!-- <button on:click={setLight1Off}>Light  Off</button> -->
    <!-- <button on:click={getTemp}>Get Temperature and Humidity</button> -->
  </Row>
</main>

<style>
  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }
</style>
