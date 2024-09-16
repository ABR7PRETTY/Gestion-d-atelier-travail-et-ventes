
import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from "@/components/Dashboard.vue";
import Apprenti from "@/components/Apprenti.vue";
import Atelier from "@/components/Atelier.vue";
import Article from "@/components/Article.vue";
import Categorie from "@/components/Categorie.vue";
import Vente from "@/components/Vente.vue";
import Designation from "@/components/Designation.vue";
import login from "@/components/Login.vue";
import Mois from "@/components/Mois.vue";
import Depense from "@/components/Depense.vue";

const route = createRouter({
    history: createWebHistory(),
    routes: [

        {
            path: '/',
            name: 'Login',
            component:login
        },

        {
            path: '/Dashboard',
            name: 'Dashboard',
            component:Dashboard
        },
        {
            path: '/Apprenti',
            name: 'Apprenti',
            component:Apprenti
        },
        {
            path: '/Atelier',
            name: 'Atelier',
            component:Atelier
        },
        {
            path: '/Article',
            name: 'Article',
            component:Article
        },
        {
            path: '/Categorie',
            name: 'Categorie',
            component:Categorie
        },
        {
            path: '/Vente',
            name: 'Vente',
            component:Vente
        },

        {
            path: '/Designation',
            name: 'Designation',
            component:Designation
        },
        {
            path: '/Mois',
            name: 'Mois',
            component:Mois
        },
        {
            path: '/Depense',
            name: 'Depense',
            component:Depense
        },




    ]
});

route.beforeEach((to, from, next) => {
    const isAuthenticated = !!localStorage.getItem('token'); // Exemple d'utilisation du token pour vérifier l'authentification

    if (to.name !== 'Login' && !isAuthenticated) {
        next({ name: 'Login' });
    } else {
        next();
    }
});
export default route