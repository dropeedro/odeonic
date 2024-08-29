<template>
  <div class="bg-secondaryWhiteColor min-h-screen flex items-start justify-center mt-12">
    <div class="bg-secondaryWhiteColor p-8 rounded-lg shadow-2xl w-96">
      <h2 class="pt-8 text-3xl text-primaryPurpleColor font-bold mb-2">Welcome Back!</h2>
      <p class="text-md text-primaryPurpleColor mb-6">Remember not to show your password to anyone!</p>

      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <input type="email" v-model="email" placeholder="Email" class="w-full px-3 py-2 border rounded-md" required>
        </div>
        <div>
          <input type="password" v-model="password" placeholder="Password" class="w-full px-3 py-2 border rounded-md"
            required>
        </div>
        <div class="mt-2 text-center">
          <a href="/" class="text-sm text-primaryPurpleColor">You Forgot Your Password?</a>
        </div>
        <button type="submit"
          class=" mb-2 w-full font-bold bg-plusGrayColor text-primaryPurpleColor py-2 rounded-md hover:bg-gray-300 transition duration-300">Log
          in</button>
      </form>
      <div class="mt-2 text-center text-sm text-primaryPurpleColor">
        You can also log in with
      </div>
      <div class="mb-8 mt-2 flex justify-center space-x-4">
        <a href="#" class="text-2xl">IG</a>
        <a href="#" class="text-2xl">TK</a>
        <a href="#" class="text-2xl">GO</a>
        <a href="#" class="text-2xl">FB</a>
        <a href="#" class="text-2xl">X</a>
      </div>
      <div>
        <div class="mt-4 text-center text-sm text-primaryPurpleColor">
          You don't have an account?
        </div>
        <button type="submit"
          class="mb-1 w-full font-bold bg-plusGrayColor text-primaryPurpleColor py-2 rounded-md hover:bg-gray-300 transition duration-300">Register
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    handleLogin() {
      // Handle login logic here
      console.log('Login attempted with:', this.email, this.password)
    }
  }
}
</script>