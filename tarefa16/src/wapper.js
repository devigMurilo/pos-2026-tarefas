import { getPessoas, getNave, getPlaneta } from './api.js'


function renderizarPessoas(container, pessoas) {
    container.innerHTML = pessoas.map((pessoa) => `<p>${pessoa.name}</p>`).join('')
}
function renderizarNaves(container, naves) {
    container.innerHTML = naves.map((nave) => `<p>${nave.name}</p>`).join('')
}
function renderizarPlanetas(container ,planetas) {
    container.innerHTML = planetas.map((planeta) => `<p>${planeta.name}</p>`).join('')
}


export function buscarPessoas(botao) {
    botao.addEventListener('click', async () => {
        const container = document.getElementById('resultado')
        container.innerHTML = ' <p>carregando...</p>'
        try {
            const data = await getPessoas()
            renderizarPessoas(container, data.results)
        } catch (error) {
            container.innerHTML = '<p>Erro ao buscar personagens. Por favor, tente novamente.</p>'
        }
        }
        
    )
}

export function buscarNave(botao) {
    botao.addEventListener('click', async () => {
        const container = document.getElementById('resultado')
        container.innerHTML = ' <p>carregando...</p>'
        try {
            const data = await getNave()
            renderizarNaves(container, data.results)
        } catch (error) {
            container.innerHTML = '<p>Erro ao buscar naves. Por favor, tente novamente.</p>'
        }
    })
}

export function buscarPlaneta(botao) {
    botao.addEventListener('click', async () => {
        const container = document.getElementById('resultado')
        container.innerHTML = ' <p>carregando...</p>' 
        try {
            const data = await getPlaneta()
            renderizarPlanetas(container, data.results)
        } catch (error) {
            container.innerHTML = '<p>Erro ao buscar planetas. Por favor, tente novamente.</p>'
        }
    })
}