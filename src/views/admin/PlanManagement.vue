<template>
  <div class="admin-dashboard">
    <div class="dashboard-content">
      <div class="plan-management">
        <div class="section-header">
          <h1 class="text-3xl font-bold mb-6">Plan Management</h1>
        </div>

        <!-- Formulario para agregar nuevo plan -->
        <div class="plan-form bg-white p-8 rounded-lg shadow-lg mb-10">
          <h2 class="text-2xl font-semibold mb-4">Add New Plan</h2>
          <input
            v-model="newPlanName"
            placeholder="Plan Name"
            class="input-field mb-4 border-2 border-gray-300 p-3 rounded-lg w-full"
          />
          <input
            v-model.number="newPlanPrice"
            type="number"
            placeholder="Plan Price (USD)"
            class="input-field mb-4 border-2 border-gray-300 p-3 rounded-lg w-full"
          />
          <textarea
            v-model="newPlanDescription"
            placeholder="Plan Description"
            class="input-field mb-4 border-2 border-gray-300 p-3 rounded-lg w-full"
          ></textarea>
          <button
            @click="createPlan"
            class="primary-btn w-full py-3 text-white bg-green-500 hover:bg-green-600 rounded-md"
          >
            Add Plan
          </button>
        </div>

        <!-- Listado de planes disponibles -->
        <div class="plans-list">
          <h1 class="text-3xl font-bold mb-6">Available Plans</h1>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div
              v-for="plan in plans"
              :key="plan._id"
              class="plan-card relative z-10 mb-10 overflow-hidden rounded-lg border-2 border-gray-300 bg-white py-10 px-8 shadow-lg transition-transform duration-300 hover:transform hover:translate-y-1"
            >
              <span
                class="mb-3 block text-lg font-semibold text-primaryPurpleColor"
                >{{ plan.name }}</span
              >
              <h2 class="mb-5 text-4xl font-bold text-gray-900">
                <span class="text-primaryPurpleColor">${{ plan.price }}</span>
                <span class="text-base font-medium text-gray-500">
                  / month
                </span>
              </h2>
              <p
                class="mb-8 border-b border-gray-300 pb-8 text-base text-gray-600"
              >
                {{ plan.description }}
              </p>
              <div class="flex justify-between mt-6">
                <button
                  @click="editPlan(plan)"
                  class="edit-btn text-white bg-yellow-500 hover:bg-yellow-600 px-4 py-2 rounded-md"
                >
                  Edit
                </button>
                <button
                  @click="deletePlan(plan._id)"
                  class="delete-btn text-white bg-red-500 hover:bg-red-600 px-4 py-2 rounded-md"
                >
                  Delete
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Formulario para editar plan -->
        <div
          v-if="selectedPlan"
          class="edit-form bg-white p-8 rounded-lg shadow-lg mt-10"
        >
          <h2 class="text-2xl font-semibold mb-4">Edit Plan</h2>
          <input
            v-model="selectedPlan.name"
            placeholder="Plan Name"
            class="input-field mb-4 border-2 border-gray-300 p-3 rounded-lg w-full"
          />
          <input
            v-model.number="selectedPlan.price"
            type="number"
            placeholder="Plan Price (USD)"
            class="input-field mb-4 border-2 border-gray-300 p-3 rounded-lg w-full"
          />
          <textarea
            v-model="selectedPlan.description"
            placeholder="Plan Description"
            class="input-field mb-4 border-2 border-gray-300 p-3 rounded-lg w-full"
          ></textarea>
          <button
            @click="updatePlan"
            class="primary-btn w-full py-3 text-white bg-green-500 hover:bg-green-600 rounded-md mb-2"
          >
            Save Changes
          </button>
          <button
            @click="cancelEdit"
            class="secondary-btn w-full py-3 text-white bg-gray-400 hover:bg-gray-500 rounded-md"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "../../axios";

export default {
  name: "PlanManagement",
  data() {
    return {
      plans: [],
      newPlanName: "",
      newPlanPrice: "",
      newPlanDescription: "",
      selectedPlan: null,
    };
  },
  mounted() {
    this.fetchPlans();
  },
  methods: {
    async fetchPlans() {
      try {
        const response = await axios.get("/plans");
        this.plans = response.data;
      } catch (error) {
        console.error("Error fetching plans:", error);
      }
    },
    async createPlan() {
      if (!this.newPlanName || !this.newPlanPrice || !this.newPlanDescription) {
        alert("Please fill all fields");
        return;
      }

      try {
        const newPlan = {
          name: this.newPlanName,
          price: this.newPlanPrice,
          description: this.newPlanDescription,
        };
        await axios.post("/plans", newPlan);
        this.fetchPlans();
        this.newPlanName = "";
        this.newPlanPrice = "";
        this.newPlanDescription = "";
      } catch (error) {
        console.error("Error creating plan:", error);
      }
    },
    editPlan(plan) {
      this.selectedPlan = { ...plan };
    },
    async updatePlan() {
      if (!this.selectedPlan || !this.selectedPlan._id) return;

      try {
        await axios.put(`/plans/${this.selectedPlan._id}`, {
          name: this.selectedPlan.name,
          price: this.selectedPlan.price,
          description: this.selectedPlan.description,
        });
        this.fetchPlans();
        this.selectedPlan = null;
      } catch (error) {
        console.error("Error updating plan:", error);
      }
    },
    async deletePlan(planId) {
      if (!confirm("Are you sure you want to delete this plan?")) return;

      try {
        await axios.delete(`/plans/${planId}`);
        this.fetchPlans();
      } catch (error) {
        console.error("Error deleting plan:", error);
      }
    },
    cancelEdit() {
      this.selectedPlan = null;
    },
  },
};
</script>
