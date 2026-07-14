import {getUser, getPosts} from './api.js'

function renderUser(user) {
    const container = document.createElement('div')
    container.classList.add('container-user')
    container.innerHTML = `
        <h2>${user.name}</h2>
        <p>${user.id}</p>
    `
    return container
}

function renderPost(post, user) {
    const container = document.createElement('div')
    container.classList.add('container-post')
    container.innerHTML = `
        <h3>${post.title}</h3>
        <p>${post.body}</p>
    `
    return container
}

export async function renderizarUsers() {
    botao.addEventListener('click', async () => {
        const users = await getUser()
        const container = document.createElement('div')
        container.classList.add('container-user')
        return users.map(user => renderUser(user))
    }    
        
    )
}

