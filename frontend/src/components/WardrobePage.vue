<template>
  <div class="wardrobe">
    <div class="header">
      <input type="text" v-model="searchTerm" placeholder="Search by name..." class="searchbar"/>
      <button @click="addItem" class="add-button">Add</button>
    </div>

    <div class="grid">
      <div v-for="item in filteredItems" :key="item.id" class="grid-item">
        <router-link :to="/wardrobe/">
          <img :src="item.image" class="item-image"/>
        </router-link>
        <h2>{{ item.name }}</h2>
        <button @click="editItem(item.id)" class="edit-button">Edit</button>
        <button @click="deleteItem(item.id)" class="delete-button">Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
import {computed, onMounted, ref} from 'vue';
import axios from "axios";

export default {
  name: 'WardrobePage',
  /*  data: () => ({
      items: []
    }),*/
  setup() {
    const items = ref([/* {
        id: 1,
        name: 'Item 1',
        image: 'https://via.placeholder.com/150'
      },
        {
        id: 2,
        name: 'Item 2',
        image: 'https://via.placeholder.com/150'
      },
        {
        id: 3,
        name: 'Item 3',
        image: 'https://via.placeholder.com/150'
      },
        {
        id: 4,
        name: 'Item 4',
        image: 'https://via.placeholder.com/150'
      },
      // ...more items...*/]);
    const searchTerm = ref("");

    const filteredItems = computed(() => {
      if (!searchTerm.value) return items.value;
      return items.value.filter(item => item.name.toLowerCase().includes(searchTerm.value.toLowerCase()));
    });

    onMounted(() => {
      axios.get('http://localhost:8000/api/wardrobe').then((response) => {
        items.value = response.data
      })
    });

    const addItem = () => {
      // Handle item addition here...
    };

    const editItem = () => {
      // Handle item edit here...
    };

    const deleteItem = (id) => {
      items.value = items.value.filter(item => item.id !== id);
    };

    return {
      searchTerm,
      filteredItems,
      addItem,
      editItem,
      deleteItem
    };
  }
};

</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.searchbar {
  width: 70%;
  padding: 10px;
  font-size: 16px;
}

.add-button {
  padding: 10px;
  font-size: 16px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.grid-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.item-image {
  width: 100%;
  height: auto;
}

.edit-button,
.delete-button {
  margin-top: 10px;
  padding: 5px 10px;
  font-size: 14px;
}
</style>
