<template>
  <div class="admin-dashboard">
    <div class="dashboard-content">
      <div class="plan-management">
        <div class="section-header">
          <h1 class="text-3xl font-bold mb-6 pt-10 text-SecondaryColor">
            Plan Management
          </h1>
        </div>

        <!-- Formulario para agregar nuevo plan -->
        <div
          class="plan-form bg-backgroundColor p-8 rounded-lg border-2 border-plusGrayColor mb-10"
        >
          <h2 class="text-2xl font-semibold mb-4 text-SecondaryColor">
            Add New Plan
          </h2>
          <input
            v-model="newPlanName"
            placeholder="Plan Name"
            class="input-field mb-4 border-2 border-plusGrayColor p-3 rounded-lg w-full"
          />
          <input
            v-model.number="newPlanPrice"
            type="number"
            placeholder="Plan Price (USD)"
            class="input-field mb-4 border-2 border-plusGrayColor p-3 rounded-lg w-full"
          />
          <textarea
            v-model="newPlanDescription"
            placeholder="Plan Description"
            class="input-field mb-4 border-2 border-plusGrayColor p-3 rounded-lg w-full"
          ></textarea>
          <button
            @click="createPlan"
            class="primary-btn w-full py-3 text-backgroundColor bg-green-500 hover:bg-green-600 rounded-md"
          >
            Add Plan
          </button>
        </div>

        <!-- Listado de planes disponibles -->
        <div class="plans-list">
          <h1 class="text-3xl font-bold mb-6 text-SecondaryColor">
            Available Plans
          </h1>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div
              v-for="plan in plans"
              :key="plan._id"
              class="plan-card relative z-10 mb-10 overflow-hidden rounded-lg border-2 border-plusGrayColor bg-white py-10 px-8 shadow-lg transition-transform duration-300 hover:transform hover:translate-y-1"
            >
              <span
                class="mb-3 block text-lg font-semibold text-PrimaryColor"
                >{{ plan.name }}</span
              >
              <h2 class="mb-5 text-4xl font-bold text-gray-900">
                <span class="text-PrimaryColor">${{ plan.price }}</span>
                <span class="text-base font-medium text-SecondaryColor">
                  / month
                </span>
              </h2>
              <p
                class="mb-8 border-b border-plusGrayColor pb-8 text-base text-SecondaryColor"
              >
                {{ plan.description }}
              </p>
              <div class="flex justify-between mt-6">
                <button
                  @click="editPlan(plan)"
                  class="edit-btn text-white bg-PrimaryColor hover:bg-PrimaryColorDark px-4 py-2 rounded-md"
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

        <!-- Modal de edición -->
        <div
          v-if="selectedPlan"
          class="fixed inset-0 bg-gray-800 bg-opacity-50 flex justify-center items-center z-50"
        >
          <div class="modal-content bg-white p-8 rounded-lg shadow-lg w-96">
            <h2 class="text-2xl font-semibold mb-4">Edit Plan</h2>
            <input
              v-model="selectedPlan.name"
              placeholder="Plan Name"
              class="input-field mb-4 border-2 border-plusGrayColor p-3 rounded-lg w-full"
            />
            <input
              v-model.number="selectedPlan.price"
              type="number"
              placeholder="Plan Price (USD)"
              class="input-field mb-4 border-2 border-plusGrayColor p-3 rounded-lg w-full"
            />
            <textarea
              v-model="selectedPlan.description"
              placeholder="Plan Description"
              class="input-field mb-4 border-2 border-plusGrayColor p-3 rounded-lg w-full"
            ></textarea>
            <div class="flex justify-between mt-6">
              <button
                @click="updatePlan"
                class="primary-btn py-2 px-4 text-white bg-green-500 hover:bg-green-600 rounded-md"
              >
                Save Changes
              </button>
              <button
                @click="cancelEdit"
                class="secondary-btn py-2 px-4 text-white bg-gray-400 hover:bg-gray-500 rounded-md"
              >
                Cancel
              </button>
            </div>
          </div>
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
        this.selectedPlan = null; // Close modal after update
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
      this.selectedPlan = null; // Close modal
    },
  },
};
</script>

