<template>
  <div class="profile-page">
    <div class="profile-image">
      <img :src="user.photo" alt="Profile photo"/>
    </div>
    <div class="profile-info">
      <h2>{{ user.name }}</h2>
      <p>{{ user.email }}</p>
    </div>
    <div class="additional-info">
      <p v-if="user.address">{{ user.address }}</p>
      <p v-if="user.phone">{{ user.phone }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfilePage',
  props: {
    user: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.profile-page {
  width: 100%;
  height: 100vh;
  padding: 20px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.profile-image img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
}

.profile-info {
  margin-top: 20px;
  text-align: center;
}

.profile-info h2 {
  margin: 0;
  padding: 0;
  font-size: 24px;
}

.profile-info p {
  margin: 5px 0;
  padding: 0;
  font-size: 16px;
}

.additional-info p {
  margin: 5px 0;
  padding: 0;
  font-size: 14px;
  text-align: center;
}
</style>
