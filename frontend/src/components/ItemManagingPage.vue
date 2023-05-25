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
          <option v-for="category in categories" :key="category.id" :value="category.id">
            {{ category.category }}
          </option>
        </select>
      </div>


      <div class="form-group">
        <label for="color">Color:</label>
        <select id="color" v-model="itemData.color">
          <option v-for="color in colors" :key="color.id" :value="color.id">
            {{ color.color }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="style">Style:</label>
        <input type="text" id="style" v-model="itemData.style"/>
      </div>

      <button type="submit" :disabled="!isFormValid">Save</button>
    </form>
  </div>
</template>

<script>
import {computed, onMounted, ref} from 'vue';
import router from "../../route/route";
import api from "../../api/api";

export default {
  name: 'ItemManagingPage',
  props: ['id'],
  setup(props) {
    const itemData = ref(props.id || {
      image: '',
      name: '',
      category: '',
      color: '',
      style: ''
    });

    const categories = ref([]);
    const colors = ref([]);

    const uploadImage = (event) => {
      itemData.value.image = event.target.files[0];
    };

    const submitForm = () => {
      const formData = new FormData();

      if (itemData.value.image)
        formData.append('image', itemData.value.image);
      formData.append('name', itemData.value.name);
      formData.append('category', itemData.value.category);
      formData.append('color', itemData.value.color);
      formData.append('style', itemData.value.style);
      console.log(formData)
      if (props.id) {
        api.patchForm('wardrobe/' + props.id + '/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          }
        }).then(() => {
          router.push({name: 'Wardrobe'})
        })
      } else {
        api.post('wardrobe/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          }
        }).then(() => {
          router.push({name: 'Wardrobe'})
        })
      }
    };

    onMounted(() => {
      api.get('wardrobe/colors').then((response) => {
        colors.value = response.data
      })
      api.get('wardrobe/categories').then((response) => {
        categories.value = response.data
      })
      if (props.id) {
        api.get('wardrobe', {
          params: {
            id: props.id,
          }
        }).then((response) => {
          console.log(response)
          itemData.value = response.data[0]
          itemData.value.image = ''
        })
      }
    })

    const isFormValid = computed(() => {
      const data = itemData.value;
      return (props.id || data.image) && data.name && data.category && data.color && data.style;
    });

    return {
      itemData,
      categories,
      colors,
      uploadImage,
      submitForm,
      isFormValid,
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
