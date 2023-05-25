<template>
  <div class="page-wrapper">
    <div class="carousel-wrapper">
      <!-- Replace with your carousel component -->
      <div class="carousel">
        <img :src="item.image" alt="Sample" class="photo"/>
      </div>
    </div>

    <div class="info-wrapper">
      <h1 class="title">{{ item.name }}</h1>
      <div class="info">
        <p>{{ item.description }}</p>
        <p>Date added: {{ item.date_added }}</p>
        <p>Color: {{ item.color }}</p>
        <p>Style: {{ item.style }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import {onMounted, ref} from "vue";
import {format, parseISO} from "date-fns";
import api from "../../api/api";

export default {
  name: 'ItemInfoPage',
  props: ['id'],
  setup(props) {
    const item = ref({
      image: '',
      name: '',
      date_added: '',
      description: '',
      category: '',
      style: '',
      color: ''
    });


    onMounted(() => {
      api.get('wardrobe', {
        params: {
          id: props.id,
        }
      }).then((response) => {
        console.log(response)
        item.value = response.data[0]
        item.value.date_added = format(parseISO(item.value.date_added), 'dd-MM-yy HH:mm')
      })
    })

    return {
      item
    };
  }
}
</script>

<style scoped>
.page-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: start;
  padding: 50px;
  height: 100vh;
}

.carousel-wrapper {
  flex-basis: 50%;
  padding-right: 20px;
}

.info-wrapper {
  flex-basis: 50%;
  padding-left: 20px;
}

.title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 20px;
}

.info {
  font-size: 1.2rem;
  margin-bottom: 15px;
}

.carousel {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.photo {
  width: 300px;
  height: 300px;
  object-fit: cover;
}

</style>
