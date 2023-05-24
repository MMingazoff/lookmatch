import {createRouter, createWebHistory} from 'vue-router'
import WardrobePage from "@/components/WardrobePage.vue";
import ItemManagingPage from "@/components/ItemManagingPage.vue";

const routes = [
  {
    path: '/wardrobe',
    name: 'Wardrobe',
    component: WardrobePage
  },
  {
    path: '/wardrobe/:id',
    name: 'ItemManaging',
    component: ItemManagingPage,
    props: true
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
