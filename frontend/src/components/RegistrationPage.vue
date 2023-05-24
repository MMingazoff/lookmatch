<template>
  <div class="registration-page">
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="userData.username" required/>
      </div>

      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="userData.email" required/>
      </div>

      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="userData.password" required minlength="8"/>
      </div>

      <div class="form-group">
        <label for="repeatPassword">Repeat Password:</label>
        <input type="password" id="repeatPassword" v-model="repeatPassword" required/>
        <p v-if="passwordsDoNotMatch" style="color: red;">Passwords do not match!</p>
      </div>

      <button type="submit" :disabled="formInvalid">Register</button>
    </form>
  </div>
</template>

<script>
import {computed, ref} from 'vue';
import axios from 'axios';
import router from "../../route/route";

export default {
  name: 'RegistrationPage',
  setup() {
    const userData = ref({
      username: '',
      email: '',
      password: '',
    });

    const repeatPassword = ref("");

    const passwordsDoNotMatch = computed(() => userData.value.password !== repeatPassword.value);

    const formInvalid = computed(() => !userData.value.username || !userData.value.email || !userData.value.password || passwordsDoNotMatch.value);

    const submitForm = async () => {
      if (formInvalid.value) return;

      axios.post('http://localhost:8000/api/users/', userData.value)
          .then(() => {
            router.push({name: 'Wardrobe'})
          })
    };


    return {
      userData,
      repeatPassword,
      passwordsDoNotMatch,
      formInvalid,
      submitForm
    };
  }
};
</script>

<style scoped>
.registration-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
}
</style>
