<template>
    <div>
        <div class="contenedor-cabecero">


            <div class="contenedor-intro">
                <h1>Geobizi, naturaleza desde el corazón</h1>
                <h3>Gestión de la empresa</h3>
            </div>

        </div>
        <div class="contenedor-principal">
            <div>
                <h2>Iniciar sesión</h2>
                <form @submit.prevent="login">
                    <div>
                        <label for="email">Email:</label>
                        <input type="email" id="email" v-model="email" required>
                    </div>
                    <div>
                        <label for="password">Contraseña:</label>
                        <input type="password" id="password" v-model="password" required>
                    </div>
                    <button type="submit">Acceder</button>
                    <p v-if="error" style="color: red;">{{ error }}</p>
                </form>
            </div>
        </div>


    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const email = ref('')
const password = ref('')
const error = ref('')
const isSubmitting = ref(false)

// La lista de usuarios hardcodeada ya no es necesaria
// const usuarios = [
//     { email: 'admin@geobizi.com', password: 'admin123' },
//     { email: 'usuario@geobizi.com', password: 'usuario123' }
// ]

async function login() {
    isSubmitting.value = true;
    error.value = '';
    try {
        const response = await fetch('http://localhost:8000/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: email.value,
                password: password.value,
            }),
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || 'Error de autenticación');
        }

        // Si el login es exitoso
        localStorage.setItem('autenticado', 'true');
        // Opcional: guardar el rol del usuario para controlar permisos en el frontend
        localStorage.setItem('rol', result.rol);
        router.push('/opciones');

    } catch (e) {
        error.value = e.message;
    } finally {
        isSubmitting.value = false;
    }
}
</script>


<style scoped>
h1 {
    color: var(--green);
}

.contenedor-cabecero {
    padding: 5rem;
    background-image: url('/public/imagenes/foto.png');
    background-size: cover;
    background-position: center;
    background-color: var(--darkgreen);
}

.contenedor-intro {
    background-color: var(--white);
    padding: 2rem;
    border-radius: 0.7rem;
    width: fit-content;
}

.contenedor-principal {
    padding: 2rem;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.contact-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 2rem;
    border: 1px solid var(--shoftgreen);
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(49, 49, 49, 0.7);
    padding-bottom: 2rem;
}


label {
    display: block;
    font-weight: bold;
}

input[type="email"],
input[type="password"] {
    width: 100%;
    padding: 0.5rem;
    font-size: 1rem;
    border: 1px solid var(--shoftgreen);
    background-color: var(--megashoftgreen);
    border-radius: 4px;
    margin: 0.5rem 0;
}

button {
    padding: 0.75rem 1rem;
    background-color: var(--green);
    color: var(--white);
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.3s ease;
}


@media (max-width: 550px) {
    .contenedor-principal {
        flex-direction: column;
    }
}

@media (max-width: 420px) {
    .contenedor-cabecero {
        padding: 2rem;
    }
}
</style>