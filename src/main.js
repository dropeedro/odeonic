import { createApp } from 'vue'
import router from './router'
import './style.css'
import App from './App.vue';
import 'primeicons/primeicons.css'
import keycloak from './keycloak';

// createApp(App).use(router).mount('#app')

const app = createApp(App);
app.use(router);
app.mount('#app');

// keycloak.init({ onLoad: 'check-sso' })
//   .then(() => {
//     app.use(router);
//     app.mount('#app');
//   })
//   .catch((error) => {
//     console.error('Keycloak initialization failed', error);
//   });