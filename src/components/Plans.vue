<template>
  <section class="relative z-10 overflow-hidden bg-backgroundColor pt-12 pb-8 lg:pt-20 lg:pb-12">
    <div class="container mx-auto px-4">
      <!-- Título de la sección -->
      <div class="text-center mb-10">
        <h2 class="text-2xl font-bold text-PrimaryColor sm:text-3xl md:text-4xl">
          Our Pricing Plan
        </h2>
        <p class="mt-4 text-sm text-SecondaryColor sm:text-base">
          We offer a variety of plans to suit your needs and budget. Choose the
          plan that best fits your musical goals and start exploring everything
          our platform has to offer.
        </p>
      </div>

      <!-- Listado de planes disponibles -->
      <div class="flex justify-center">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="plan in plans" :key="plan._id"
            class="plan-card relative z-10 mb-10 overflow-hidden rounded-lg border-2 border-plusGrayColor bg-white py-6 sm:py-8 px-6 sm:px-8 transition-transform duration-300 hover:transform hover:translate-y-1">
            <span class="mb-3 block text-lg font-semibold text-PrimaryColor">{{ plan.name }}</span>
            <h2 class="mb-5 text-2xl sm:text-4xl font-bold text-gray-900">
              <span class="text-PrimaryColor">${{ plan.price }}</span>
              <span class="text-base font-medium text-SecondaryColor">/ month</span>
            </h2>
            <p class="mb-8 border-b border-plusGrayColor pb-8 text-base text-SecondaryColor">
              {{ plan.description }}
            </p>
            <div class="features-list mb-4">
              <h3 class="font-semibold text-SecondaryColor">Features:</h3>
              <ul>
                <li v-for="(feature, index) in plan.features" :key="index" class="text-SecondaryColor">
                  • {{ feature }}
                </li>
              </ul>
            </div>
            <!-- Botón de "Choose Plan" -->
            <div class="text-center">
              <button @click="choosePlan(plan)"
                class="mt-6 px-6 py-2 bg-PrimaryColor text-SecondaryColor font-bold rounded-lg hover:bg-PrimaryColorDark transition duration-300">
                Choose Plan
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "../axios";

export default {
  name: "PricingPlans",
  data() {
    return {
      plans: [],
    };
  },
  mounted() {
    this.fetchPlans();
  },
  methods: {
    async fetchPlans() {
      try {
        const response = await axios.get("/plans");
        this.plans = response.data.map(plan => ({
          ...plan,
          features: plan.features ? plan.features.split(",") : []
        }));
      } catch (error) {
        console.error("Error fetching plans:", error);
      }
    },
    choosePlan(plan) {
      // Aquí puedes manejar el evento de selección de un plan.
      // Puedes redirigir al usuario, mostrar un modal, o realizar otra acción
      console.log("Plan chosen:", plan);
      // Ejemplo de redirección a una página de pago o detalles
      this.$router.push({ name: "PlanDetails", params: { planId: plan._id } });
    }
  }
};
</script>
