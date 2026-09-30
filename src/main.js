const botao = document.getElementById('botao');
const entrada = document.getElementById('entrada');
const combo = document.getElementById('combo');
const texto1 = document.getElementById('texto1');
const texto2 = document.getElementById('texto2');

botao.addEventListener('click', () => {
  texto1.textContent = entrada.value;
  texto2.textContent = combo.value;
});

// Foca o cursor na entrada
entrada.focus();
