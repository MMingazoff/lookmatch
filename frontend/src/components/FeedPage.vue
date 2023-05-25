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
        <select v-model="selectedMood">
          <option value="good">Good</option>
          <option value="bad">Bad</option>
        </select>
      </div>
      <!-- The button has been added here -->
      <div class="add-look-button">
        <button @click="addLook">Add Look</button>
      </div>
    </div>

    <div class="grid">
      <div v-for="item in filteredItems" :key="item.id" class="grid-item">
        <img :src="item.images[item.currentImageIndex]" @click="nextImage(item)" class="item-image">
        <h2>{{ item.mood }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
import {computed, onMounted, ref} from 'vue';
import router from "../../route/route";
import api from "../../api/api";
// import CarouselPhotos from "@/components/Carousel.vue";

export default {
  name: 'FeedPage',
  components: {
    // CarouselPhotos
  },
  setup() {
    const items = ref([]); // should be replaced by API call
    const tempRange = ref({min: null, max: null});
    const selectedMood = ref("good");

    const filteredItems = computed(() => {
      return items.value.filter((item) => {
        const isInTempRange = item.temp >= tempRange.value.min &&
            (item.temp <= tempRange.value.max || !tempRange.value.max);
        const matchesMood = item.mood === selectedMood.value;
        return isInTempRange && matchesMood;
      });
    });

    onMounted(() => {
      api.get('looks').then((response) => {
        const newData = []
        for (let i = 0; i < response.data.length; i++) {
          const newValue = response.data[i]
          newValue['temp'] = JSON.parse(newValue['weather_range'])['lower']
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
