import Keycloak from 'keycloak-js';

const keycloak = new Keycloak({
  url: 'http://localhost:8080',  // URL del servidor Keycloak
  realm: 'odeonic-app',          // Nombre del Realm
  clientId: 'frontend',        // Client ID configurado en Keycloak
});

let isKeycloakInitialized = false; // Variable para rastrear el estado de inicialización

const initKeycloak = () => {
  // Retorna una promesa que se resuelve o rechaza dependiendo del estado de inicialización
  return new Promise((resolve, reject) => {
    if (isKeycloakInitialized) {
      resolve(); // Ya está inicializado
      return;
    }

    keycloak.init({
      onLoad: 'check-sso', // Cambia esto si necesitas que inicie sesión al cargar
      checkLoginIframe: false,
      silentCheckSsoRedirectUri: window.location.origin + '/silent-check-sso.html',
      responseMode: 'query',  
    })
    .then((authenticated) => {
      if (authenticated) {
        console.log("Keycloak authenticated");
      } else {
        console.warn("User is not authenticated");
      }
      isKeycloakInitialized = true; // Marca como inicializado
      resolve(); // Resuelve la promesa
    })
    .catch((error) => {
      console.error("Keycloak initialization failed", error);
      reject(error); // Rechaza la promesa
    });
  });
};

export { keycloak, initKeycloak };
