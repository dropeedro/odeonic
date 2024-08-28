<template>
  <nav>
    <ul>
      <li class="logo"><img src="https://imgur.com/cq4f4wn.png" alt="LOGO" width="250px"></li>
      <li class="nav-item"><button><router-link to="/" class="nav-button">Home</router-link></button></li>
      <li class="nav-item"><button class="nav-button">About us</button></li>
      <li class="nav-item"><button class="nav-button">Generate Music</button></li>
      <li class="nav-item"><button class="nav-button">Plans</button></li>
      <li class="nav-item"><button class="nav-button">Log-In</button></li>
      <li class="nav-item"><button class="nav-button"><i class="pi pi-shopping-bag"></i></button></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>
nav {
  background-color: var(--secondary-color);
  color: var(--primary-color);
  padding: 1em;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  display: flex;
  justify-content: center;
}

ul {
  list-style: none;
  display: flex;
  align-items: center;
  margin: 0;
  padding: 0;
  width: 100%;
  max-width: 1600px;
}

li {
  color: var(--primary-color);
  font-weight: bold;
}

.logo {
  margin-right: auto;
  padding-top: 5px;
  width: 100px;
}

.nav-item {
  margin-left: 20px;
}

.nav-button {
  color: var(--primary-color);
  text-decoration: none;
}

.nav-button:hover {
  color: var(--terciary-color);
}
</style>
