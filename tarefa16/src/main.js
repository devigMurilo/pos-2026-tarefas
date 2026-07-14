import './style.css'
import {renderizarUsers} from './wapper.js'

document.querySelector('#app').innerHTML = `
<section id="center">
  <div>
    <h1>Procurar Usuarios:</h1>
  
  </div>
  <button id="buscar-user" type="button" class="counter">Buscar Usuário</button>

  <input type="text" id="user-id" placeholder="Digite o ID do usuário" />
  <button id="buscar-post-user" type="button" class="counter">Buscar Posts</button>
</section>

<section id="next-steps">
  <div id="social">
    <ul>
      <li><a href="https://github.com/devigMurilo/" target="_blank"><svg class="button-icon" role="presentation" aria-hidden="true"><use href="/icons.svg#github-icon"></use></svg>GitHub</a></li>
    </ul>
  </div>
</section>


`


renderiazarUsers(document.querySelector('#buscar-user'))

