<template>
  <div class="form-page">
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="photo">Photo:</label>
        <input type="file" id="photo" @change="uploadImage"/>
      </div>

      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="itemData.name"/>
      </div>

      <div class="form-group">
        <label for="category">Category:</label>
        <select id="category" v-model="itemData.category">
          <option v-for="category in categories" :key="category" :value="category">
            {{ category }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="color">Color:</label>
        <select id="color" v-model="itemData.color">
          <option v-for="color in colors" :key="color" :value="color">
            {{ color }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="style">Style:</label>
        <input type="text" id="style" v-model="itemData.style"/>
      </div>

      <button type="submit">{{ formType }}</button>
    </form>
  </div>
</template>

<script>
import {onMounted, ref} from 'vue';
import axios from "axios";

export default {
  name: 'ItemManagingPage',
  props: {
    id: String,
    formType: String,
    defaultData: Object
  },
  setup(props) {
    const itemData = ref(props.defaultData || {
      image: '',
      name: '',
      category: '',
      color: '',
      style: ''
    });

    const categories = ref(['Category 1', 'Category 2', 'Category 3']);
    const colors = ref(['Color 1', 'Color 2', 'Color 3']);

    const uploadImage = (event) => {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = (e) => {
        itemData.value.image = e.target.result;
      };

      reader.readAsDataURL(file);
    };

    const submitForm = () => {
      // Handle form submission here...
      console.log(itemData.value);
    };

    onMounted(() => {
      axios.get('http://localhost:8000/api/wardrobe/id=' + props.id).then((response) => {
        itemData.value = response.data
      })
    })

    return {
      itemData,
      categories,
      colors,
      uploadImage,
      submitForm
    };
  }
};
</script>

<style scoped>
.form-page {
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
