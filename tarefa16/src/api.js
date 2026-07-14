const API = 'https://jsonplaceholder.typicode.com/'

export async function getUser() {
    const response = await fetch(`${API}users/`)
    return await response.json()

}

export async function getPosts() {
    const response = await fetch(`${API}posts/`)
    return await response.json()
}
