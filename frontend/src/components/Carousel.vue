<template>
  <div class="photo-component-wrapper">
    <div class="photo-component">
      <div class="photo-container">
        <button class="arrow left" id="btnPrev" type="button" @click="prevPicture">&lt;</button>
        <div class="image-frame">
          <img :src="carousel_data[position]" alt="Sample" class="photo"/>
        </div>
        <button class="arrow right" id="btnNext" type="button" @click="nextPicture">&gt;</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CarouselPhotos",
  props: {
    carousel_data: {
      type: Array,
      default: () => [],
    }
  },
  data(props) {
    return {
      len: props.carousel_data.length,
      position: 0,
    }
  },
  methods: {

    nextPicture() {
      if (this.position === this.len - 1)
        this.position = 0
      else
        this.position++
    },
    prevPicture() {
      if (this.position === 0)
        this.position = this.len - 1
      else
        this.position--
    }
  }
}
</script>

<style scoped>
.photo-component-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
}

.photo-component {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.photo-container {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  position: relative;
}

.image-frame {
  border: 2px solid #ccc;
  padding: 10px;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
}

.photo {
  max-width: 200px;
  max-height: 200px;
}

.arrow {
  background-color: transparent;
  border: none;
  font-size: 2rem;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1;
}

.left {
  left: -20px;
}

.right {
  right: -20px;
}
</style>
