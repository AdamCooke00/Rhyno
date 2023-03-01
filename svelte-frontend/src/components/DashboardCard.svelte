<script>
  import { onMount } from "svelte";
  import { Card, CardBody, CardFooter, CardText } from "sveltestrap";
  import Light from "./Light.svelte";
  import Plug from "./Plug.svelte";
  import Temp from "./Temp.svelte";
  import RgbLight from "./RgbLight.svelte";

  import { apiUrl } from "../pages/dashboard.js";

  export let cardTitle; // Title of card
  export let cardType; // Card type (component), determines what is placed inside the card
  export let cardCmd; // A card command that can be passed down as a prop into a child component (such as Light)
  export let imgSrc; // Location of card image
  export let id; // Id of the card

  let toggle = false; // boolean for toggle details
  let textColor = "white";
  let cardFooterText = "Show Details";
  let imgClass = "";

  // Function to handle the details toggle
  function toggleDetails() {
    toggle = !toggle;
    if (toggle) cardFooterText = "Hide Details";
    else cardFooterText = "Show Details";
  }

  // Functions to handle move going over the details text
  function handleMouseOver() {
    textColor = "#a3ceff";
  }

  function handleMouseOut() {
    textColor = "white";
  }

  let tempClass = "";
  // Setting the image source and css class based on the type of card
  // Note this image is displayed in the header of the card
  if (cardType == "Light") {
    imgSrc = "./images/light_on.png";
    imgClass = "light";
  }
  if (cardType == "Plug") {
    imgSrc = "./images/plug.png";
    imgClass = "plug";
  }
  if (cardType == "Rgb-Light") {
    imgSrc = "./images/rgb_light.png";
    imgClass = "rgb-light";
  }
  if (cardType == "Temp") {
    // Class that sets the height to 100% for the graph..
    tempClass = "temp-class";
  }

  onMount(() => {
    if (id == "light-1") {
      fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          light1: "get-data",
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          let state = data.state;
          if (state == "ON") {
            imgSrc = "./images/light_on.png";
          } else {
            imgSrc = "./images/light_off.png";
          }
        })
        .catch((error) => console.error(error));
    } else if (id == "light-2") {
      fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          light2: "get-data",
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          let state = data.state;
          if (state == "ON") {
            imgSrc = "./images/light_on.png";
          } else {
            imgSrc = "./images/light_off.png";
          }
        })
        .catch((error) => console.error(error));
    }
  });
</script>

<!-- Card Layout -->

<Card inverse color="dark" class="mb-4 ms-auto {tempClass}">
  <div class="card">
    <CardBody>
      <CardText
        >{cardTitle}
        {#if cardType != "Temp"}
          <img id="img" class={imgClass} src={imgSrc} alt="Not Found" />
        {/if}
      </CardText>
      {#if toggle && cardType == "Light"}
        <Light bind:imgSrc {id} setLight={cardCmd} />
      {/if}
      {#if toggle && cardType == "Plug"}
        <Plug setPlug={cardCmd} />
      {/if}
      {#if cardType == "Temp"}
        <Temp />
      {/if}
      {#if toggle && cardType == "Rgb-Light"}
        <RgbLight />
      {/if}
    </CardBody>

    {#if cardType != "Temp"}
      <CardFooter class="d-flex align-items-center justify-content-between">
        <p
          style="--txt-color: {textColor}"
          on:click={toggleDetails}
          on:keypress={toggleDetails}
          on:mouseover={handleMouseOver}
          on:focus={handleMouseOver}
          on:mouseout={handleMouseOut}
          on:blur={handleMouseOut}
        >
          {cardFooterText}
        </p>
      </CardFooter>
    {/if}
  </div>
</Card>

<style>
  p {
    color: var(--txt-color);
    cursor: pointer;
  }
  .card {
    background-color: rgba(93, 151, 185, 0.665);
    height: 100%;
  }
  .light {
    margin-left: 50px;
    height: 40px;
    width: 40px;
  }
  .rgb-light {
    margin-left: 50px;
    height: 100px;
    width: 100px;
  }
  .matter {
    margin-left: 50px;
    height: 50px;
    width: 150px;
  }

  .plug {
    margin-left: 50px;
    width: 40px;
    height: 50px;
  }
  :global(.temp-class) {
    height: 100%;
  }
</style>
