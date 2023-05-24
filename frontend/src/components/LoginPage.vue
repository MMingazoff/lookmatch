<template>
  <div class="login-page">
    <form @submit.prevent="submitForm" class="login-form">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="loginData.email" required/>
      </div>

      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="loginData.password" required/>
      </div>

      <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>

      <button type="submit" :disabled="formInvalid">Submit</button>
      <button type="button" @click="googleLogin">Login via Google</button>
    </form>
  </div>
</template>

<script>
import {computed, ref} from 'vue';
import axios from 'axios'; // Make sure to install this with npm install axios

export default {
  name: 'LoginPage',
  setup() {
    const loginData = ref({
      email: '',
      password: '',
    });

    const errorMessage = ref("");

    const formInvalid = computed(() => !loginData.value.email || !loginData.value.password);

    const submitForm = async () => {
      if (formInvalid.value) return;

      try {
        const response = await axios.post('/api/login', loginData.value); // Replace with your actual API endpoint
        console.log(response.data);
      } catch (error) {
        errorMessage.value = "Email or password is incorrect"; // Customize this as per your needs
        console.error(error);
      }
    };

    const googleLogin = () => {
      // Handle Google login here...
      console.log("Login via Google clicked");
    };

    return {
      loginData,
      errorMessage,
      formInvalid,
      submitForm,
      googleLogin
    };
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
