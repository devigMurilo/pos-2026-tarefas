import './style.css'
import { buscarPessoas, buscarNave, buscarPlaneta} from './wapper.js'


document.querySelector('#app').innerHTML = `
<section id="center">
  <div class="hero">
    <h1>Star Wars </h1>
    <h1>Personagens/Planetas/Naves</h1>
  </div>
  <div id="spacer">
    <button id="buscar-personagem" type="button" class="counter">personagens </button>

    <button id="buscar-planeta" type="button" class="counter">planetas </button>

    <button id="buscar-nave" type="button" class="counter">naves </button>
  </div>
  <div id="resultado">
  </div>

</section>
`

buscarPessoas(document.getElementById('buscar-personagem'))
buscarPlaneta(document.getElementById('buscar-planeta'))
buscarNave(document.getElementById('buscar-nave'))