window.onload = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        position => {
          console.log('Localização capturada:', position.coords);
  
          fetch('/save_location', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              latitude: position.coords.latitude,
              longitude: position.coords.longitude
            })
          })
          .then(res => res.json())
          .then(data => {
            console.log('Resposta do servidor:', data);
          })
          .catch(err => {
            console.error('Erro ao enviar localização:', err);
          });
        },
        error => {
          console.error('Erro ao capturar localização:', error);
        }
      );
    } else {
      alert('Seu navegador não suporta geolocalização.');
    }
  };
  