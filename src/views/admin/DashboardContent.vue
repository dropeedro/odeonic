<template>
  <div class="admin-dashboard">
    <AdminSidebar />
    <div class="dashboard-content">
      <h1>Admin Dashboard</h1>
      <div class="charts">
        <div class="chart-container">
          <canvas id="userChart"></canvas>
        </div>
        <div class="chart-container">
          <canvas id="downloadsChart"></canvas>
        </div>
        <div class="chart-container">
          <canvas id="earningsChart"></canvas>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';
import AdminSidebar from '../Admin/AdminSidebar.vue';

Chart.register(...registerables);

export default {
  name: "DashboardContent",
  components: {
    AdminSidebar,
  },
  mounted() {
    // Ejemplo de gráfico para usuarios
    new Chart(document.getElementById("userChart"), {
      type: 'line',
      data: {
        labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        datasets: [{
          label: 'New Users',
          data: [30, 45, 25, 60],
          borderColor: 'rgba(75, 192, 192, 1)',
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          fill: true
        }]
      }
    });

    // Ejemplo de gráfico para descargas
    new Chart(document.getElementById("downloadsChart"), {
      type: 'bar',
      data: {
        labels: ['January', 'February', 'March', 'April'],
        datasets: [{
          label: 'Downloads',
          data: [150, 200, 180, 220],
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1
        }]
      }
    });

    // Ejemplo de gráfico para ganancias
    new Chart(document.getElementById("earningsChart"), {
      type: 'doughnut',
      data: {
        labels: ['Plan A', 'Plan B', 'Plan C'],
        datasets: [{
          label: 'Earnings',
          data: [500, 700, 400],
          backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(153, 102, 255, 0.2)'],
          borderColor: ['rgba(255, 99, 132, 1)', 'rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)'],
          borderWidth: 1
        }]
      }
    });
  }
};
</script>

<style scoped>
.admin-dashboard {
  display: flex;
}

.dashboard-content {
  padding: 20px;
  flex-grow: 1;
}

.charts {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.chart-container {
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  padding: 10px;
  background-color: #f8f8f8;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
