<!-- views/Home.vue -->
<script setup>
import Plans from '../components/Plans.vue';
import Midi from '../components/Midi.vue';
</script>

<template>
  <div>
    <section id="midi">
      <div>
        <Midi></Midi>
      </div>
    </section>
    <section id="about">
      <div class="w-full px-4">
        <div class="mx-auto mb-[60px] max-w-[510px] text-center">
          <h2 class="mb-3 text-3xl leading-[1.208] font-bold text-dark sm:text-4xl md:text-[40px]">
            About Us
          </h2>
          <p class="text-base text-body-color text-center">We offer an innovative platform for generating music with our
            Virtual MIDI. Designed for musicians of all levels and casual users, our service allows you to create unique
            melodies and harmonies intuitively, without the need for advanced technical knowledge.
          </p>
        </div>
        <div class="w-full overflow-hidden rounded-[10px]">
          <img src="../assets/aboutusimage.jpg" alt="About Us" class="w-full object-cover">
        </div>
      </div>
    </section>
    <section id="plans">
      <div>
        <Plans></Plans>
      </div>
    </section>
  </div>
</template>
