<template>
    <NavbarAdmin />
    <main>
      <div class="max-w-[1200px] mx-auto">
        <router-view />
      </div>
    </main>
  </template>
  
  <script setup>
  import NavbarAdmin from "../components/NavbarAdmin.vue";
  </script>
  