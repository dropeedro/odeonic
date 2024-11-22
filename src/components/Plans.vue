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
      projects: "Use on 3 (Three) project",
      support: "4 Months support",
    },
    button: {
      text: "Choose Business",
    },
  },
]);
</script>

<template>
  <!-- ====== Pricing Section Start -->
  <section
    class="relative z-10 overflow-hidden bg-backgroundColor pt-20 pb-12 lg:pt-[120px] lg:pb-[90px]"
  >
    <div class="container mx-auto">
      <div class="-mx-4 flex flex-wrap">
        <div class="w-full px-4">
          <div class="mx-auto mb-[60px] max-w-[510px] text-center">
            <h2
              class="mb-3 text-3xl leading-[1.208] font-bold text-PrimaryColor sm:text-4xl md:text-[40px]"
            >
              Our Pricing Plan
            </h2>
            <p class="text-base text-SecondaryColor">
              We offer a variety of plans to suit your needs and budget. Choose
              the plan that best fits your musical goals and start exploring
              everything our platform has to offer.
            </p>
          </div>
        </div>
      </div>
      <div class="-mx-4 flex flex-wrap justify-center">
        <div
          v-for="(plan, index) in pricingPlans"
          :key="index"
          class="w-full px-4 md:w-1/2 lg:w-1/3"
        >
          <div
            class="relative z-10 mb-10 overflow-hidden rounded-[10px] border-2 border-stroke bg-backgroundColor py-10 px-8 shadow-pricing sm:p-12 lg:py-10 lg:px-6 xl:p-[50px]"
          >
            <span class="mb-3 block text-lg font-semibold text-PrimaryColor">{{
              plan.name
            }}</span>
            <h2 class="mb-5 text-[42px] font-bold text-dark">
              <span class="text-PrimaryColor">{{ plan.price }}</span>
              <span class="text-base text-SecondaryColor font-bold">
                / month
              </span>
            </h2>
            <p
              class="mb-8 border-b border-stroke pb-8 text-base text-SecondaryColor"
            >
              {{ plan.description }}
            </p>
            <div class="mb-9 flex flex-col gap-[14px]">
              <p class="text-base text-SecondaryColor">
                {{ plan.features.users }}
              </p>
              <p class="text-base text-SecondaryColor">
                {{ plan.features.components }}
              </p>
              <p class="text-base text-SecondaryColor">
                {{ plan.features.access }}
              </p>
              <p class="text-base text-SecondaryColor">
                {{ plan.features.updates }}
              </p>
              <p class="text-base text-SecondaryColor">
                {{ plan.features.projects }}
              </p>
              <p class="text-base text-SecondaryColor">
                {{ plan.features.support }}
              </p>
            </div>
            <a
              href="javascript:void(0)"
              class="block w-full rounded-md border border-PrimaryColorDark bg-PrimaryColor text-SecondaryColor p-3 text-center text-base font-medium transition hover:bg-yellow-300 hover:border-yellow-300"
            >
              {{ plan.button.text }}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
