<template>
  <div>
    <h1>Admin Dashboard</h1>
    <p>Welcome, {{ userName }}!</p>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
import { keycloak } from '../../keycloak'; 

export default {
  data() {
    return {
      userName: ''
    };
  },
  mounted() {
    // Verifica si el usuario está autenticado
    if (keycloak.authenticated) {
      this.userName = keycloak.tokenParsed?.preferred_username || 'Admin';
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