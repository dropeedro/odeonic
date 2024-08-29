<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-md w-96">
      <h1 class="text-3xl font-bold text-purple-600 mb-6">ODEONIC</h1>
      <h2 class="text-xl font-semibold mb-2">Register form</h2>
      <p class="text-sm text-gray-600 mb-6">Remember not to show your password to anyone!</p>

      <form @submit.prevent="handleRegister">
        <div class="grid grid-cols-2 gap-4 mb-4">
          <input type="text" v-model="firstName" placeholder="First Name" class="px-3 py-2 border rounded-md" required>
          <input type="text" v-model="lastName" placeholder="Last Name" class="px-3 py-2 border rounded-md" required>
        </div>
        <div class="grid grid-cols-2 gap-4 mb-4">
          <input type="text" v-model="birthDate" placeholder="Birth Date" class="px-3 py-2 border rounded-md" required>
          <input type="text" v-model="country" placeholder="Country" class="px-3 py-2 border rounded-md" required>
        </div>
        <div class="grid grid-cols-2 gap-4 mb-4">
          <input type="text" v-model="gender" placeholder="Gender" class="px-3 py-2 border rounded-md" required>
          <input type="text" v-model="language" placeholder="Language" class="px-3 py-2 border rounded-md" required>
        </div>
        <div class="mb-4">
          <input type="email" v-model="email" placeholder="Email" class="w-full px-3 py-2 border rounded-md" required>
        </div>
        <div class="mb-6">
          <input type="password" v-model="password" placeholder="Password" class="w-full px-3 py-2 border rounded-md"
            required>
        </div>
        <button type="submit"
          class="w-full bg-purple-600 text-white py-2 rounded-md hover:bg-purple-700 transition duration-300">Register</button>
      </form>

      <div class="mt-6 text-center">
        <p class="text-sm text-gray-600">You want to go back?</p>
        <a href="#" class="text-2xl">📷</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      firstName: '',
      lastName: '',
      birthDate: '',
      country: '',
      gender: '',
      language: '',
      email: '',
      password: ''
    }
  },
  methods: {
    handleRegister() {
      // Handle registration logic here
      console.log('Registration attempted with:', this.$data)
    }
  }
}
</script>