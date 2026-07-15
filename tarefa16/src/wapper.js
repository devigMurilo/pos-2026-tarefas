import {getUser, getPosts} from './api.js'

function renderUser(user, container) {
    container.innerHTML = `
    <h2>Usuários:</h2>
    <li>
        ${user.map(u => `<li>${u.name} - ${u.id}</li>`).join('')}
    </li>
    `
}




export async function renderizarUsers(botao, container,) {
    botao.addEventListener('click', async () => {
        const container = document.getElementById('resultado')
        container.innerHTML = '<p>Carregando...</p>'
        try {
            const data = await getUser()
            renderUser(data, container)
        }
        catch (error) {
            container.innerHTML = '<p>Erro ao carregar os usuários.</p>'
            console.log(error)
        }
    })
} 

