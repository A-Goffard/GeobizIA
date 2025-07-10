<template>
    <header :class="{ 'scrolled-nav': scrolledNav }">
        <nav>
            <div class="branding">
                <img src="@/assets/GeobiziLogo.png" class="logo" alt="">
            </div>
            <ul v-show="!mobile" class="navigation">
                <li><router-link class="link" :to="{ name: 'inicio' }">Inicio</router-link></li>
                <li><router-link class="link" to="/actividades">Actividades</router-link></li>
                
                <!-- Menú Desplegable: Gestión -->
                <li class="dropdown">
                    <a class="link">Gestión &#9662;</a>
                    <ul class="dropdown-menu">
                        <li><router-link class="link" to="/clientes">Clientes</router-link></li>
                        <li><router-link class="link" to="/empresas">Empresas</router-link></li>
                        <!-- <li><router-link class="link" to="/participantes">Participantes</router-link></li> -->
                    </ul>
                </li>

                <!-- Menú Desplegable: Contenido -->
                <li class="dropdown">
                    <a class="link">Contenido &#9662;</a>
                    <ul class="dropdown-menu">
                        <li><router-link class="link" to="/documentos">Documentos</router-link></li>
                        <li><router-link class="link" to="/publicaciones">Publicaciones</router-link></li>
                        <li><router-link class="link" to="/facturas">Facturas</router-link></li>
                    </ul>
                </li>

                <li><router-link class="link" to="/proyectos">Proyectos</router-link></li>
                <li><router-link class="link" to="/eventos">Eventos</router-link></li>
                <!-- <li><router-link class="link" to="/redes-sociales">Redes Sociales</router-link></li> -->
            </ul>
            <div class="icon">
                <button @click="toggleMobileNav" v-show="mobile">
                    <img :class="{ 'icon-active': mobileNav }" src="@/assets/Hojitas.png" class="hojitas" alt="">
                </button>
            </div>
            <transition name="mobile-nav">
                <ul v-show="mobileNav" class="dropdown-nav">
                    <li @click="closeMobileNav"><router-link class="link" :to="{ name: 'inicio' }">Inicio</router-link></li>
                    <li @click="closeMobileNav"><router-link class="link" to="/actividades">Actividades</router-link></li>
                    
                    <!-- Menú Desplegable Móvil: Gestión -->
                    <li class="dropdown-mobile">
                        <a @click="toggleDropdown('gestion')" class="link">Gestión &#9662;</a>
                        <ul v-show="activeDropdown === 'gestion'" class="sub-menu">
                            <li @click="closeMobileNav"><router-link class="link" to="/clientes">Clientes</router-link></li>
                            <li @click="closeMobileNav"><router-link class="link" to="/empresas">Empresas</router-link></li>
                            <!-- <li @click="closeMobileNav"><router-link class="link" to="/participantes">Participantes</router-link></li> -->
                        </ul>
                    </li>

                    <!-- Menú Desplegable Móvil: Contenido -->
                    <li class="dropdown-mobile">
                        <a @click="toggleDropdown('contenido')" class="link">Contenido &#9662;</a>
                        <ul v-show="activeDropdown === 'contenido'" class="sub-menu">
                            <li @click="closeMobileNav"><router-link class="link" to="/documentos">Documentos</router-link></li>
                            <li @click="closeMobileNav"><router-link class="link" to="/publicaciones">Publicaciones</router-link></li>
                            <li @click="closeMobileNav"><router-link class="link" to="/facturas">Facturas</router-link></li>
                        </ul>
                    </li>

                    <li @click="closeMobileNav"><router-link class="link" to="/proyectos">Proyectos</router-link></li>
                    <li @click="closeMobileNav"><router-link class="link" to="/eventos">Eventos</router-link></li>
                    <!-- <li @click="closeMobileNav"><router-link class="link" to="/redes-sociales">Redes Sociales</router-link></li> -->
                </ul>
            </transition>
        </nav>
    </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const mobileNav = ref(false);
const mobile = ref(true);
const scrolledNav = ref(false);
const activeDropdown = ref(null); // Para controlar el desplegable en móvil

const toggleDropdown = (menu) => {
    if (activeDropdown.value === menu) {
        activeDropdown.value = null;
    } else {
        activeDropdown.value = menu;
    }
};

const toggleMobileNav = () => {
    mobileNav.value = !mobileNav.value;
    const hojitasIcon = document.querySelector('.hojitas');
    if (hojitasIcon) {
        hojitasIcon.style.transform = mobileNav.value ? 'rotate(45deg)' : 'rotate(0deg)';
    }
    if (!mobileNav.value) {
        activeDropdown.value = null; // Cierra submenús al cerrar nav principal
    }
};

const closeMobileNav = () => {
    mobileNav.value = false;
    const hojitasIcon = document.querySelector('.hojitas');
    if (hojitasIcon) {
        hojitasIcon.style.transform = 'rotate(0deg)';
    }
    activeDropdown.value = null; // Cierra submenús
};

