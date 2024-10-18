<template>
  <aside class="admin-sidebar">
    <nav>
      <ul>
        <li>
          <router-link to="/admin">Dashboard</router-link>
        </li>
        <li>
          <router-link to="/admin/plans">Plans</router-link>
        </li>
        <li>
          <router-link to="/admin/users">Users</router-link>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script>
export default {
  name: "AdminSidebar",
};
</script>

<style scoped>
.admin-sidebar {
  width: 200px;
  background-color: #f4f4f4;
  padding: 15px;
  height: 100vh;
}

.admin-sidebar nav ul {
  list-style-type: none;
  padding: 0;
}

.admin-sidebar nav ul li {
  margin-bottom: 10px;
}

.admin-sidebar nav ul li a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.admin-sidebar nav ul li a.router-link-active {
  color: #007bff;
}
</style>
