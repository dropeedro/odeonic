<template>
  <header
    class="bg-SecondaryColor sticky top-0 shadow-md flex items-center justify-center px-8 py-2 z-50"
  >
    <div class="flex w-full max-w-6xl justify-between items-center">
      <!-- logo -->
      <h1 class="flex-shrink-0">
        <a href="/">
          <img
            src="../assets/riffname.svg"
            alt="logo"
            class="mx-auto max-w-[180px]"
          />
        </a>
      </h1>
      <!-- navigation -->
      <nav class="font-semibold text-md flex-grow">
        <ul
          class="flex items-center justify-center space-x-4 text-PrimaryColor hover:text-PrimaryColorDark duration-200"
        >
          <li
            class="p-4 border-b-2 border-PrimaryColor border-opacity-0 hover:border-opacity-100 hover:text-PrimaryColorDark text-PrimaryColor duration-200 cursor-pointer"
          >
            <router-link to="/admin">Dashboard</router-link>
          </li>
          <li
            class="p-4 border-b-2 border-PrimaryColor border-opacity-0 hover:border-opacity-100 hover:text-PrimaryColorDark text-PrimaryColor duration-200 cursor-pointer"
          >
            <router-link to="/admin/plans">Plans</router-link>
          </li>
          <li
            class="p-4 border-b-2 border-PrimaryColor border-opacity-0 hover:border-opacity-100 hover:text-PrimaryColorDark text-PrimaryColor duration-200 cursor-pointer"
          >
            <router-link to="/admin/users">Users</router-link>
          </li>
        </ul>
      </nav>
      <!-- profile icon with dropdown -->
      <div class="relative" ref="dropdownRef">
        <a
          href="#"
          @click="toggleDropdown"
          class="flex items-center justify-center text-PrimaryColor hover:text-PrimaryColorDark duration-200 cursor-pointer"
        >
          <svg
            class="h-10 p-1"
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
            focusable="false"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            fill="none"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <path stroke="none" d="M0 0h24v24H0z" fill="none" />
            <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
            <path d="M12 10m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0" />
            <path
              d="M6.168 18.849a4 4 0 0 1 3.832 -2.849h4a4 4 0 0 1 3.834 2.855"
            />
          </svg>
        </a>
        <!-- Dropdown menu -->
        <div
          v-if="isDropdownOpen"
          class="absolute right-0 mt-2 w-48 bg-white border border-gray-200 rounded-md shadow-lg z-10"
        >
          <button
            @click="openModal"
            class="block w-full rounded-md px-4 py-2 text-left text-SecondaryColor hover:bg-PrimaryColor hover:text-SecondaryColor duration-200"
          >
            Cerrar sesión
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Modal -->
  <div
    v-if="isModalOpen"
    class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50"
    @click="closeModal"
  >
    <div class="bg-backgroundColor p-6 rounded-lg w-80" @click.stop>
      <h3 class="text-lg font-semibold text-center mb-4 text-SecondaryColor">
        ¿Estás seguro de que quieres cerrar sesión?
      </h3>
      <div class="flex justify-between">
        <button
          @click="logout"
          class="bg-PrimaryColor text-backgroundColor px-4 py-2 rounded-lg hover:bg-PrimaryColorDark"
        >
          Sí
        </button>
        <button
          @click="closeModal"
          class="bg-plusGrayColor text-SecondaryColor px-4 py-2 rounded-lg hover:bg-gray-400"
        >
          No
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";

const isDropdownOpen = ref(false);
const isModalOpen = ref(false);
const dropdownRef = ref(null);

// Función para alternar el estado del dropdown
function toggleDropdown() {
  isDropdownOpen.value = !isDropdownOpen.value;
}

// Función para abrir el modal de confirmación
function openModal() {
  isModalOpen.value = true;
  isDropdownOpen.value = false; // Cierra el dropdown cuando se abre el modal
}

// Función para cerrar el modal
function closeModal() {
  isModalOpen.value = false;
}

// Función para cerrar sesión
function logout() {
  console.log("Cerrar sesión");
  closeModal();
}

// Detectar clic fuera del dropdown para cerrarlo
function handleClickOutside(event) {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
    isDropdownOpen.value = false;
  }
}

// Configuración de eventos al montar y desmontar el componente
onMounted(() => {
  document.addEventListener("click", handleClickOutside);
});

onBeforeUnmount(() => {
  document.removeEventListener("click", handleClickOutside);
});
</script>

<style scoped>
/* Opcional: Ajustar estilos según sea necesario */
</style>
