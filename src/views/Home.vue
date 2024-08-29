<script setup lang="ts">
import Plans from '../components/Plans.vue';
import Midi from '../components/Midi.vue';
</script>

<template>
  <section>
    <div>
      <Midi></Midi>
    </div>
  </section>
  <section>
    <div id="aboutus" class="py-0 mb-5">
      <div class="flex flex-col md:flex-row items-center justify-between">
        <div class="md:w-1/2 px-4 md:px-12 text-primary">
          <h1 class="text-3xl mb-4">About us</h1>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. A consequatur labore earum quae, ducimus sapiente
            suscipit, odit atque ab error veniam officiis ex distinctio repellat. Qui a accusamus molestiae ipsam.</p>
        </div>
        <div class="md:w-1/2 relative overflow-hidden">
          <img class="w-full h-auto object-cover"
            src="https://myscena.org/wp-content/uploads/2021/10/Beethoven_X_Header-e1635204954120.jpg"
            alt="A representation of Beethoven" />
        </div>
      </div>
    </div>
  </section>
  <section>
    <div>
      <Plans></Plans>
    </div>
  </section>
</template>