<template>
  <div class="admin-dashboard">
    <AdminSidebar />
    <div class="dashboard-content">
      <h1 class="text-2xl font-bold mb-6">User Management</h1>
      <div class="crud-section">
        <!-- Aquí puedes añadir el listado y gestión de usuarios -->
        <div class="crud-card">
          <h2 class="text-lg font-semibold">Listar y Gestionar Usuarios</h2>
          <p class="text-base">
            Administra la lista de usuarios registrados en tu plataforma.
          </p>
          <button class="btn-primary mt-4">Agregar Nuevo Usuario</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AdminSidebar from '../Admin/AdminSidebar.vue';

export default {
  name: "UserManagement",
  components: {
    AdminSidebar,
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

.crud-section {
  display: grid;
  gap: 20px;
}

.crud-card {
  padding: 20px;
  background-color: #f8f8f8;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.btn-primary {
  padding: 10px 20px;
  background-color: #6b5b95;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: #5a4a82;
}
</style>
