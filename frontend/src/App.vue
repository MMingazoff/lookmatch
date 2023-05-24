<template>
  <!--  <HelloWorld msg="Welcome to Your Vue.js App"/>-->
  <!--  <ProfilePage :user="userData"/>-->
  <NavBar/>
  <!--  <LoginPage />-->
  <RegistrationPage/>
  <!--  <ShopPage/>-->
  <!--    <WardrobePage/>-->
  <!--  <ItemManagingPage/>-->
</template>

<script>
// import ProfilePage from "@/components/ProfilePage.vue";
// import ShopPage from "@/components/FeedPage.vue";
// import WardrobePage from "@/components/WardrobePage.vue";
import NavBar from "@/components/NavBar.vue";
// import LoginPage from "@/components/LoginPage.vue";
import RegistrationPage from "@/components/RegistrationPage.vue";
// import ItemManagingPage from "@/components/ItemManagingPage.vue";


export default {
  name: 'App',
  components: {
    // LoginPage,
    RegistrationPage,
    NavBar,
    // ItemManagingPage,
    // ShopPage,
    // WardrobePage
    // ProfilePage,
  },
  data() {
    return {
      userData: {
        photo: 'URL to photo',
        name: 'User Name',
        email: 'User Email',
        // Additional fields can be added here
      }
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
