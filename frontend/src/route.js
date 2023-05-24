import {createRouter} from 'vue-router'
import WardrobePage from "@/components/WardrobePage.vue";
import ItemManagingPage from "@/components/ItemManagingPage.vue";

const routes = [
    {
        path: '/wardrobe',
        name: 'ItemList',
        component: WardrobePage
    },
    {
        path: '/wardrobe/:id',
        name: 'ItemInfo',
        component: ItemManagingPage,
        props: true
    },
]

const router = createRouter({
    routes
})

export default router
