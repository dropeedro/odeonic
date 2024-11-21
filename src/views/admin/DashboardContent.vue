<template>
  <div class="admin-dashboard px-4 sm:px-6 lg:px-8">
    <div class="dashboard-content">
      <div class="section-header">
        <h1 class="text-3xl font-bold mb-6 pt-10 text-SecondaryColor text-center sm:text-left">
          Admin Dashboard
        </h1>
        <!-- Grid responsivo -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- Card 1 -->
          <div class="card bg-white w-full p-6 rounded-lg border-2 border-plusGrayColor">
            <canvas id="userChart"></canvas>
          </div>
          <!-- Card 2 -->
          <div class="card bg-white w-full p-6 rounded-lg border-2 border-plusGrayColor">
            <canvas id="downloadsChart"></canvas>
          </div>
          <!-- Card 3 -->
          <div class="card bg-white w-full p-6 rounded-lg border-2 border-plusGrayColor">
            <canvas id="earningsChart"></canvas>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

export default {
  name: "DashboardContent",
  mounted() {
    // Ejemplo de gráfico para usuarios
    new Chart(document.getElementById("userChart"), {
      type: "line",
      data: {
        labels: ["Week 1", "Week 2", "Week 3", "Week 4"],
        datasets: [
          {
            label: "New Users",
            data: [30, 45, 25, 60],
            borderColor: "rgba(75, 192, 192, 1)",
            backgroundColor: "rgba(75, 192, 192, 0.2)",
            fill: true,
          },
        ],
      },
    });

    // Ejemplo de gráfico para descargas
    new Chart(document.getElementById("downloadsChart"), {
      type: "bar",
      data: {
        labels: ["January", "February", "March", "April"],
        datasets: [
          {
            label: "Downloads",
            data: [150, 200, 180, 220],
            backgroundColor: "rgba(54, 162, 235, 0.2)",
            borderColor: "rgba(54, 162, 235, 1)",
            borderWidth: 1,
          },
        ],
      },
    });

    // Ejemplo de gráfico para ganancias
    new Chart(document.getElementById("earningsChart"), {
      type: "doughnut",
      data: {
        labels: ["Plan A", "Plan B", "Plan C"],
        datasets: [
          {
            label: "Earnings",
            data: [500, 700, 400],
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
    });
  },
};
</script>
