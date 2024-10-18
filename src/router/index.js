import { createRouter, createWebHistory } from "vue-router";
import DefaultLayout from '../components/DefaultLayout.vue';
import AdminLayout from '../components/AdminLayout.vue';
import Home from  "../views/Home.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import AdminDashboard from "../views/admin/adminDashboard.vue";
import { keycloak } from '../keycloak'; // Asegúrate de que la ruta sea correcta

const routes = [
    {
      path: '/',
      component: DefaultLayout,
      children: [
        {
          path: '',
          name: 'Home',
          component: Home,
        },
        {
          path: 'login',
          name: 'Login',
          component: Login,
        },
        {
          path: 'register',
          name: 'Register',
          component: Register,
        }
      ]
    },
    {
      path: '/Admin',
      component: AdminLayout,
      children: [
        {
          path: '', 
          name: 'AdminDashboard',
          component: AdminDashboard,
          meta: { requiresAuth: true },
        }
      ]
    }
];
  
const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
  // Verifica si la ruta requiere autenticación
  if (to.matched.some(record => record.meta.requiresAuth)) {
      // Verifica si el usuario está autenticado con Keycloak
      if (keycloak.authenticated) {
          next();  // Usuario autenticado, permite el acceso
      } else {
          // Redirige al login si no está autenticado
          next('/login');
      }
  } else {
      next();  // Si la ruta no requiere autenticación, permite el acceso
  }
});
  
export default router;

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});
