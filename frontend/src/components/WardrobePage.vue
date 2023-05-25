<template>
  <div class="wardrobe">
    <div class="header">
      <input type="text" v-model="searchTerm" placeholder="Search by name..." class="searchbar"/>
      <button @click="addItem" class="add-button">Add</button>
    </div>

    <div class="grid">
      <div v-for="item in filteredItems" :key="item.id" class="grid-item">
        <router-link :to="{ name: 'ItemInfo', params: { id: item.id }}">
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
import router from "../../route/route";
import api from "../../api/api";

export default {
  name: 'WardrobePage',
  setup() {
    const items = ref([]);
    const searchTerm = ref("");

    const filteredItems = computed(() => {
      if (!searchTerm.value) return items.value;
      return items.value.filter(item => item.name.toLowerCase().includes(searchTerm.value.toLowerCase()));
    });


    onMounted(() => {
      api.get('wardrobe').then((response) => {
        items.value = response.data
      })
    });

    const addItem = () => {
      router.push({name: 'ItemManagingAdd'})
    };

    const editItem = (id) => {
      router.push({name: 'ItemManagingEdit', params: {id: id}})
    };

    const deleteItem = (id) => {
      api.delete('wardrobe/' + id + '/').then(() => {
        items.value = items.value.filter(item => item.id !== id);
      })
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
  border: 2px solid #000; /* black frame */
  padding: 10px;
  background-color: #fff; /* white background */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* optional: box-shadow for a bit of depth */
}

.item-image {
  width: 300px;
  height: 300px;
  object-fit: cover;
}

.edit-button,
.delete-button {
  margin-top: 10px;
  padding: 5px 10px;
  font-size: 14px;
}
</style>
