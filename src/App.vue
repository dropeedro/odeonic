<script setup>
import Navbar from './components/Navbar.vue'
</script>

<template>
  <Navbar/>
  <br>
  <div id="aboutus">
    <div class="aboutus">
      <div class="aboutus-content">
        <div class="aboutus-text">
          <h1>About us</h1>
          <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Neque adipisci qui itaque, facere repudiandae molestiae dolore nulla voluptas ducimus minima accusantium aperiam sunt vel voluptatum, distinctio soluta ut rerum vitae.</p>
        </div>
        <div class="aboutus-image">
          <img src="https://myscena.org/wp-content/uploads/2021/10/Beethoven_X_Header-e1635204954120.jpg" alt="slide 1"/>
        </div>
      </div>
    </div>
  </div>
  <div id="generate">
    <div class="body">
      <div class="content">
        <div class="text">
          <h1>Let's Generate!</h1>
        </div>
      </div>
    </div> 
  </div>
</template>

<style scoped>
.aboutus {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 60vh;
  box-sizing: border-box;
}

.aboutus-content {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  max-width: 100%;
  justify-content: space-between;
}

.aboutus-text {
  max-width: 50%;
  padding: 1rem;
  margin: 0 auto;
  padding-left: 100px;
  color: var(--text-color);
}

.aboutus-image {
  position: relative;
  max-width: 100%;
  height: 500px;
  overflow: hidden;
}

.aboutus-image img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: relative;
  z-index: 1;
}

.aboutus-image::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to left, rgba(0, 0, 0, 0) 0%, rgba(255, 255, 255, 1) 100%);
  z-index: 2;
}
</style>