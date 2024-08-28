<script setup>
import Navbar from './components/Navbar.vue'
</script>

<template>
  <Navbar/>
  <br>
  <div id="aboutus">
    <div class="divsections">
      <div class="divsections-content">
        <div class="divsections-text">
          <h1>About us</h1>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. A consequatur labore earum quae, ducimus sapiente suscipit, odit atque ab error veniam officiis ex distinctio repellat. Qui a accusamus molestiae ipsam.</p>
        </div>
        <div class="divsections-image">
          <img src="https://myscena.org/wp-content/uploads/2021/10/Beethoven_X_Header-e1635204954120.jpg" alt="A representation of Beethoven"/>
        </div>
      </div>
    </div>
  </div>
  <div id="generatemusic">
    <div class="divsections">
      <div class="divsections-content">
        <div class="divsections-image-right">
          <img src="https://assets.mofoprod.net/network/images/AI-musicBlog-hero.original.png" alt="AI-generated music illustration"/>
        </div>
        <div class="divsections-text">
          <h1>Let's Generate!</h1>
          <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Neque adipisci qui itaque, facere repudiandae molestiae dolore nulla voluptas ducimus minima accusantium aperiam sunt vel voluptatum, distinctio soluta ut rerum vitae.</p>
          <button><router-link to="/login" class="section-button" style="align-items: center;">View More</router-link></button>
        </div>
      </div>
    </div>
  </div>
  <div>
    <div class="divsections">
      <div class="divsections-content">
        <div class="divsections-text">
          <h1 style="text-align: center;">Pricing Plans</h1>
          <p style="text-align: center;">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Neque adipisci qui itaque, facere repudiandae molestiae dolore nulla voluptas ducimus minima accusantium aperiam sunt vel voluptatum, distinctio soluta ut rerum vitae.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="subscription-cards">
    <div class="card">
      <h2>BASIC<br>PLAN</h2>
      <p>$4.99/MONTH</p>
      <button>GET STARTED</button>
      <ul>
        <br>
        <li>Acceso básico</li>
        <li>1 usuario</li>
        <li>Soporte por email</li>
      </ul>
    </div>
    <div class="card">
      <h2>PREMIUM<br>PLAN</h2>
      <p>$4.99/MONTH</p>
      <button>GET STARTED</button>
      <ul>
        <br>
        <li>Acceso completo</li>
        <li>Hasta 5 usuarios</li>
        <li>Soporte por chat</li>
      </ul>
    </div>
    <div class="card">
      <h2>PRO<br>PLAN</h2>
      <p>$4.99/MONTH</p>
      <button>GET STARTED</button>
      <ul>
        <br>
        <li>Acceso completo</li>
        <li>Usuarios ilimitados</li>
        <li>Soporte prioritario</li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
body, html {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow-x: hidden;
  box-sizing: border-box;
}

.divsections {
  display: flex;
  justify-content: center;
  align-items: center;
  height: auto;
  box-sizing: border-box;
  padding: 20px 0;
  margin-bottom: 20px;
}

.divsections-content {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  max-width: 100%;
  justify-content: space-between;
  margin: 0 auto;
  padding: 0;
}

.divsections-text {
  max-width: 50%;
  padding: 1rem;
  margin: 0 auto;
  padding-left: 50px;
  color: var(--primary-color);
}

.divsections-text h1, .divsections-text p {
  margin-bottom: 10px;
}

.divsections-image,
.divsections-image-right {
  position: relative;
  max-width: 100%;
  height: auto;
  overflow: hidden;
}

.divsections-image img,
.divsections-image-right img {
  display: block;
  width: 100%;
  height: auto;
  object-fit: cover;
  position: relative;
  z-index: 1;
}

.divsections-image::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: var(--gradient-left);
  z-index: 2;
}

.divsections-image-right::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
  background: var(--gradient-right);
  z-index: 2;
}

.section-button {
  display: block;
  padding: 0.5rem 1rem;
  font-size: 1.3rem;
  color: var(--secondary-color);
  background-color: var(--primary-color);
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.section-button:hover {
  background-color: var(--terciary-color);
}

/* Tarjetas de suscripción */
.subscription-cards {
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
  padding: 20px;
  margin-bottom: 20px;
}

.card {
  background: var(--secondary-color);
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.582);
  padding: 15px;
  text-align: center;
  flex: 1;
  max-width: 300px;
  margin-bottom: 20px;
}

.card h2 {
  font-weight: 800;
  font-size: 2.4em;
  margin-bottom: 10px;
  color: var(--primary-color);
}

.card p {
  font-size: 1.2em;
  color: var(--primary-color);
  margin-bottom: 20px;
}

.card ul {
  list-style: none;
  padding: 0;
  margin: 0 0 20px;
}

.card ul li {
  margin-bottom: 10px;
  color: var(--primary-color);
}

.card button {
  background-color: var(--primary-color);
  color: var(--secondary-color);
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 1.2em;
  font-weight: bold;
}

.card button:hover {
  background-color: var(--terciary-color);
}
</style>
