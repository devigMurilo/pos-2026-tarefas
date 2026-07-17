 const api = 'https://swapi.dev/api/'

 export async function getPessoas() {
    try {
        const response = await fetch(`${api}people/`)

        if (!response.ok) {
            throw new Error('Erro na requisição')
        }

        const data = await response.json()
        return data
    } catch (error) {
        console.error('Erro ao buscar pessoas:', error)
        throw error 
    }
}

export async function getNave() {
    try {
        const response = await fetch(`${api}starships/`)
        if (!response.ok) {
            throw new Error('Erro na requisição')
        }

        const data = await response.json()
        return data
    } catch (error) {
        console.error('Erro ao buscar naves:', error)
        throw error
    }
}

export async function getPlaneta() {
    try {
        const response = await fetch(`${api}planets/`)

        if (!response.ok) {
            throw new Error('Erro na requisição')
        }    

        const data = await response.json()
        return data
    } catch (error) {
        console.error('Erro ao buscar planeta:', error)
        throw error 
        }
};