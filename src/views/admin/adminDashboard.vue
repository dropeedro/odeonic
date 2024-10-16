<!-- <script setup>
</script>

<template>
  <div>
    <div class="mx-4 flex flex-wrap">
      <div class="w-full px-4">
        <div class="mx-auto mb-[60px] max-w-[510px] text-left">
          <h2 class="mb-3 text-3xl leading-[1.208] font-bold text-dark sm:text-4xl md:text-[40px]">
            Welcome Back {username}
          </h2>
          <p class="text-base text-body-color ">
            We offer a variety of plans to suit your needs and budget. Choose the plan that best fits
            your musical goals and start exploring everything our platform has to offer.
          </p>
        </div>
      </div>
    </div>
  </div>
</template> -->

<template>
  <div>
    <h1>Admin Dashboard</h1>
    <p>Welcome, {{ userName }}!</p>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
import { keycloak } from '../../keycloak'; // Asegúrate de que la ruta sea correcta

export default {
  data() {
    return {
      userName: ''
    };
  },
  mounted() {
    // Verifica si el usuario está autenticado
    if (keycloak.authenticated) {
      this.userName = keycloak.tokenParsed.preferred_username; // O el campo que desees
    } else {
      // Redirige a la página de inicio de sesión si no está autenticado
      keycloak.login();
    }
  },
  methods: {
    logout() {
      keycloak.logout();
    }
  }
};
</script>
