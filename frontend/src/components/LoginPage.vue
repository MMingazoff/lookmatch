<template>
  <div class="login-page">
    <form @submit.prevent="submitForm" class="login-form">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="text" id="email" v-model="loginData.username" required/>
      </div>

      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="loginData.password" required/>
      </div>

      <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>

      <button type="submit" :disabled="formInvalid">Submit</button>
      <button type="button" @click="githubLogin">Login via GitHub</button>
    </form>
  </div>
</template>

<script>
import {computed, ref} from 'vue';
import axios from 'axios';
import route from "../../route/route";

export default {
  name: 'LoginPage',
  setup() {
    const loginData = ref({
      username: '',
      password: '',
    });

    const errorMessage = ref("");

    const formInvalid = computed(() => !loginData.value.username || !loginData.value.password);

    const submitForm = async () => {
      if (formInvalid.value) return;

      axios.post('http://localhost:8000/api/users/login/', loginData.value)
          .then((response) => {
            localStorage.setItem('accessToken', response.data.access);
            localStorage.setItem('refreshToken', response.data.refresh);
            route.push({name: 'Wardrobe'})
          })
          .catch(() => {
            errorMessage.value = "Invalid login or password"
          })
    };

    const githubLogin = () => {
      // window.location.href = "`https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${callbackUrl}&scope=read:user`"
      window.location.href = 'http://localhost:8000/api/users/github/login?redirect_to=http://localhost:8080/login'
    };

    return {
      loginData,
      errorMessage,
      formInvalid,
      submitForm,
      githubLogin
    };
  },
  created() {
    let access = this.$route.query.access
    if (access) {
      localStorage.setItem('accessToken', access);
      localStorage.setItem('refreshToken', this.$route.query.refresh);
      this.$router.push({name: 'Wardrobe'})
    }
  }
};
</script>


<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
}
</style>
