import {createRouter, createWebHistory} from 'vue-router'
import WardrobePage from "@/components/WardrobePage.vue";
import ItemManagingPage from "@/components/ItemManagingPage.vue";
import LoginPage from "@/components/LoginPage.vue";
import RegistrationPage from "@/components/RegistrationPage.vue";
import FeedPage from "@/components/FeedPage.vue";
import ItemInfoPage from "@/components/ItemInfoPage.vue";
import CreateLook from "@/components/CreateLook.vue";

const routes = [
    {
        path: '/wardrobe',
        name: 'Wardrobe',
        component: WardrobePage
    },
    {
        path: '/wardrobe/edit/:id',
        name: 'ItemManagingEdit',
        component: ItemManagingPage,
        props: true
    },
    {
        path: '/wardrobe/add',
        name: 'ItemManagingAdd',
        component: ItemManagingPage,
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginPage
    },
    {
        path: '/register',
        name: 'Register',
        component: RegistrationPage
    },
    {
        path: '/feed',
        name: 'Feed',
        component: FeedPage
    },
    {
        path: '/wardrobe/:id',
        name: 'ItemInfo',
        component: ItemInfoPage,
        props: true
    },
    {
        path: '/create_look',
        name: 'CreateLook',
        component: CreateLook,
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
