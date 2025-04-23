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


  
  async function enviarFormulario(event) {
      event.preventDefault(); // evita o recarregamento da página
      
      const formData = new FormData(document.getElementById('formulario'));
      
      const resposta = await fetch('/contato', {
          method: 'POST',
          body: formData
      });

      const data = await resposta.json();
      document.getElementById('msgform').textContent = data.mensagem;
      document.getElementById('formulario').reset(); // limpa o formulário
  }


  function mostrarAlerta(mensagem, tipo) {
    const container = document.getElementById('alerta-container');
  
    const alerta = document.createElement('div');
    alerta.className = `alert alert-${tipo} alert-dismissible fade show`;
    alerta.role = 'alert';
    alerta.innerHTML = `
      ${mensagem}
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
  
    container.innerHTML = ''; // Remove alertas anteriores
    container.appendChild(alerta);
  
    // Fecha automaticamente após 5 segundos
    setTimeout(() => {
      alerta.classList.remove('show');
      alerta.classList.add('hide');
      setTimeout(() => alerta.remove(), 300); // Espera a animação
    }, 5000);
  }
  