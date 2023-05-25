<template>
  <nav>
    <router-link :to="{ name: 'Wardrobe' }">
      <div class="logo">LOOKMATCH</div>
    </router-link>
    <div class="nav-buttons">
      <router-link :to="{ name: 'Wardrobe' }">
        <button>Wardrobe</button>
      </router-link>
      <router-link :to="{ name: 'Feed' }">
        <button>Feed</button>
      </router-link>
    </div>
    <div class="nav-buttons">
      <template v-if="!isLoggedIn">
        <router-link :to="{ name: 'Register' }">
          <button>Register</button>
        </router-link>
        <router-link :to="{ name: 'Login' }">
          <button>Login</button>
        </router-link>
      </template>
      <template v-else>
        <button @click="logout">Logout</button>
      </template>
    </div>
  </nav>
</template>

<script>
import router from "../../route/route";
import {onMounted, ref} from "vue";

export default {
  name: "NavBar",
  setup() {
    const isLoggedIn = ref(!!localStorage.getItem("accessToken"));

    const logout = () => {
      localStorage.removeItem("accessToken");
      isLoggedIn.value = false;
      router.push({name: "Login"});
    };

    onMounted(() => {
      window.addEventListener("storage", handleStorageChange);
    });

    const handleStorageChange = (event) => {
      if (event.key === "accessToken") {
        isLoggedIn.value = !!event.newValue;
      }
    };

    return {
      isLoggedIn,
      logout
    };
  }
};
</script>

<style scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #333;
  color: #fff;
}

button {
  padding: 10px 20px;
  font-size: 1em;
}

.logo {
  font-size: 1.5em;
}

.nav-buttons {
  display: flex;
  gap: 15px;
}
</style>
