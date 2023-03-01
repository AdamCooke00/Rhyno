<script>
  import { onMount } from 'svelte';
  import { Col, Container, Row, Button } from "sveltestrap";
  import jquery from 'jquery';
  import  "round-slider";
  import 'round-slider/dist/roundslider.min.css';

  
  // Id used for the slider div passed in as a prop, this way each slider has a unique id and can be accessed individually. 
  export let id;

  // Function passed in as a prop that posts a command to set the light to the backend api 
  export let setLight;

  //This is the source of the image in the parent component (ie DashboardCard..)
  //Can be modified within this component to modify the image in the parent card
  export let imgSrc; 

  // Initial values
  let sliderValue = 50;
  let stateText = "TURN OFF";
  let state = "ON";


  // Handles the click of the on/off burron
  // Checks the current state and reverses, setting the corresponding state, text, img source, and css classes
  // Finally calls the passed in setLight function to call the api and send the info to the backend
  function handleClick() {
    
    if(state == "OFF"){
      state = "ON";
    }
    else{
      state = "OFF"
    }
    sliderValue = jquery('#' + id).roundSlider('getValue');

    setLight(state, sliderValue);
  }

  // Handles the change of the slider value and sends a "on" command to the backend with selected brightness
  function handleSlider() {
    sliderValue = jquery('#' + id).roundSlider('getValue');
    console.log(sliderValue)
    state = "ON";
   
    setLight(state,sliderValue);
  }

  // On document ready run the roundSlider() function on the id of the slider, this initiates the component
  jquery(document).ready(() => {
    jquery('#' + id).roundSlider({
      sliderType: "min-range",
      value: sliderValue,
      stopAtEnd: true,
      min:0,
      max:254,
      step:1,
      showTooltip: true,
      endAngle:360,
      tooltipFormat: (args) => args.value,

    });
    // Using jquery to modify the css of the round-slider classes
    jquery('#' + id).on('change', handleSlider); // add event listener for input event
    jquery('.rs-handle').css('background-color', '#808080');
    jquery('.rs-tooltip-text').css('color', '#a1caed');
    jquery('.rs-tooltip-text').css('background-color', '#29324a');
    jquery('.rs-range-color').css('background-color', '#2a3f52');
    jquery('.rs-path-color').css('background-color', '#b5b5b5');
    jquery('.rs-border').css('border','None');
  });

  function updateValues() {

    let key = ""
    if(id == "light-1")
      key = "light1"
    else if(id == "light-2")
      key = "light2"
    fetch(`./device_states/${key}_curr.txt`)
  .then(response => response.text())
  .then(data => {
    // do something with the data
    const values = data.split(',');
    const brightness = parseInt(values[0].split(':')[1]);
    const lightState = values[1].split(':')[1];
    // console.log('Brightness:', brightness);
    // console.log('State:', lightState);
    sliderValue = brightness
    jquery('#' + id).roundSlider('setValue',sliderValue);
    state = lightState

    
    if(state == "OFF"){
      imgSrc = "./images/light_off.png"
      stateText = "Turn ON"
    }
    else{
      imgSrc = "./images/light_on.png"
      stateText = "Turn OFF"
    }
    return data
  })
  .catch(error => {
    // handle any errors
    console.error(error);
    throw error
  });
  }

  onMount(() => {
    
   
    setInterval(updateValues,750); 
  });

</script>

<!-- Light Component -->
<main>
  <Container>
    <Row>
      <Col>State: {state}</Col>
      <Col>Brightness: {sliderValue}</Col>
    </Row>
    <div id={id} class = "slider" on:change={handleSlider}></div>
    <Button color="light" on:click={handleClick}>{stateText}</Button>
  </Container>
</main>

<style>
  main {
    max-width: 100%;
    color: aliceblue;
  }

  .slider {
    margin: auto;
    padding-bottom: 200px;
  }
</style>
