<template>
    <div>
      <h2>¡Pago Exitoso!</h2>
      <p>Gracias por tu compra. La descarga comenzará en breve...</p>
    </div>
  </template>
  
  <script>
  export default {
    async mounted() {
      const urlParams = new URLSearchParams(window.location.search);
      const songId = urlParams.get('song_id');
  
      if (songId) {
        // Redirigir al backend para descargar la canción
        window.location.href = `http://localhost:8000/stripe/download-song?song_id=${songId}`;
      }
    }
  };
  </script>
  