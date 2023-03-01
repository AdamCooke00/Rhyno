<script>
  import { onMount } from 'svelte';
  import Chart, { registerables } from 'chart.js/auto';
  import zoomPlugin from 'chartjs-plugin-zoom';
  import {apiUrl} from '../pages/dashboard';

  Chart.register(zoomPlugin,...registerables)

  let tempData = [];
  let humData = [];
  let timeData = [];

  let chartCtx, chart;

  export let currTemp, currHum;

  function createChart(){
    chartCtx = document.getElementById('myChart').getContext('2d');
    chart = new Chart(chartCtx, {
      type: 'line',
      data: {
        labels: timeData,
        datasets: [
          {
            label: 'Temperature',
            data: tempData,
            fill: false,
            borderColor: 'red'
          },
          {
            label: 'Humidity',
            data: humData,
            fill: false,
            borderColor: 'blue'
          }
        ]
      },
      options: {
        plugins: {
          zoom: {
            pan: {
              enabled: true,
              mode: 'x'
            },
            zoom: {
              wheel: {
                enabled: true,
              },
              pinch: {
                enabled: true
              },
              mode: 'x'
            }
          }
        },
        maintainAspectRatio: false // set to false to fill the height of the canvas
      }
    });
  }

  function getData() {
    fetch(apiUrl, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        temp: "get-data",
      }),
    })
    .then(response => response.json())
    .then(data => {
      
      timeData = data.time;
      tempData = data.temperature;
      humData = data.humidity;

      currTemp = tempData[tempData.length - 1];
      currHum = humData[humData.length - 1];
      
      // Update the data object of the chart instance
      chart.data.labels = timeData;
      chart.data.datasets[0].data = tempData;
      chart.data.datasets[1].data = humData;
      
      chart.update();
    })
    .catch(error => console.error(error));
  }

  onMount(() => {
    createChart();
    getData();
    setInterval(getData, 10000);
  });
</script>

<div style="height: 100%;">
  <canvas id="myChart"></canvas>
</div>
