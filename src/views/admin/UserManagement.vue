<template>
  <div>
    <h2>Lista de Usuarios</h2>
    <ul v-if="usuarios.length > 0">
      <li v-for="usuario in usuarios" :key="usuario.id">
        {{ usuario.email }}
      </li>
    </ul>
    <p v-else>No hay usuarios registrados.</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserList',
  data() {
    return {
      usuarios: [] // Almacena los usuarios obtenidos del backend
    }
  },
  methods: {
    async fetchUsuarios() {
      try {
        // Solicitud al backend para obtener la lista de usuarios
        const response = await axios.get('http://localhost:8000/usuarios')
        this.usuarios = response.data
      } catch (error) {
        console.error("Error al obtener usuarios:", error)
      }
    }
  },
  mounted() {
    // Llamada al método cuando se monta el componente
    this.fetchUsuarios()
  }
}
</script>

<style scoped>
h2 {
  color: #333;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 5px 0;
}
</style>
