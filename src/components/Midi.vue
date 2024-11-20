<template>
  <div class="min-h-screen flex items-center justify-center bg-backgroundColor">
    <div class="p-2 rounded-lg max-w-3xl w-full">
      <!-- TITLE -->
      <div class="mx-auto mb-[60px] max-w-[510px] text-center">
        <h2 class="text-PrimaryColor mb-3 text-3xl leading-[1.208] font-bold text-dark sm:text-4xl md:text-[40px]">
          Let's Generate!
        </h2>
        <p class="text-base text-SecondaryColor">
          We invite you to experiment with our innovative music generator, which uses adjustable parameters to create
          unique melodies and harmonies.
        </p>
      </div>

      <div class="flex justify-between items-start space-x-4">
        <!-- GENERATE MUSIC -->
        <div class="bg-backgroundColor p-6 rounded-lg w-full max-w-md">
          <h2 class="text-lg font-semibold mb-2 text-SecondaryColor">What's your content?</h2>
          <div class="relative mb-4">
            <select class="bg-backgroundColor text-SecondaryColor p-2 flex-grow rounded-md w-full appearance-none outline-none"
              style="outline: 2px solid #D9D9D9;">
              <option value="Party">Party</option>
              <option value="Relaxing">Relaxing</option>
              <option value="Workout">Workout</option>
              <option value="Rock">Rock</option>
            </select>
            <div class="absolute right-0.5 top-1/2 transform -translate-y-1/2 bg-SecondaryColor p-2 rounded">
              <span class="text-white">&#9660;</span>
            </div>
          </div>

          <h2 class="text-lg font-semibold mb-2 text-SecondaryColor">How much music?</h2>
          <div class="relative mb-4">
            <select class="bg-backgroundColor text-SecondaryColor p-2 flex-grow rounded-md w-full appearance-none outline-none"
              style="outline: 2px solid #D9D9D9;">
              <option value="30">30 seconds</option>
              <option value="60">60 seconds</option>
              <option value="120">120 seconds</option>
            </select>
            <div class="absolute right-0.5 top-1/2 transform -translate-y-1/2 bg-SecondaryColor p-2 rounded">
              <span class="text-white">&#9660;</span>
            </div>
          </div>

          <h2 class="text-lg font-semibold mb-4 text-SecondaryColor">Find your Groove</h2>
          <div v-for="(item, index) in grooves" :key="index" class="flex items-center justify-between mb-4">
            <span>{{ item.label }}</span>
            <input type="range" class="w-1/2" v-model="grooveValues[index]" :min="item.min" :max="item.max"
              @input="handleGrooveChange(index)" />
            <span>{{ item.value }}</span>
          </div>

          <!-- Play button -->
          <h2 class="text-lg font-semibold mb-2 text-SecondaryColor">Do you want to hear a preview?</h2>
          <button @click="playSongBasedOnParameters"
            class="bg-SecondaryColor text-secondaryWhiteColor p-1 rounded-md w-full">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 mx-auto" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path v-if="isPlaying" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M10 9v6m4-6v6" />
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </button>
        </div>

        <!-- SHARE MUSIC -->
        <div class="bg-secondaryWhiteColor p-7 rounded-lg shadow-2xl w-full max-w-md">
          <h2 class="text-lg font-bold text-SecondaryColor mb-2">Like it? Keep it!</h2>
          <button @click="redirectToCheckout" class="bg-plusGrayColor p-2 rounded-md mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
          </button>
          <h3 class="text-lg font-bold text-SecondaryColor mb-2">Share it</h3>
          <div class="flex space-x-2">
            <button @click="shareOnInstagram" class="bg-plusGrayColor p-2 rounded-md">
              <img src="../assets/InstagramIcon.svg" alt="Instagram icon" class="h-12 w-12" />
            </button>
            <button @click="shareOnTikTok" class="bg-plusGrayColor p-2 rounded-md">
              <img src="../assets/TiktokIcon.svg" alt="TikTok icon" class="h-12 w-12" />
            </button>
            <button @click="shareOnTwitter" class="bg-plusGrayColor p-2 rounded-md">
              <img src="../assets/XIcon.svg" alt="Twitter icon" class="h-11 w-12" />
            </button>
            <button @click="shareOnFacebook" class="bg-plusGrayColor p-2 rounded-md">
              <img src="../assets/FacebookIcon.svg" alt="Facebook icon" class="h-12 w-12" />
            </button>
          </div>
          <h3 class="font-bold text-SecondaryColor mt-4 mb-1 text-lg">And that's not all</h3>
          <p class="text-sm text-SecondaryColor mb-4">Unlock more features when you create an account</p>
          <a href="/register"
            class="bg-SecondaryColor text-secondaryWhiteColor py-4 px-4 rounded-md w-full mb-2 font-semibold block text-center">
            Create a free Account
          </a>
          <p class="text-sm text-center">You already have an account?</p>
          <p class="text-lg text-center text-SecondaryColor font-semibold p-2">
            <a href="/login" class="text-SecondaryColor">Log In</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PaymentButton from './PaymentButton.vue';
import { loadStripe } from '@stripe/stripe-js';

export default {
  components: {
    PaymentButton,
  },
  name: 'OdeonicInterface',
  data() {
    return {
      grooveValues: [50, 50, 50],
      selectedContent: 'Party',
      selectedDuration: '30',
      audio: null,
      isPlaying: false,
      grooves: [
        { label: 'Chilled', min: 0, max: 100, value: 'Wild' },
        { label: 'Weird', min: 0, max: 100, value: 'Formal' },
        { label: 'Barbeque', min: 0, max: 100, value: 'Dance' },
      ],
    };
  },
  methods: {
    handleGrooveChange(index) {
      console.log(this.grooveValues[index]);
    },
    playSongBasedOnParameters() {
      // Código original...
    },
    async redirectToCheckout() {
      // Código original...
    },
    // Métodos para compartir en redes sociales
    shareOnInstagram() {
      alert('Instagram no permite compartir directamente desde la web.');
    },
    shareOnTikTok() {
      alert('TikTok no permite compartir directamente desde la web.');
    },
    shareOnTwitter() {
      const url = encodeURIComponent(window.location.href);
      const text = encodeURIComponent(
        '¡Escucha esta increíble música generada con nuestra app!'
      );
      const twitterShareUrl = `https://twitter.com/intent/tweet?url=${url}&text=${text}`;
      window.open(twitterShareUrl, '_blank');
    },
    shareOnFacebook() {
      const url = encodeURIComponent(window.location.href);
      const facebookShareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
      window.open(facebookShareUrl, '_blank');
    },
  },
};
</script>
