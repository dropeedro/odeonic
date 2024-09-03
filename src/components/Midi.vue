<template>
  <div class="min-h-screen flex items-center justify-center">
    <div class="p-2 rounded-lg max-w-3xl w-full">
      <!-- TITLE -->
      <div class="mx-auto mb-[60px] max-w-[510px] text-center">
        <h2 class="mb-3 text-3xl leading-[1.208] font-bold text-dark sm:text-4xl md:text-[40px]">
          Let's Generate!
        </h2>
        <p class="text-base text-body-color">
          We invite you to experiment with our innovative music generator, which uses adjustable parameters to create
          unique melodies and harmonies.
        </p>
      </div>

      <div class="flex justify-between items-start space-x-4"> <!-- Añadido espacio entre divs -->

        <!-- GENERATE MUSIC -->
        <div class="bg-secondaryWhiteColor p-6 rounded-lg w-full max-w-md">
          <h2 class="text-lg font-semibold mb-2">What's your content?</h2>
          <div class="flex items-center bg-gray-200 rounded-md mb-4">
            <input type="text" value="Party" class="bg-transparent p-2 flex-grow" />
            <button class="bg-primaryPurpleColor text-secondaryWhiteColor p-2 rounded-r-md">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>
          </div>

          <h2 class="text-lg font-semibold mb-2">How much music?</h2>
          <div class="flex items-center bg-gray-200 rounded-md mb-4">
            <input type="text" value="30" class="bg-transparent p-2 w-16" />
            <button class="bg-primaryPurpleColor text-secondaryWhiteColor p-2 rounded-md mx-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            <span class="flex-grow">Seconds</span>
          </div>

          <h2 class="text-lg font-semibold mb-4">Find your Groove</h2>
          <div v-for="(item, index) in ['Chilled', 'Weird', 'Barbeque']" :key="index"
            class="flex items-center justify-between mb-4">
            <span>{{ item }}</span>
            <input type="range" class="w-1/2" />
            <span>{{ ['Wild', 'Formal', 'Dance'][index] }}</span>
          </div>

          <h2 class="text-lg font-semibold mb-2">Do you want to hear a preview?</h2>
          <button class="bg-primaryPurpleColor text-secondaryWhiteColor p-1 rounded-md w-full">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 mx-auto" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </button>
        </div>

        <!-- SHARE MUSIC -->
        <div class="bg-secondaryWhiteColor p-7 rounded-lg shadow-2xl w-full max-w-md">
          <h2 class="text-lg font-bold text-primaryPurpleColor mb-2">Like it? Keep it!</h2>
          <button class="bg-gray-200 p-2 rounded-md mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
          </button>
          <h3 class="text-lg font-bold text-primaryPurpleColor mb-2">Share it</h3>
          <div class="flex space-x-2">
            <button class="bg-gray-200 p-2 rounded-md">
              <img src="../assets/InstagramIcon.svg" alt="Instagram icon" class="h-12 w-12" />
            </button>
            <button class="bg-gray-200 p-2 rounded-md">
              <img src="../assets/TiktokIcon.svg" alt="TikTok icon" class="h-12 w-12" />
            </button>
            <button class="bg-gray-200 p-2 rounded-md">
              <img src="../assets/XIcon.svg" alt="Twitter icon" class="h-11 w-12" />
            </button>
            <button class="bg-gray-200 p-2 rounded-md">
              <img src="../assets/FacebookIcon.svg" alt="Facebook icon" class="h-12 w-12" />
            </button>
          </div>
          <h3 class="font-bold text-primaryPurpleColor mt-4 mb-1 text-lg">And that's not all</h3>
          <p class="text-sm text-primaryPurpleColor mb-4">Unlock more features when you create an account</p>
          <button
            class="bg-primaryPurpleColor text-secondaryWhiteColor py-4 px-4 rounded-md w-full mb-2 font-semibold">Create
            a free Account</button>
          <p class="text-sm text-center">
            <a href="#" class="text-primaryPurpleColor">You already have an account?</a>
          </p>
          <p class="text-lg text-center text-primaryPurpleColor font-semibold p-2">Log In</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OdeonicInterface'
}
</script>
