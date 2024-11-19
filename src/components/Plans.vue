<script setup lang="ts">
import { ref } from "vue";

const pricingPlans = ref([
  {
    name: "Personal",
    price: "$5",
    description: "Perfect for using in a personal website or a client project.",
    features: {
      users: "1 User",
      components: "All UI components",
      access: "Lifetime access",
      updates: "Free updates",
      projects: "Use on 1 (one) project",
      support: "3 Months support",
    },
    button: {
      text: "Choose Personal",
    },
  },
  {
    name: "Business",
    price: "$20",
    description: "Perfect for using in a Business website or a client project.",
    features: {
      users: "5 Users",
      components: "All UI components",
      access: "Lifetime access",
      updates: "Free updates",
      projects: "Use on 3 (Three) projects",
      support: "4 Months support",
    },
    button: {
      text: "Choose Business",
    },
  },
]);
</script>

<template>
  <section
    class="relative z-10 overflow-hidden bg-backgroundColor pt-12 pb-8 lg:pt-20 lg:pb-12"
  >
    <div class="container mx-auto px-4">
      <!-- Título de la sección -->
      <div class="text-center mb-10">
        <h2
          class="text-2xl font-bold text-PrimaryColor sm:text-3xl md:text-4xl"
        >
          Our Pricing Plan
        </h2>
        <p class="mt-4 text-sm text-SecondaryColor sm:text-base">
          We offer a variety of plans to suit your needs and budget. Choose the
          plan that best fits your musical goals and start exploring everything
          our platform has to offer.
        </p>
      </div>

      <!-- Tarjetas de planes -->
      <div class="flex flex-wrap justify-center gap-6">
        <div
          v-for="(plan, index) in pricingPlans"
          :key="index"
          class="w-full sm:w-[calc(50%-12px)] lg:w-[calc(33.333%-16px)]"
        >
          <div
            class="relative z-10 mb-6 overflow-hidden rounded-lg border-2 border-stroke bg-backgroundColor p-6 transition-transform hover:scale-105 sm:p-8"
          >
            <span class="block text-lg font-semibold text-PrimaryColor">
              {{ plan.name }}
            </span>
            <h2 class="mt-3 text-4xl font-bold text-dark">
              <span class="text-PrimaryColor">{{ plan.price }}</span>
              <span class="text-base text-SecondaryColor font-normal">
                / month
              </span>
            </h2>
            <p
              class="mt-4 border-b border-stroke pb-4 text-sm text-SecondaryColor"
            >
              {{ plan.description }}
            </p>
            <div class="mt-6 space-y-2 text-sm text-SecondaryColor">
              <p>{{ plan.features.users }}</p>
              <p>{{ plan.features.components }}</p>
              <p>{{ plan.features.access }}</p>
              <p>{{ plan.features.updates }}</p>
              <p>{{ plan.features.projects }}</p>
              <p>{{ plan.features.support }}</p>
            </div>
            <a
              href="#"
              class="mt-6 block w-full rounded-md border border-PrimaryColor bg-PrimaryColor py-3 text-center text-sm font-medium text-SecondaryColor transition hover:bg-yellow-300 hover:border-yellow-300"
            >
              {{ plan.button.text }}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
