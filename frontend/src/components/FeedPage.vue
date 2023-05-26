<template>
  <div>
    <div class="filters">
      <div>
        <label>Temperature Range:</label>
        <input v-model="tempRange.min" placeholder="Min">
        <input v-model="tempRange.max" placeholder="Max">
      </div>
      <div>
        <label>Mood:</label>
        <select id="mood" v-model="selectedMood">
          <option v-for="mood in moods" :key="mood.id" :value="mood">
            {{ mood.mood }}
          </option>
        </select>
      </div>
      <div class="add-look-button">
        <button @click="addLook">Add Look</button>
      </div>
    </div>

    <div class="grid">
      <div v-for="item in filteredItems" :key="item.id" class="grid-item">
        <img :src="item.images[item.currentImageIndex]" @click="nextImage(item)" class="item-image">
        <h2>{{ item.description }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
import {computed, onMounted, ref} from 'vue';
import router from "../../route/route";
import api from "../../api/api";

export default {
  name: 'FeedPage',
  components: {
  },
  setup() {
    const items = ref([]);
    const tempRange = ref({min: null, max: null});
    const selectedMood = ref();
    const moods = ref([])

    onMounted(() => {
      api.get('looks/moods').then((response) => {
        moods.value = response.data
        moods.value.push({id: -1, mood: 'any'})
        selectedMood.value = moods.value[0]
      })
    })

    const filteredItems = computed(() => {
      return items.value.filter((item) => {
        const isInTempRange = item.tempMin >= tempRange.value.min &&
            (item.tempMax <= tempRange.value.max || !tempRange.value.max);
        const matchesMood = item.mood === selectedMood.value.mood || selectedMood.value.id === -1
        return isInTempRange && matchesMood;
      });
    });

    onMounted(() => {
      api.get('looks').then((response) => {
        const newData = []
        for (let i = 0; i < response.data.length; i++) {
          const newValue = response.data[i]
          newValue['tempMin'] = JSON.parse(newValue['weather_range'])['lower']
          newValue['tempMax'] = JSON.parse(newValue['weather_range'])['upper']
          newValue['images'] = newValue['clothing_items'].map((uri) => "http://localhost:8000" + uri)
          newValue['currentImageIndex'] = 0
          newData.push(newValue)
        }
        console.log(newData)
        items.value = newData
      })
    });

    const addLook = () => {
      router.push({name: 'CreateLook'})
    };

    const nextImage = (item) => {
      item.currentImageIndex = (item.currentImageIndex + 1) % item.images.length;
    };

    return {
      items,
      tempRange,
      selectedMood,
      filteredItems,
      addLook,
      nextImage,
      moods,
    };
  }
};
</script>

<style scoped>
.filters {
  display: flex;
  justify-content: flex-start;
  gap: 20px;
  padding: 20px;
  background-color: #eee;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  padding: 20px;
}

.grid-item {
  border: 1px solid #ccc;
  padding: 10px;
  text-align: center;
}

.item-image {
  width: 100%;
  height: 300px;
  object-fit: cover;
  cursor: pointer;
}
</style>
