<script>
  import { Row } from "sveltestrap";

  import DashboardCard from "../components/DashboardCard.svelte";
  
  import VideoCard from "../components/VideoCard.svelte"
  import {setLight1, setLight2} from './dashboard.js'

</script>

<Row>
  <Row>
    <h1 class="title">Dashboard</h1>
  </Row>
  <Row>
    <div class="col-xl-4 col-md-6 ms-auto">
      <DashboardCard cardType = "Light" cardTitle="Smart Light 1" id = "light-1" cardCmd = {setLight1} />
    </div>
    <div class="col-xl-4 col-md-6 ms-auto">
      <DashboardCard cardType = "Light" cardTitle="Smart Light 2" id = "light-2" cardCmd = {setLight2} />
    </div>
    <div class="col-xl-4 col-md-6 ms-auto">
      <DashboardCard cardType = "Plug" cardTitle="Smart Plug" />
    </div>
  </Row>

  <Row>
    <div class="col-xl-8">
      
      <DashboardCard cardType="Temp" cardTitle="Temperature and Humidity Sensor" id = "temp" cardCmd = None/>
      
    </div>
    <div class="col-xl-4">  
      <VideoCard cardTitle="Camera Feed"/>
      <DashboardCard
            cardTitle="Matter Device"
            cardType="Rgb-Light"
          />
    </div>
  </Row>
</Row>

<style>
  .title {
    padding: 30px;
    color: white;
    text-align: left;
    font-size: x-large;
  }
  /* :global(.col-xl-8){
    height: 100%;
  }
  :global(.col-xl-4){
    height: 100%;
  } */
</style>
