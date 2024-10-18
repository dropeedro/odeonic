<template>
    <div class="admin-dashboard">
      <AdminSidebar />
      <div class="dashboard-content">
        <div class="plan-management">
          <div class="section-header">
            <h1 class="text-3xl font-bold mb-6">Plan Management</h1>
          </div>
  
          <!-- Formulario para agregar nuevo plan -->
          <div class="plan-form bg-white p-8 rounded-lg shadow-lg mb-10">
            <h2 class="text-2xl font-semibold mb-4">Add New Plan</h2>
            <input v-model="newPlanName" placeholder="Plan Name" class="input-field mb-4" />
            <input v-model.number="newPlanPrice" type="number" placeholder="Plan Price (USD)" class="input-field mb-4" />
            <textarea v-model="newPlanDescription" placeholder="Plan Description" class="input-field mb-4"></textarea>
            <button @click="createPlan" class="primary-btn w-full">Add Plan</button>
          </div>
  
          <!-- Listado de planes disponibles -->
          <div class="plans-list">
            <h2 class="text-2xl font-semibold mb-4">Available Plans</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <div v-for="plan in plans" :key="plan._id" class="plan-card relative z-10 mb-10 overflow-hidden rounded-[10px] border-2 border-stroke bg-secondaryWhiteColor py-10 px-8 shadow-pricing sm:p-12 lg:py-10 lg:px-6 xl:p-[50px]">
                <span class="mb-3 block text-lg font-semibold text-primaryPurpleColor">{{ plan.name }}</span>
                <h2 class="mb-5 text-[42px] font-bold text-dark">
                  <span class="text-primaryPurpleColor">${{ plan.price }}</span>
                  <span class="text-base font-medium text-body-color"> / month </span>
                </h2>
                <p class="mb-8 border-b border-stroke pb-8 text-base text-body-color">{{ plan.description }}</p>
                <div class="flex justify-between mt-6">
                  <button @click="editPlan(plan)" class="edit-btn">Edit</button>
                  <button @click="deletePlan(plan._id)" class="delete-btn">Delete</button>
                </div>
              </div>
            </div>
          </div>
  
          <!-- Formulario para editar plan -->
          <div v-if="selectedPlan" class="edit-form bg-white p-8 rounded-lg shadow-lg mt-10">
            <h2 class="text-2xl font-semibold mb-4">Edit Plan</h2>
            <input v-model="selectedPlan.name" placeholder="Plan Name" class="input-field mb-4" />
            <input v-model.number="selectedPlan.price" type="number" placeholder="Plan Price (USD)" class="input-field mb-4" />
            <textarea v-model="selectedPlan.description" placeholder="Plan Description" class="input-field mb-4"></textarea>
            <button @click="updatePlan" class="primary-btn w-full mb-2">Save Changes</button>
            <button @click="cancelEdit" class="secondary-btn w-full">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from '../../axios';
  import AdminSidebar from '../Admin/AdminSidebar.vue';
  
  export default {
    name: 'PlanManagement',
    components: {
      AdminSidebar,
    },
    data() {
      return {
        plans: [],
        newPlanName: '',
        newPlanPrice: '',
        newPlanDescription: '',
        selectedPlan: null,
      };
    },
    mounted() {
      this.fetchPlans();
    },
    methods: {
      async fetchPlans() {
        try {
          const response = await axios.get('/plans');
          this.plans = response.data;
        } catch (error) {
          console.error('Error fetching plans:', error);
        }
      },
      async createPlan() {
        if (!this.newPlanName || !this.newPlanPrice || !this.newPlanDescription) {
          alert('Please fill all fields');
          return;
        }
  
        try {
          const newPlan = {
            name: this.newPlanName,
            price: this.newPlanPrice,
            description: this.newPlanDescription,
          };
          await axios.post('/plans', newPlan);
          this.fetchPlans();
          this.newPlanName = '';
          this.newPlanPrice = '';
          this.newPlanDescription = '';
        } catch (error) {
          console.error('Error creating plan:', error);
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
          console.error('Error updating plan:', error);
        }
      },
      async deletePlan(planId) {
        if (!confirm('Are you sure you want to delete this plan?')) return;
  
        try {
          await axios.delete(`/plans/${planId}`);
          this.fetchPlans();
        } catch (error) {
          console.error('Error deleting plan:', error);
        }
      },
      cancelEdit() {
        this.selectedPlan = null;
      },
    },
  };
  </script>
  
  <style scoped>
  /* Estilos actualizados */
  .admin-dashboard {
    display: flex;
  }
  
  .dashboard-content {
    padding: 20px;
    flex-grow: 1;
    background-color: #f9f9f9;
  }
  
  .plan-form,
  .edit-form {
    background-color: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 30px;
  }
  
  .plans-list {
    margin-top: 30px;
  }
  
  .plan-card {
    border: 2px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    transition: transform 0.3s, box-shadow 0.3s;
    background-color: #ffffff;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  }
  
  .plan-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  }
  
  .input-field {
    display: block;
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  .primary-btn {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .primary-btn:hover {
    background-color: #45a049;
  }
  
  .secondary-btn {
    background-color: #ccc;
    color: #333;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .secondary-btn:hover {
    background-color: #bbb;
  }
  
  .edit-btn {
    background-color: #ffa500;
    color: white;
    padding: 6px 12px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .edit-btn:hover {
    background-color: #ff8c00;
  }
  
  .delete-btn {
    background-color: #d9534f;
    color: white;
    padding: 6px 12px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .delete-btn:hover {
    background-color: #c9302c;
  }
  </style>
  