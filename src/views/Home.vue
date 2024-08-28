<template>
  <div>
    <div id="aboutus" class="py-5 mb-5">
      <div class="flex flex-col md:flex-row items-center justify-between">
        <div class="md:w-1/2 px-4 md:px-12 text-primary">
          <h1 class="text-3xl mb-4">About us</h1>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. A consequatur labore earum quae, ducimus sapiente suscipit, odit atque ab error veniam officiis ex distinctio repellat. Qui a accusamus molestiae ipsam.</p>
        </div>
        <div class="md:w-1/2 relative overflow-hidden">
          <img class="w-full h-auto object-cover" src="https://myscena.org/wp-content/uploads/2021/10/Beethoven_X_Header-e1635204954120.jpg" alt="A representation of Beethoven" />
        </div>
      </div>
    </div>
    <div id="generatemusic" class="py-5 mb-5">
      <div class="flex flex-col md:flex-row items-center justify-between">
        <div class="md:w-1/2 relative overflow-hidden">
          <img class="w-full h-auto object-cover" src="https://assets.mofoprod.net/network/images/AI-musicBlog-hero.original.png" alt="AI-generated music illustration" />
        </div>
        <div class="md:w-1/2 px-4 md:px-12 text-primary">
          <h1 class="text-3xl mb-4">Let's Generate!</h1>
          <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Neque adipisci qui itaque, facere repudiandae molestiae dolore nulla voluptas ducimus minima accusantium aperiam sunt vel voluptatum, distinctio soluta ut rerum vitae.</p>
          <button class="bg-primary text-secondary py-2 px-4 rounded transition-colors duration-300 hover:bg-tertiary">
            <router-link to="/" class="flex items-center">View More</router-link>
          </button>
        </div>
      </div>
    </div>
    <div class="py-5 mb-5">
      <div class="flex flex-col items-center">
        <div class="text-center">
          <h1 class="text-3xl mb-4">Pricing Plans</h1>
          <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Neque adipisci qui itaque, facere repudiandae molestiae dolore nulla voluptas ducimus minima accusantium aperiam sunt vel voluptatum, distinctio soluta ut rerum vitae.</p>
        </div>
      </div>
    </div>
    <div class="flex justify-evenly flex-wrap p-5 mb-5">
      <div class="bg-secondary text-primary rounded-lg shadow-lg p-4 text-center flex-1 max-w-xs mb-5">
        <h2 class="text-2xl font-extrabold mb-2">BASIC<br />PLAN</h2>
        <p class="text-xl mb-4">$4.99/MONTH</p>
        <button class="bg-primary text-secondary py-2 px-4 rounded transition-colors duration-300 hover:bg-tertiary">GET STARTED</button>
        <ul class="list-disc mt-4">
          <li>Acceso básico</li>
          <li>1 usuario</li>
          <li>Soporte por email</li>
        </ul>
      </div>
      <div class="bg-secondary text-primary rounded-lg shadow-lg p-4 text-center flex-1 max-w-xs mb-5">
        <h2 class="text-2xl font-extrabold mb-2">PREMIUM<br />PLAN</h2>
        <p class="text-xl mb-4">$4.99/MONTH</p>
        <button class="bg-primary text-secondary py-2 px-4 rounded transition-colors duration-300 hover:bg-tertiary">GET STARTED</button>
        <ul class="list-disc mt-4">
          <li>Acceso completo</li>
          <li>Hasta 5 usuarios</li>
          <li>Soporte por chat</li>
        </ul>
      </div>
      <div class="bg-secondary text-primary rounded-lg shadow-lg p-4 text-center flex-1 max-w-xs mb-5">
        <h2 class="text-2xl font-extrabold mb-2">PRO<br />PLAN</h2>
        <p class="text-xl mb-4">$4.99/MONTH</p>
        <button class="bg-primary text-secondary py-2 px-4 rounded transition-colors duration-300 hover:bg-tertiary">GET STARTED</button>
        <ul class="list-disc mt-4">
          <li>Acceso completo</li>
          <li>Usuarios ilimitados</li>
          <li>Soporte prioritario</li>
        </ul>
      </div>
    </div>
    <pricingPlans></pricingPlans>
  </div>
</template>

