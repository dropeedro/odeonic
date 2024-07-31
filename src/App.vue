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
          <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Neque adipisci qui itaque, facere repudiandae molestiae dolore nulla voluptas ducimus minima accusantium aperiam sunt vel voluptatum, distinctio soluta ut rerum vitae.</p>
        </div>
        <div class="divsections-image">
          <img src="https://myscena.org/wp-content/uploads/2021/10/Beethoven_X_Header-e1635204954120.jpg" alt="aboutusimage"/>
        </div>
      </div>
    </div>
  </div>
  <div id="generatemusic">
    <div class="divsections">
      <div class="divsections-content">
        <div class="divsections-image-right">
          <img src="https://wi-tech.org/wp-content/uploads/2022/02/ai-produced-music-2-1.png" alt="generateaimusicimage"/>
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
        <h2>PREMIUN<br>PLAN</h2>
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
  height: 60vh;
  box-sizing: border-box;
}

.divsections-content {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  max-width: 100%;
  justify-content: space-between;
}

.divsections-text {
  max-width: 50%;
  padding: 1rem;
  margin: 0 auto;
  padding-left: 100px;
  color: var(--primary-color);
}

.divsections-image,
.divsections-image-right {
  position: relative;
  max-width: 100%;
  height: 100%;
  overflow: hidden;
}

.divsections-image img,
.divsections-image-right img {
  display: block;
  width: 100%;
  height: 100%;
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
  color: var(--secondary-color);;
  background-color: var(--primary-color);
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: var(--secondary-color);
}

.section-button:hover {
  background-color: var(--terciary-color);
}

/*CARDS PLANES PAGO */

.subscription-cards {
  padding-top: -100%;
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
  padding: 20px;
}

.card {
  background: var(--secondary-color);
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.582);
  padding: 15px;
  text-align: center;
  flex: 1;
  max-width: 300px;
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