const updateScroll = () => {
    scrolledNav.value = window.scrollY > 50;
};

const checkScreen = () => {
    mobile.value = window.innerWidth <= 990;
    if (mobile.value) {
        mobileNav.value = false;
    }
};

const closeOnClickOutside = (event) => {
    const nav = document.querySelector('.dropdown-nav');
    const button = document.querySelector('.icon button');

    if (mobileNav.value && nav && !nav.contains(event.target) && button && !button.contains(event.target)) {
        closeMobileNav();
    }
};

onMounted(() => {
    window.addEventListener('resize', checkScreen);
    window.addEventListener('scroll', updateScroll);
    document.addEventListener('click', closeOnClickOutside);
});

onUnmounted(() => {
    window.removeEventListener('resize', checkScreen);
    window.removeEventListener('scroll', updateScroll);
    document.removeEventListener('click', closeOnClickOutside);
});

checkScreen();
</script>

<style scoped>
header {
    box-sizing: border-box;
    background-color: var(--white);
    z-index: 99;
    width: 100%;
    position: fixed;
    height: 3.5rem;
    transition: 0.5s ease all;
}

header nav {
    position: relative;
    display: flex;
    flex-direction: row;
    padding: 0.5em 0;
    transition: 0.5s ease all;
    width: 100%;
    margin: 0rem 0rem;
}

header nav .branding img {
    max-height: 5rem;
}

header nav .navigation {
    display: flex;
    align-items: center;
    flex: 1;
    justify-content: center;
}

header nav .icon {
    display: flex;
    align-items: center;
    position: absolute;
    top: 0.1rem;
    right: 0.5rem;
}

header nav button {
    width: 4rem;
    cursor: pointer;
    transition: 0.8s ease all;
    background-color: transparent;
    border: none;
    margin: 0.5rem;
}

header nav .hojitas {
    width: 100%;
    transition: transform 0.5s ease;
}

header nav .dropdown-nav {
    display: flex;
    flex-direction: column;
    position: fixed;
    width: 100%;
    max-width: 250px;
    height: 100%;
    background-color: var(--white);
    top: 0;
    left: 0;
    padding-top: 1rem;
}

header nav .dropdown-nav li {
    margin-left: 1rem;
}

header nav .mobile-nav-enter-active,
header nav .mobile-nav-leave-active {
    transition: 1s ease all;
}

header nav .mobile-nav-enter-from,
header nav .mobile-nav-leave-to {
    transform: translateX(-250px);
}

header nav .mobile-nav-enter-to {
    transform: translateX(0);
}

.scrolled-nav {
    background-color: rgba(255, 255, 255, 1);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.scrolled-nav nav {
    padding: 0.5rem 0;
}

.link {
    font-weight: bold;
    color: var(--green);
    position: relative;
    transition: 250s ease all;
    cursor: pointer; /* Para que los <a> no-link parezcan clicables */
}

.link:hover {
    color: var(--lightgreen);
    border-color: var(--lightgreen);
    cursor: pointer;
}

.link:hover::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: -3px;
    width: 100%;
    height: 2px;
    background-color: var(--lightgreen);
    cursor: pointer;
}

ul {
    margin: 0;
    list-style: none; /* Quita los puntos de la lista */
}

li {
    padding: 0.5rem 0.5rem;
    margin-top: 0.2rem;
}

.logo {
    position: absolute;
    height: 2.8rem;
}

/* Estilos para los menús desplegables */
.dropdown {
    position: relative;
}

.dropdown-menu {
    position: absolute;
    top: 100%;
    left: 0;
    background-color: white;
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    border-radius: 4px;
    list-style: none;
    padding: 0.5rem 0;
    margin: 0;
    min-width: 180px;
    opacity: 0;
    visibility: hidden;
    transform: translateY(10px);
    transition: opacity 0.3s ease, transform 0.3s ease, visibility 0.3s;
}

.dropdown:hover .dropdown-menu {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.dropdown-menu li {
    padding: 0;
}

.dropdown-menu .link {
    display: block;
    padding: 0.75rem 1.5rem;
    width: 100%;
    box-sizing: border-box;
}

.dropdown-menu .link:hover::after {
    content: none; /* No queremos la línea inferior en los sub-items */
}

/* Estilos para desplegables en móvil */
.dropdown-mobile .sub-menu {
    list-style: none;
    padding-left: 1rem; /* Indentación para los sub-items */
    overflow: hidden;
    max-height: 500px; /* Suficiente para los items */
    transition: max-height 0.5s ease-in-out;
}

.dropdown-mobile .sub-menu[v-show="false"] {
    max-height: 0;
}

@media (min-width: 1024px) {
    li {
        padding: 0.5rem 1.5rem;
    }
}

@media (min-width: 768px) {
    li {
        padding: 0.5rem 1rem;
    }
}
</style>