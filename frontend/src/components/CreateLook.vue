<template>
  <div>
    <div class="button-container">
      <button @click="openModal">Create</button>
    </div>

    <section class="section-above"
             @dragover.prevent
             @drop="drop('above')"
    >
      <div
          v-for="item in itemsAbove"
          :key="item.id"
          @dragstart="dragStart(item.id)"
          @dragend="dragEnd"
          draggable
      >
        <img :src="item.image" alt="item image" class="item-image"/>
        <h2>{{ item.name }}</h2>
        <p>{{ item.description }}</p>
      </div>
    </section>

    <section class="section-below"
             @dragover.prevent
             @drop="drop('below')"
    >
      <div
          v-for="item in itemsBelow"
          :key="item.id"
          @dragstart="dragStart(item.id)"
          @dragend="dragEnd"
          draggable
      >
        <img :src="item.image" alt="item image" class="item-image"/>
        <h2>{{ item.name }}</h2>
        <p>{{ item.description }}</p>
      </div>
    </section>

    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <button @click="closeModal" class="close-btn">X</button>
        <form @submit.prevent="submitForm" class="form">
          <div class="form-field">
            <label for="is-public">Is public:</label>
            <input type="checkbox" id="is-public" v-model="form.isPublic"/>
          </div>
          <div class="form-field">
            <label for="min-temp">Min Temperature:</label>
            <input type="number" id="min-temp" v-model.number="form.minTemp" pattern="\d*"/>
            <label for="max-temp">Max Temperature:</label>
            <input type="number" id="max-temp" v-model.number="form.maxTemp" pattern="\d*"/>
          </div>
          <div class="form-field">
            <label for="mood">Mood:</label>
            <select id="mood" v-model="form.mood">
              <option v-for="mood in moods" :key="mood.id" :value="mood.id">
                {{ mood.mood }}
              </option>
            </select>
          </div>

          <button type="submit" class="submit-btn">Confirm</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import {onMounted, ref} from 'vue';
import api from "../../api/api";
import router from "../../route/route";

export default {
  name: 'CreateLook',
  setup() {
    const itemsAbove = ref([]);
    const itemsBelow = ref([]);
    let draggingItem = null;
    const showModal = ref(false);
    const form = ref({
      isPublic: false,
      minTemp: null,
      maxTemp: null,
      mood: '',
    });
    const moods = ref([])

    onMounted(() => {
      api.get('looks/moods').then((response) => {
        moods.value = response.data
      })
    })

    const openModal = () => {
      showModal.value = true;
    };

    const closeModal = () => {
      showModal.value = false;
    };

    const submitForm = async () => {
      const itemIds = itemsAbove.value.map((item) => Number(item.id));
      const payload = {
        public: form.value.isPublic,
        clothing_items: itemIds,
        mood: form.value.mood,
        weather_range: [form.value.minTemp, form.value.maxTemp]
      };

      api.post('looks/', payload)
          .then(() => {
            closeModal();
            router.push({name: 'Feed'});
          })
          .catch((error) => {
            console.error(error);
            // Handle error
          });
    };

    const fetchItems = async () => {
      api.get('wardrobe').then((response) => {
        itemsBelow.value = response.data
      })
    };

    const dragStart = (id) => {
      draggingItem = id;
    };

    const dragEnd = () => {
      draggingItem = null;
    };

    const drop = (section) => {
      const itemIndexAbove = itemsAbove.value.findIndex((item) => item.id === draggingItem);
      const itemIndexBelow = itemsBelow.value.findIndex((item) => item.id === draggingItem);
      let item;

      if (itemIndexAbove !== -1) {
        item = itemsAbove.value.splice(itemIndexAbove, 1)[0];
      } else if (itemIndexBelow !== -1) {
        item = itemsBelow.value.splice(itemIndexBelow, 1)[0];
      }

      if (section === 'below') {
        itemsBelow.value.push(item);
      } else {
        itemsAbove.value.push(item);
      }
    };

    onMounted(fetchItems);

    return {
      itemsAbove,
      itemsBelow,
      dragStart,
      dragEnd,
      drop,
      openModal,
      closeModal,
      submitForm,
      showModal,
      form,
      moods,
    };
  }
};
</script>

<style scoped>
section {
  border: 1px solid black;
  padding: 10px;
  margin: 10px;
  min-height: 100px;
}

section > div {
  margin: 10px;
  padding: 10px;
  border: 1px solid black;
  cursor: move;
}

.button-container {
  display: flex;
  justify-content: center;
  padding: 10px;
}

.button-container button {
  flex-grow: 1;
  max-width: 100%;
}

.item-image {
  max-width: 200px;
  max-height: 200px;
  object-fit: contain;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  width: 90%;
  max-width: 500px;
  display: flex;
  flex-direction: column;
  align-items: stretch;
}


.close-btn {
  align-self: flex-end;
  margin-bottom: 20px;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-field {
  display: flex;
  flex-direction: column;
}

.submit-btn {
  align-self: center;
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit-btn:hover {
  background-color: #45a049;
}
</style>
