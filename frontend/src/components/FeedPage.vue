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
    </div>

    <div class="grid">
      <div v-for="item in filteredItems" :key="item.id" class="grid-item">
        <Carousel>
          <Slide v-for="img in item.images" :key="img">
            <img :src="img"/>
          </Slide>
        </Carousel>
        <h2>{{ item.name }}</h2>
        <p>{{ item.additionalData }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import {computed, onMounted, ref} from 'vue';
import {Carousel, Slide} from 'vue3-carousel';

export default {
  name: 'ShopPage',
  components: {
    Carousel,
    Slide
  },
  setup() {
    const items = ref([]); // should be replaced by API call
    const tempRange = ref({min: null, max: null});
    const selectedMood = ref("good");

    const filteredItems = computed(() => {
      return items.value.filter(item => {
        const isInTempRange = item.temp >= tempRange.value.min &&
            (item.temp <= tempRange.value.max || !tempRange.value.max);
        const matchesMood = item.mood === selectedMood.value;
        console.log(tempRange.value.max)
        return isInTempRange && matchesMood;
      });
    });

    onMounted(() => {
      // Replace with API call
      console.log('sdfsdfsdf')
      items.value = [
        {
          id: 1,
          name: 'Item 1',
          images: [
            'https://via.placeholder.com/150',
            'https://via.placeholder.com/150',
            'https://via.placeholder.com/150'
          ],
          additionalData: 'Additional data 1',
          temp: 15,
          mood: 'good'
        },
        {
          id: 2,
          name: 'Item 2',
          images: [
            'https://via.placeholder.com/150',
            'https://via.placeholder.com/150',
            'https://via.placeholder.com/150'
          ],
          additionalData: 'Additional data 2',
          temp: 20,
          mood: 'bad'
        }
        // more items...
      ];
      console.log(items.value)
    });

    return {
      items,
      tempRange,
      selectedMood,
      filteredItems
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

.carousel {
  width: 100%;
  margin-bottom: 15px;
}
</style>
