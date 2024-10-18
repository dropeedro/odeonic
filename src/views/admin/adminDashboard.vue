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

<style scoped>
h1 {
  margin-bottom: 20px;
}

p {
  font-size: 18px;
  margin-bottom: 20px;
}

button {
  padding: 10px 20px;
  background-color: #2d2d2d;
  color: #ffffff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #3a3a3a;
}
</style>
