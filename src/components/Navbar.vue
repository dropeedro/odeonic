<template>
  <nav>
    <ul>
      <li class="logo"><img src="C:/Users/Diego/Desktop/ODEONIC/Odeonic-project/src/assets/ODEONICLOGO.png" alt="LOGO" width="180px"></li>
      <li class="nav-item"><button><router-link to="/" class="nav-button">Home</router-link></button></li>
      <li class="nav-item"><button><router-link to="/about" class="nav-button">About us</router-link></button></li>
      <li class="nav-item"><button><router-link to="/" class="nav-button">Generate Music</router-link></button></li>
      <li class="nav-item"><button><router-link to="/plans" class="nav-button">Plans</router-link></button></li>
      <li class="nav-item"><button><router-link to="/login" class="nav-button">Log-In</router-link></button></li>
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

/* Media */
@media (max-width: 768px) {
  nav {
    padding: 0.5em;
  }

  ul {
    flex-direction: column;
    align-items: flex-start;
  }

  .logo {
    padding-left: 15px;
  }

  .nav-item {
    margin-left: 0;
    margin-top: 10px;
  }

  .nav-cart {
    margin-top: 10px;
  }
}

@media (max-width: 480px) {
  .logo img {
    width: 120px;
  }

  .nav-button {
    font-size: 0.9em;
  }
}
</style>
