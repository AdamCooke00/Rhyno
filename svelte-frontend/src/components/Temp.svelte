<script>
    import { Row, Col } from "sveltestrap";

    import GraphCard from "../components/GraphCard.svelte";

    let tempImg = "./images/temp.png";
    let humImg = "./images/humidity.png";
    let temperature;
    let humidity;
  </script>
  
  <Row>
    <Col>
      <img class="temp" src={tempImg} alt="Temperature" />
      <p>Temperature: {temperature}°C</p>
    </Col>
    <Col>
      <img class="humidity" src={humImg} alt="Humidity" />
      <p>Humidity: {humidity}%</p>
    </Col>
  </Row>
  <GraphCard bind:currTemp={temperature} bind:currHum={humidity} graphTitle="History">
  
  </GraphCard>
  
  
  <style>
    .temp{
      height: 60px;
      width: 40px;
    }
  
    .humidity{
      height: 60px;
      width: 60px;
    } 
    p {
      text-align: center;
      margin-top: 10px;
    }
  </style>
  