<script>
  import { Card, CardBody, CardFooter, CardText } from "sveltestrap";
  import { Player, Hls } from "@vime/svelte";
  import { start_hydrating } from "svelte/internal";
  import { apiUrl } from "../pages/dashboard";

  export let cardTitle;

  // location of hls video file in the public/video directory
  // Note this hls video is converted from rtsp by another program running FFPMEG
  let videoUrl = "./video/stream.m3u8";

  let rtspUrl = "";
  let ezVizCameraUrl = "rtsp://admin:EZCMNT@192.168.50.170:554/H.264";
  let testRtspUrl =
    "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4";

  // Sends camera command to the djgano REST api
  function sendCameraCmd(direction, state) {
    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        camera: direction,
        move: state,
      }),
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  }

  function videoStream(startStop) {
    // rtspUrl = document.getElementById("rtsp-url").value;
    rtspUrl = ezVizCameraUrl;
    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        camera: "rtsp",
        rtspUrl: rtspUrl,
        cmd: startStop,
      }),
    });

    // Reloads after 3.5s to show the video
    setTimeout(reload, 3500);
  }

  function reload() {
    location.reload();
  }

  const options = [
    { value: ezVizCameraUrl, label: "Ezviz Wifi Camera" },
    { value: testRtspUrl, label: "Test RTSP Stream" },
  ];

  function handleChange(event) {
    let selectedValue = event.target.value;
    document.getElementById("rtsp-url").value = selectedValue;
  }
</script>

<!-- Layout of the Video Card - On mouse down the movement starts, when button released movement stops -->
<Card inverse color="dark" class="mb-4 ms-auto">
  <div class="card-div">
    <CardBody>
      <CardText>{cardTitle}</CardText>
      <Player controls>
        <Hls version="latest">
          <source data-src={videoUrl} type="application/x-mpegURL" />
        </Hls>
      </Player>
    </CardBody>
    <div class="container">
      <div class="row">
        <div class="col text-center">
          <!-- <div class ="row">
            <label for="dropdown">Select an RTSP stream:</label>
            <select class="dropdown" id="dropdown" on:change={handleChange}>
              <option value="">Select an RTSP stream</option>
              {#each options as option}
                <option value={option.value}>{option.label}</option>
              {/each}
            </select>
          </div>
          <input type="text" class="form-control" id="rtsp-url" bind:value={rtspUrl} placeholder="Enter RTSP Url"> -->
          <button class="submit-btn" on:click={() => videoStream("start")}
            >Start Stream</button
          >
          <button class="submit-btn" on:click={() => videoStream("stop")}
            >End Stream</button
          >
        </div>
      </div>
      <div class="row">
        <div class="col text-center">
          <button
            class="btn"
            id="up"
            on:mousedown={() => sendCameraCmd("up", "start")}
            on:mouseup={() => sendCameraCmd("up", "stop")}>↑</button
          >
        </div>
      </div>
      <div class="row">
        <div class="col text-center">
          <button
            class="btn"
            id="left"
            on:mousedown={() => sendCameraCmd("left", "start")}
            on:mouseup={() => sendCameraCmd("left", "stop")}>←</button
          >
          <button
            class="btn"
            id="down"
            on:mousedown={() => sendCameraCmd("down", "start")}
            on:mouseup={() => sendCameraCmd("down", "stop")}>↓</button
          >
          <button
            class="btn"
            id="right"
            on:mousedown={() => sendCameraCmd("right", "start")}
            on:mouseup={() => sendCameraCmd("right", "stop")}>→</button
          >
        </div>
      </div>
    </div>
  </div>
</Card>

<style>
  .container {
    background-color: rgba(14, 32, 53, 0.729);
    width: 92.5%;
    padding: 25px;
    border-radius: 5%;
  }

  .card-div {
    background-color: rgba(93, 151, 185, 0.665);
    padding-top: 10px;
    padding-bottom: 25px;
    border-radius: 1%;
  }
  .btn {
    width: 50px;
    font-size: 40px;
    background-color: aliceblue;
    border-color: None;
    margin: 0%;
    padding: 0%;
  }
  .btn:hover {
    background-color: rgb(56, 75, 85);
    color: aliceblue;
  }

  .row {
    padding-bottom: 2%;
  }
  .dropdown {
    width: 50%;
    margin: auto;
  }
</style>
