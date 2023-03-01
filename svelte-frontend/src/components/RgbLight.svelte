<script>
    import {apiUrl} from "../pages/dashboard.js"
  
    let brightness = 127;
    let state = "off"
    let currentColor = ""
  
    const colors = [
      { name: 'Red', hex: '#ff0000' },
      { name: 'Orange', hex: '#ffa500' },
      { name: 'Yellow', hex: '#ffff00' },
      { name: 'Lime-Green', hex: '#00ff00' },
      { name: 'Green', hex: '#008000' },
      { name: 'Turquoise', hex: '#40e0d0' },
      { name: 'Blue', hex: '#0000ff' },
      { name: 'Purple', hex: '#800080' }
    ];
  

  function sendColorCmd(color,state){
    currentColor = color
    console.log(color,brightness,state)
    fetch(apiUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                matter: "rgb-light",
                color: color,
                state: state,
                brightness:brightness
            }),
            })
            .then((response) => response.json())
            .then((data) => console.log(data))
            .catch((error) => console.error(error));
  }

  function handleSlider(){
    sendColorCmd(currentColor,"on")
  }
  
  </script>
  
  <style>
    .color-button {
      display: inline-block;
      width: 50px;
      height: 50px;
      margin-right: 10px;
      border-radius: 50%;
      cursor: pointer;
      transition: transform 0.2s ease-in-out;
    }
  
    .color-button:hover {
      transform: translate(2px, -2px);
    }
  </style>
  
  <div>
    {#each colors as color}
      <div
        class="color-button"
        style="background-color: {color.hex}"
        on:click={() => sendColorCmd(color,"on")}
      ></div>
    {/each}
  </div>
  
  <div>
    <input
      type="range"
      min="0"
      max="254"
      step="1"
      bind:value={brightness}
      on:mouseup={handleSlider}
    />
    <div>{brightness}</div>
  </div>
  