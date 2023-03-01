export let apiUrl = "http://192.168.50.154:8000/api/smarthome/"

export function sendPostOn() {
    sendPlugCmd("ON");
  }
  export function sendPostOff() {
    sendPlugCmd("OFF");
  }

  export function sendPlugCmd(state) {
    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        plug: state,
      }),
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  }

  export function setLight1(state, value) {
    setLight("light1",state,value)
  }

  export function setLight2(state, value) {
    setLight("light2",state,value)
  }
    

  function setLight( light, state, value ){

    console.log("HELLO!")
    console.log(value);
    
    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        [light]: state,
        brightness: value,
      }),
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  }
