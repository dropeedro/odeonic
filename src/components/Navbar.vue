<template>
    <nav>
      <ul>
        <li class="logo"><img src="C:/Users/Diego/Desktop/ODEONIC/Odeonic-project/src/assets/ODEONICLOGO.png" alt="LOGO" width="180px"></li>
        <li><router-link to="/" class="nav-button">Home</router-link></li>
        <li><router-link to="/about" class="nav-button">About</router-link></li>
        <li><router-link to="/plans" class="nav-button">Plans</router-link></li>
        <li><router-link to="/login" class="nav-button">Log-In</router-link></li>
        <li><button class="nav-cart">Cart</button></li>
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
    background-color: #ffffff;
    color: white;
    padding: 1em;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  ul {
    list-style: none;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 0;
    padding: 0;
    padding-right: 40px;
  }
  
  li {
    color: rgb(0, 0, 0);
    font-weight: bold;
  }
  
  .logo {
    margin-right: auto;
  }
  
  ul > li:not(.logo) {
    margin-left: 20px;
  }
  
  router-link {
    color: rgb(0, 0, 0);
    text-decoration: none;
  }
  
  router-link:hover {
    color: #82328B;
  }
  </style>