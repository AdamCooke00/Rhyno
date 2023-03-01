<script>
    import { onMount } from 'svelte';
    import { Col, Container, Row, Button } from "sveltestrap";
    import {sendPlugCmd, apiUrl} from '../pages/dashboard.js'
      
    let value = 0;
    let stateText = "TURN OFF";
    let state = "ON";

    let imgSrc = "./images/plug_off.png"
  
    function handleClick() {
      console.log(state);
      if (state == "OFF") {
        state = "ON";
      } else {
        state = "OFF";
      }
  
      sendPlugCmd(state)
    }
  
    let color = "primary";

  function updateState(){
    fetch('./device_states/plug1_curr.txt')
  .then(response => response.text())
  .then(data => {
    // do something with the data
    const plugState = data.split(':')[1];
    state = plugState
    // console.log('State:', state);

    if(state == "ON")
    {
      imgSrc = "./images/plug_on.png"
      stateText = "Turn OFF"
    }
    else{
      imgSrc = "./images/plug_off.png"
      stateText = "Turn ON"
    }
    return data;
  })
  .catch(error => {
    // handle any errors
    console.error(error);
    throw error;
  });
    

    

  }
  
  onMount(() => {
    
    updateState();
    setInterval(updateState,750);
  });

    

 

  </script>
  
  <main>
    <Container>
      <Row>
        <Col>
          State:
          <img class = "power-img" src={imgSrc} alt="your_image_alt_text" />
        </Col>
        <Col class="text-right">
          <button class = "btn" color="light" on:click={handleClick}>{stateText}</button>
        </Col>
      </Row>
    </Container>
  </main>

  <style>
    .power-img{
      height: 60px;
      width: 40px;
    }
    .btn{
      margin-top:10px;
      background-color: aliceblue;
      color:rgb(21, 27, 49);
    }
    .btn:hover{
      background-color: rgb(28, 45, 58);
      color:aliceblue
    }
  </style>