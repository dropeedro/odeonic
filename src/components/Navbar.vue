<template>
  <header class="header sticky top-0 bg-white shadow-md flex items-center justify-between px-8 py-2 z-50">
    <!-- logo -->
    <h1 class="w-3/12">
      <a href="/">
        <img src="../assets/ODEONICLOGO.png" alt="logo" class="mx-auto inline-block max-w-[180px]"/>
      </a>
    </h1>
    <!-- navigation -->
    <nav class="nav font-semibold text-lg">
      <ul class="flex items-center">
        <li
          class="p-4 border-b-2 border-purple-900 border-opacity-0 hover:border-opacity-100 hover:text-purple-900 duration-200 cursor-pointer active">
          <a href="/">Home</a>
        </li>
        <li
          class="p-4 border-b-2 border-purple-900 border-opacity-0 hover:border-opacity-100 hover:text-purple-900 duration-200 cursor-pointer">
          <a href="">About</a>
        </li>
        <li
          class="p-4 border-b-2 border-purple-900 border-opacity-0 hover:border-opacity-100 hover:text-purple-900 duration-200 cursor-pointer">
          <a href="">Generate</a>
        </li>
        <li
          class="p-4 border-b-2 border-purple-900 border-opacity-0 hover:border-opacity-100 hover:text-purple-900 duration-200 cursor-pointer">
          <a href="">Pricing Plans</a>
        </li>
      </ul>
    </nav>

    <!-- buttons -->
    <div class="w-3/12 flex justify-end">
      <a href="">
        <svg class="h-10 p-1 mr-2 hover:text-purple-900 duration-200" xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true" focusable="false" viewBox="0 0 25 25" stroke-width="1.5" stroke="currentColor" fill="none"
          stroke-linecap="round" stroke-linejoin="round">
          <path stroke="none" d="M0 0h24v24H0z" fill="none" />
          <path
            d="M6.331 8h11.339a2 2 0 0 1 1.977 2.304l-1.255 8.152a3 3 0 0 1 -2.966 2.544h-6.852a3 3 0 0 1 -2.965 -2.544l-1.255 -8.152a2 2 0 0 1 1.977 -2.304z" />
          <path d="M9 11v-5a3 3 0 0 1 6 0v5" />
        </svg>
      </a>
      <a href="/login">
        <svg class="h-10 p-1 ml-2 hover:text-purple-900 duration-200" xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true" focusable="false" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none"
          stroke-linecap="round" stroke-linejoin="round">
          <path stroke="none" d="M0 0h24v24H0z" fill="none" />
          <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0" />
          <path d="M12 10m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0" />
          <path d="M6.168 18.849a4 4 0 0 1 3.832 -2.849h4a4 4 0 0 1 3.834 2.855" />
        </svg>
      </a>
    </div>
  </header>
</template>
