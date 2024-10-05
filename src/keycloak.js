import Keycloak from 'keycloak-js';

const keycloak = new Keycloak({
  url: 'http://localhost:8080',  // URL del servidor Keycloak
  realm: 'odeonic-app',          // Nombre del Realm
  clientId: 'frontend',          // Client ID configurado en Keycloak
});

export default keycloak;
